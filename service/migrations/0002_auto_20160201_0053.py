# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 00:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.AddField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 0, 53, 47, 72239)),
            preserve_default=False,
        ),
    ]
