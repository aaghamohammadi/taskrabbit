# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20160131_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]
