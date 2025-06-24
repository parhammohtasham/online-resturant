from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'address',  'zip_code', 'image','date_joined')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'address', 'zip_code','image','date_joined')