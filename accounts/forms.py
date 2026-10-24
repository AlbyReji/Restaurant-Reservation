from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'char', 'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'char', 'class': 'form-control', 'placeholder': 'Email'}))
    phone_no = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'char', 'class': 'form-control', 'placeholder': 'Enter Your Phone'}))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'char', 'class': 'form-control', 'placeholder': 'Enter Your First Name'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'char', 'class': 'form-control', 'placeholder': 'Enter Your Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_no', 'password1', 'password2']
