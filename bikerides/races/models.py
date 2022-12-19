from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

states = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

class Race(models.Model):
    name = models.CharField(default= "",max_length=24, unique=True)
    state = models.CharField(max_length=16, choices=states)
    city = models.CharField(max_length=16)
    distance = models.IntegerField()
    discipline = models.CharField(max_length=6,choices=(('Gravel', 'Gravel'), ('Road', 'Road'), ('MTB', 'MTB')))
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    email = models.EmailField(verbose_name= 'email address', max_length=64, unique=True)
    username = models.CharField(max_length=16, unique=True)
    friends = models.ManyToManyField('MyUser', blank=True)
    
class FriendRequest(models.Model):
    from_user = models.ForeignKey(MyUser, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(MyUser, related_name='to_user', on_delete=models.CASCADE)
   


