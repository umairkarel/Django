from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	# Gives namespace for configs
	class Meta:
		model = User #form.save saves in user model
		fields = ['username', 'email', 'password1', 'password2'] #fields needed in form and in what order

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	# Gives namespace for configs
	class Meta:
		model = User #form.save saves in user model
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']