# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girls', '0014_auto_20170303_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishes',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Вручено'),
        ),
        migrations.AlterField(
            model_name='girls',
            name='code',
            field=models.CharField(db_index=True, default='ron', max_length=3, verbose_name='Уникальный код'),
        ),
    ]
