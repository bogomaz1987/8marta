# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import girls.models


class Migration(migrations.Migration):

    dependencies = [
        ('girls', '0020_auto_20170306_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girls',
            name='code',
            field=models.CharField(db_index=True, default=girls.models.get_unique_code, max_length=3, verbose_name='Уникальный код'),
        ),
    ]
