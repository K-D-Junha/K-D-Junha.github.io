# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-09 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='introduction',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='myemail',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='myname',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phonenum',
            field=models.CharField(default='000-000-000', max_length=30),
        ),
    ]
