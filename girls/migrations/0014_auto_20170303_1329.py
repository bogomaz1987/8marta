# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girls', '0013_auto_20170303_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girls',
            name='code',
            field=models.CharField(db_index=True, default='cqb', max_length=3, verbose_name='Уникальный код'),
        ),
    ]
