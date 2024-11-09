from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from .forms import SignUpForm, LoginForm, ResetPasswordForm
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'User created successfully!'
            return redirect('login_view')
        else:
            msg = 'Form is not valid.'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    # Initialize the authentication form
    form = AuthenticationForm(request, data=request.POST or None)

    # If the request method is POST, validate the form
    if request.method == 'POST':
        if form.is_valid():  # Check if the form is valid
            # Get the cleaned data from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            # If the user exists, log them in and redirect to home
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired URL name

            # If authentication fails, add a message
            else:
                messages.error(request, 'Invalid credentials')

        # If the form is not valid, add an error message
        else:
            messages.error(request, 'Error validating the form')

    # Render the login page with the form and any messages
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login_view')

def reset_password(request):
    msg = None
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            # Reset password logic (you can integrate email-sending)
            msg = 'Password reset link has been sent to your email.'
            return redirect('login_view')
        else:
            msg = 'Please enter a valid email address.'
    else:
        form = ResetPasswordForm()
    return render(request, 'reset_password.html', {'form': form, 'msg': msg})

def student(request):
    return render(request, 'student.html')

def parent(request):
    return render(request, 'parent.html')

def faculty(request):
    return render(request, 'faculty.html')

def coordinator(request):
    return render(request, 'coordinator.html')
