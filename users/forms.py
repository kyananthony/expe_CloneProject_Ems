from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import PasswordResetForm
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(atttrs={
        'class': 'form-contol',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})