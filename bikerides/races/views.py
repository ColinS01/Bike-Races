from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'races/index.html')

def sign_up(request):
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