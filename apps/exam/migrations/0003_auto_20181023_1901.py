# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-23 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20181023_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='alias',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='last_name',
        ),
    ]
