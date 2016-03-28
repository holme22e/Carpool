# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-25 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0004_auto_20160229_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='user_type',
            field=models.CharField(default='Driver', max_length=10),
        ),
        migrations.AddField(
            model_name='rider',
            name='user_type',
            field=models.CharField(default='Rider', max_length=10),
        ),
    ]
