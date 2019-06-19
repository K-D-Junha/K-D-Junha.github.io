# Generated by Django 2.2.1 on 2019-06-18 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0010_remove_profile_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Member.Profile'),
        ),
    ]
