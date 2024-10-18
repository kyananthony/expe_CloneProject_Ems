from urllib import request
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import views as auth_views
from djangoProject import settings
from emssssss.users.forms import CustomPasswordResetForm
import random
import string
from django.core.mail import send_mail
from django.contrib.auth.models import User
def base(request):
    pass
    return render (request, 'base.html')

def register(request):
    pass
    return render (request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
    if user is not None:
        login (request, user)
        return redirect('home')
    else:
        messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

class CustomPasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
class CustomPasswordResetDoneView(auth_views.PasswordResetView):
    form_class = CustomPasswordResetForm
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    # Send email logic
                    send_mail(
                        'Password Reset Requested',
                        'You requested a password reset. Click the link to reset your password.',
                        'from@example.com',
                        [user.email],
                        fail_silently=False,
                    )
            return redirect("/password_reset/done/")
    else:
        password_reset_form = PasswordResetForm()
    return render(request, 'registration/password_reset.html', {'password_reset_form': password_reset_form})
def generate_auth_code(length=6):
    """Generate a random authentication code for admin."""
    characters= string.digits
    auth_code=''.join(random.choice(characters) for i in range(length))
    return auth_code
def admin_auth_code(request):
    """Generates auth code only for admin."""
    is_admin= True
    if is_admin:
        auth_code=generate_auth_code()
        print(f"Admin authenthication code : {auth_code}")
        return auth_code
    else:
        print("Access denied: Only admins can generate auth code.")
        return none

def send_auth_code_email(request, user=None):
    subject = 'Your Authentication Code'
    message = f'Hello {user.username},\n\nYour authentication code is: {auth_code}'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_code = generate_auth_code(request)
            user.profile.auth_code = auth_code
            user.save()

            send_auth_code_email(user, auth_code)

            request.session['user_id'] = user.id
            return redirect('auth_code')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
            return render(request,'login.html')
# views.py

def auth_code_view(request):
    if request.method == 'POST':
        auth_code = request.POST['auth_code']
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)

        # Check if the auth code matches
        if user.profile.auth_code == auth_code:
            login(request, user)  # Log in the user after successful validation
            return redirect('home')  # Redirect to home page or dashboard
        else:
            return render(request, 'auth_code.html', {'error': 'Invalid auth code'})

    return render(request, 'auth_code.html')
