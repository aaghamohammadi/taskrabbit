# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20160128_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(default='/static/images/profile-image-default.jpg', upload_to='profile_images'),
        ),
    ]