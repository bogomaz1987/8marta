# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girls', '0002_auto_20170303_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='gifts',
            name='description',
            field=models.CharField(default='', max_length=250, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='girls',
            name='code',
            field=models.CharField(db_index=True, default='xef', max_length=3, verbose_name='Уникальный код'),
        ),
    ]
