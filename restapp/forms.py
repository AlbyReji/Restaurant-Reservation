from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from restapp.models import bookingdetails,contactdetails,restdetails

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'type': 'char', 'class':'form-control form-control' ,'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'char', 'class':'form-control form-control' ,'placeholder': 'Email'}))
    phone_no = forms.CharField(max_length=20 ,widget=forms.TextInput(attrs={'type': 'char', 'class':'form-control form-control' ,'placeholder': 'Enter Your Phone'}))
    first_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'type': 'char', 'class':'form-control form-control' ,'placeholder': 'Enter Your First Name'}))
    last_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'type': 'char', 'class':'form-control form-control' ,'placeholder': 'Enter Your Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control','placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control','placeholder': 'confirm Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class bookingdetailsform(forms.ModelForm):
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class':'form-control timepicker'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control datepicker'}))
    totalpeople = forms.CharField(widget=forms.TextInput(attrs={'type': 'char', 'class':'form-control form-control' ,'placeholder': 'totalpeople'}))

    class Meta:
        model = bookingdetails
        fields = ['time','date','totalpeople']

class contactdetailsform(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'type': 'char', 'class':'form-control form-control' ,'placeholder': 'Name'}))
    Phone = forms.CharField(widget=forms.TextInput(attrs={'type': 'char', 'class':'form-control form-control' ,'placeholder': 'Phone'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'char', 'class':'form-control form-control' ,'placeholder': 'Email'}))
    # Subject = forms.TextField(widget=forms.TextInput(attrs={'type': 'Text', 'class':'form-control form-control' ,'placeholder': 'totalpeople'}))


    class Meta:
        model = contactdetails
        fields = ['Name','Phone','Email','Subject']
    
class restdetailsform(forms.ModelForm):
    special = forms.CharField(widget=forms.TextInput(attrs={'type': 'char', 'class':'form-control form-control' ,'placeholder': 'special'}))
    opentime = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class':'form-control timepicker'}))
    closetime = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class':'form-control timepicker'}))


    class Meta:
        model = restdetails
        fields = ['special','opentime','closetime']

