# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-28 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Belt', '0007_auto_20170927_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='user_destinations',
        ),
        migrations.AddField(
            model_name='destination',
            name='users',
            field=models.ManyToManyField(related_name='destinations', to='Belt.User'),
        ),
    ]
