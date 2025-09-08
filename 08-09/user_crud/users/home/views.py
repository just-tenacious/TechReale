from django.shortcuts import render, get_object_or_404, redirect
from .models import Users
from .forms import UserForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserForm
from django.urls import reverse
import random

# def register_view(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid() and request.POST.get('age').isdigit() and 0 <= int(request.POST.get('age')) <= 100:
#             form.save()
#             return redirect('login')
#     else:
#         form = UserForm()
#     return render(request, 'register.html', {'form': form})

def generate_otp():
    return random.randint(100000, 999999)

def register_view(request):
    if request.method == "POST":
        if 'otp' in request.POST:  # OTP verification step
            user_otp = request.POST.get('otp')
            session_otp = request.session.get('otp')

            if session_otp and str(user_otp) == str(session_otp):
                # OTP correct - now save user data from session
                user_data = request.session.get('user_data')
                if user_data:
                    form = UserForm(user_data)
                    if form.is_valid():
                        user = form.save(commit=False)
                        user.is_email_verified = True  # mark email verified
                        user.save()

                        # Clear session data after successful registration
                        request.session.pop('otp', None)
                        request.session.pop('user_data', None)

                        return redirect('login')  # Redirect after successful registration
                    else:
                        # Form invalid on second validation (rare but possible)
                        return render(request, 'register.html', {'form': form})
                else:
                    # No user data in session, redirect to registration form
                    return redirect('register')
            else:
                context = {'otp_error': 'Invalid OTP. Please try again.'}
                return render(request, 'otp_verify.html', context)

        else:
            # Registration form submission step
            form = UserForm(request.POST)
            if form.is_valid():
                # Save user data in session temporarily
                request.session['user_data'] = request.POST.dict()
                otp = generate_otp()
                request.session['otp'] = otp

                # Send OTP email
                subject = 'Your OTP Verification Code'
                message = f'Your OTP code is {otp}. It is valid for 10 minutes.'
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [request.POST.get('email')]

                send_mail(subject, message, from_email, recipient_list)

                return render(request, 'otp_verify.html')
            else:
                return render(request, 'register.html', {'form': form})

    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def verify_email_view(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        session_otp = str(request.session.get('otp'))
        verify_user_id = request.session.get('verify_user_id')

        if not verify_user_id:
            return redirect('login')

        if session_otp and user_otp == session_otp:
            user = get_object_or_404(Users, id=verify_user_id)
            user.is_email_verified = True
            user.save()

            # Clean up session
            request.session.pop('otp', None)
            request.session.pop('verify_user_id', None)

            return redirect('user_list')
        else:
            return render(request, 'otp_verify.html', {'otp_error': 'Invalid OTP. Please try again.'})

    return render(request, 'otp_verify.html')


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


# def user_list(request):
#     if not request.session.get('user_id'):
#         return redirect('login')

#     users = Users.objects.all()
#     return render(request, 'user_list.html', {'users': users})

def user_list(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = get_object_or_404(Users, id=user_id)

    if not user.is_email_verified:
        # Generate and send OTP
        otp = generate_otp()
        request.session['otp'] = otp
        request.session['verify_user_id'] = user.id  # to know which user to verify

        subject = 'Email Verification Required'
        message = f'Your OTP code is {otp}. It is valid for 10 minutes.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)

        return redirect('verify_email')  # NEW view we’ll add below

    # User is verified
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
            return render(request, 'update_user.html', {'form': form, 'errors': form.errors})
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
