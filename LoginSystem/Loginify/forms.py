from django import forms
from .models import UserDetails

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
