# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 08:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=64, verbose_name='Организация')),
                ('region', models.CharField(blank=True, max_length=32, verbose_name='Регион')),
                ('site', models.CharField(blank=True, max_length=64, verbose_name='Сайт')),
                ('position', models.CharField(max_length=64, verbose_name='Должность')),
                ('duties', models.TextField(verbose_name='Обязанности')),
                ('start', models.DateField(verbose_name='Начало')),
                ('end', models.DateField(default=datetime.date(2017, 7, 31), verbose_name='Конец')),
            ],
        ),
    ]
