from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'), 
    path('login/', views.loginPage, name='login'),  
    path('logout/', views.logoutUser, name='logout'), 
    path('friends/', views.friends, name='friends'), 
    path('send_friend_request/<int:id>/', views.send_friend_request, name='send friend request'),
    path('accept_friend_request/<int:id>/', views.accept_friend_request, name='accept friend request'),
    path('signup/', views.sign_up, name='sign up'),
    path('create/', views.create_race, name='create'),
    path('seeraces/', views.see_races, name='races'),
    path('register/', views.register, name='register'),
    path('myraces/', views.my_races, name='my races'),
]
