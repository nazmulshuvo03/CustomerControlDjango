from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *


class CustomerForm(ModelForm):
	"""docstring for CustomerForm"""
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
	"""User Registration Form"""
		
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
			