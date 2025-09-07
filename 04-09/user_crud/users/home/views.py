from django.shortcuts import render, get_object_or_404, redirect
from .models import Users
from .forms import UserForm

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
