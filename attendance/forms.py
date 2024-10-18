from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmployeeRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmployeeLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    auth_code = forms.CharField(max_length=6)
