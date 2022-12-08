from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Race
from django.forms import ModelForm

class CreatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class CreateRaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ['name', 'city', 'state', 'distance', 'date', 'time']