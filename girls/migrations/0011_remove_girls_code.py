# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('girls', '0010_girls_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='girls',
            name='code',
        ),
    ]
