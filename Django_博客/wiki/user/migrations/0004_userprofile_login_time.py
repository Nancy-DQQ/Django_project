# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-06 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userprofile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='login_time',
            field=models.DateTimeField(default='2019-10-10 10:10:10', null=True, verbose_name='登录时间'),
        ),
    ]
