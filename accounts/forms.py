from pyexpat import model
from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user',]

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', ]