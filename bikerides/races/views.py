from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

def create_race(request):
    form = CreateRaceForm()

    if request.method == 'POST':
        form = CreateRaceForm(request.POST)
        
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'races/newrace.html', context)

def send_friend_request(request, id):
    from_user = request.user
    to_user = MyUser.objects.get(id=id)
    friend_requests = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
    return HttpResponseRedirect('/friends/')

def accept_friend_request(request, id):
    friend_request = FriendRequest.objects.get(id=id)
    user1 = request.user
    user2 = friend_request.from_user
    user1.friends.add(user2)
    user2.friends.add(user1)
    friend_request.delete()
    return HttpResponseRedirect('/friends/')
    

def friends(request):
    allusers = MyUser.objects.exclude(username = request.user)
    requests = FriendRequest.objects.filter(to_user = request.user)
    return render(request, 'races/friends.html', 
                  {
                      'allusers':allusers,
                      'requests': requests
                  })


def see_races(request):
    return render(request, 'races/seeraces.html')

def register(request):
    pass

def my_races(request):
    pass