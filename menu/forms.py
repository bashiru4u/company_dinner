from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="Full Name",  # change “Name” to “Full Name”
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your full name'
        })
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'placeholder': 'Choose a unique username'
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Create a secure password'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Re‑type your password'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']
