# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-11 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-owner_id']},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='myemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='myname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='myid',
            new_name='owner_id',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='myphone',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='profile',
            name='leaveparty',
            field=models.BooleanField(default=False),
        ),
    ]
