# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20160129_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='comment_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='review.CommentSet', unique=True),
        ),
    ]
