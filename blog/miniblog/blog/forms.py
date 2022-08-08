from cProfile import label
from dataclasses import fields
from multiprocessing import AuthenticationError
from turtle import textinput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post
class singupForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password',widget= forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password',widget= forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model= User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First_Name','last_name':'Last_Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),}

class EditUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','date_joined','last_login']

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplate':'current-password','class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','decs']
        labels = {'title':'Title','decs':'Descrptioon'}
        widgets = {'title':forms.TextInput(attrs={'class':'from-control'}),
        'decs':forms.Textarea(attrs={'class':'from-control'})}
