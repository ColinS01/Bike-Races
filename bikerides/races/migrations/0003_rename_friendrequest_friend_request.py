# Generated by Django 4.1.1 on 2022-12-13 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0002_myuser_friends_friendrequest'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FriendRequest',
            new_name='Friend_Request',
        ),
    ]
