# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girls', '0012_girls_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girls',
            name='code',
            field=models.CharField(db_index=True, default='zmj', max_length=3, verbose_name='Уникальный код'),
        ),
    ]
