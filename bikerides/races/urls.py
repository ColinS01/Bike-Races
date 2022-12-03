from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('login/', views.login, name='login'),  
    path('signup/', views.sign_up, name='sign up'),
    path('create/', views.create_race, name='create'),
    path('seeraces/', views.see_races, name='races'),
    path('register/', views.register, name='register'),
    path('myraces/', views.my_races, name='my races'),
]
