# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-07 03:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_auto_20190107_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='realnames',
            new_name='realname',
        ),
    ]
