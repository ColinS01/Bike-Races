from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate
from bikerides.settings import AUTH_USER_MODEL

# Create your views here.


def index(request):
    return render(request, 'races/index.html')

def sign_up(request):
    
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first')
            return HttpResponseRedirect('/login/')
        else:
            messages.error(request, 'Email already in use')
            
    context = {'form':form}
    return render(request, 'races/signup.html', context)

def loginPage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, email, password)
    
    return render(request, 'races/login.html')

def create_race(request):
    pass

def see_races(request):
    pass

def register(request):
    pass

def my_races(request):
    pass