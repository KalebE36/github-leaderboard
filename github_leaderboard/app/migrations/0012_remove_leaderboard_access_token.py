# Generated by Django 3.1.7 on 2021-04-15 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210415_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='access_token',
        ),
    ]
