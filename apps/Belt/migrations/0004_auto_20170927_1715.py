# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-27 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Belt', '0003_auto_20170927_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='user_destinations',
        ),
        migrations.AddField(
            model_name='destination',
            name='user_destinations',
            field=models.ManyToManyField(related_name='user_destinations', to='Belt.User'),
        ),
    ]
