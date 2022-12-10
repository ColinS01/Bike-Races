from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Race, MyUser
from django.forms import ModelForm

class CreatUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ['username', 'email']

class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = MyUser
        fields = ['username', 'email']
        
class CreateRaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ['name', 'state', 'city', 'distance', 'discipline', 'date', 'time']