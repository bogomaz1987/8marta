# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import girls.models


class Migration(migrations.Migration):

    dependencies = [
        ('girls', '0007_remove_girls_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='girls',
            name='code',
            field=models.CharField(db_index=True, default='', max_length=3, verbose_name='Уникальный код'),
        ),
    ]