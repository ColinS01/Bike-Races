from django.forms import ModelForm
from .models import User, Race
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = {
            'first': forms.TextInput(attrs={'class': 'first'}),
            'last': forms.TextInput(attrs={'class': 'last'}),
            'email': forms.TextInput(attrs={'class': 'email'}),
            'password': forms.TextInput(attrs={'class': 'password'}),
            'sex': forms.TextInput(attrs={'class': 'first'}),
            'age': forms.TextInput(attrs={'class': 'last'})
        }

