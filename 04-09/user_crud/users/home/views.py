from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.sites.shortcuts import get_current_site
from .models import Users
from django.contrib.auth import login
from .forms import UserForm,RegisterForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = Users.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect('user_list')
        else:
            error = "Invalid username or password."

    return render(request, 'login.html', {'error': error})


def logout_view(request):
    request.session.flush() 
    return redirect('login')


def user_list(request):
    if not request.session.get('user_id'):
        return redirect('login')

    users = Users.objects.all()
    return render(request, 'user_list.html', {'users': users})


def add_user(request):
    if not request.session.get('user_id'):
        return redirect('login')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() and request.POST.get('age').isdigit() and 0 <= int(request.POST.get('age')) <= 100:
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form})


def update_user(request, user_id):
    if not request.session.get('user_id'):
        return redirect('login')

    user = get_object_or_404(Users, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    return render(request, 'update_user.html', {'form': form})


def delete_user(request, user_id):
    if not request.session.get('user_id'):
        return redirect('login')

    if request.method == 'POST':
        user = get_object_or_404(Users, id=user_id)
        user.delete()

    return redirect('user_list')

def activate(request,uidb64,token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        User=get_user_model()
        user=User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError<User.DoesNotExist):
        user=None

    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.save()
        return render(request,'activation_success.html')
    else:
        return render(request,'activation_invalid.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['email']

        user=Users.objects.create_user(username=username,email=email,password=password)

        user.is_active = False
        current_site=get_current_site(request)
        mail_subject='Activate your account.'
        message=render_to_string('acc_active_email.html',{
            'user':user,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        email_message=EmailMessage(mail_subject,message,to=[email])
        email_message.send()

        return render(request,'please_confirm.html')
    return render(request,'register.html')    