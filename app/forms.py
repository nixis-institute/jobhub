from app.models import *
from django.forms import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate

class Registrationform(UserCreationForm):
    username=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    first_name=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
    last_name=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))
    email=forms.EmailField(error_messages={'required': 'already exist!'},widget=forms.TextInput(attrs={'type':"email",'class':"validate form-control",'id':'email','placeholder':'Email Address'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password Repeat'}))
    #password1=forms.PasswordInput(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    #password2=forms.PasswordInput(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Password Repeat'}))
    #phone = forms.IntegerField()
    #phone = forms.IntegerField(widget=forms.TextInput(attrs={'type': "phone", 'class': "validate", 'id': 'phone','name':'phone'}))
    class Meta:
        model = User
        fields =("username","first_name","last_name","email")