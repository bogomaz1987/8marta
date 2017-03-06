# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-02 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Girls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=250)),
                ('flour', models.SmallIntegerField()),
                ('code', models.CharField(default='tgs', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girls.Gifts')),
                ('girl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girls.Girls')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='wish',
            unique_together=set([('girl', 'gift')]),
        ),
    ]