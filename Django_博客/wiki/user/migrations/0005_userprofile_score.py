# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-11 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userprofile_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='score',
            field=models.IntegerField(default=0, null=True, verbose_name='分数'),
        ),
    ]
