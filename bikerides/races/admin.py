from django.contrib import admin
from .models import Race, MyUser
from .forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = MyUser
    list_display = ['username', 'email', 'password']
    
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Race)

