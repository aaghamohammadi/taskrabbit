# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20160131_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='/media/profile_images/profile-image-default.jpg', upload_to='profile_images'),
        ),
    ]
