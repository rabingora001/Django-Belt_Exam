# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-24 23:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20181024_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='like',
        ),
    ]