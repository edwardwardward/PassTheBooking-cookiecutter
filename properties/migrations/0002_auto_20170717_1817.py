# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='no_of_bedrooms',
        ),
        migrations.AddField(
            model_name='property',
            name='no_of_bedroom',
            field=models.IntegerField(default=0),
        ),
    ]
