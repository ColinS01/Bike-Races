# Generated by Django 4.1.1 on 2022-12-16 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0003_rename_friendrequest_friend_request'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Friend_Request',
            new_name='FriendRequest',
        ),
    ]