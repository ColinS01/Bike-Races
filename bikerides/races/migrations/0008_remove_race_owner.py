# Generated by Django 4.1.1 on 2022-12-20 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0007_race_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='owner',
        ),
    ]