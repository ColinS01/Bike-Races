from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, 'races/index.html')

def sign_up(request):
    if request.POST == 'POST':
        form = UserForm()
        if form.is_valid():
            form.save()
        return render(request, 'races/dashboard.html')

    return render(request, 'races/signup.html')

def login(request):
    return render(request, 'races/login.html')

def create_race(request):
    pass

def see_races(request):
    pass

def register(request):
    pass

def my_races(request):
    pass