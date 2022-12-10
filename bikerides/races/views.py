from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, 'races/index.html')

def sign_up(request):
    
    form = CreatUserForm()

    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        else:
            messages.error(request, 'Email or Username already in use')
            
    context = {'form':form}
    return render(request, 'races/signup.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/')
        else:
            messages.info(request, 'Username OR Password incorrect')
    
    return render(request, 'races/login.html')

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def sendFriendRequest(request, userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    friendRequest, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
    if created:
        messages.info(request, 'Friend Request Sent')
    else:
        messages.info(request, 'Friend Request Already Sent')

def acceptFreindRequest(request, requestID):
    friendRequest = FriendRequest.objects.get(id=requestID)
    # https://medium.com/analytics-vidhya/add-friends-with-689a2fa4e41d to finish friend system

def friends(request):
    return render(request, 'races/friends.html')
    

def create_race(request):
    form = CreateRaceForm()

    if request.method == 'POST':
        form = CreateRaceForm(request.POST)
        
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'races/newrace.html', context)

def see_races(request):
    pass

def register(request):
    pass

def my_races(request):
    pass