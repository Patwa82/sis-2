from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control"}
        )
    )
    is_student = forms.BooleanField(required=False, label="Student")
    is_parent = forms.BooleanField(required=False, label="Parent")
    is_faculty = forms.BooleanField(required=False, label="Faculty")
    is_coordinator = forms.BooleanField(required=False, label="Course Coordinator")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_student', 'is_parent', 'is_faculty', 'is_coordinator')


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email"}
        )
    )
