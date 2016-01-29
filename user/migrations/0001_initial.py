# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 17:06
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('M', 'مرد'), ('F', 'زن')], default='M', max_length=1, null=True)),
                ('city', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=150)),
                ('image', models.ImageField(default='/static/images/user/profile-image-default.jpg', upload_to='profile_images')),
                ('activation_key', models.CharField(blank=True, max_length=40)),
                ('key_expires', models.DateTimeField(default=datetime.date.today)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'کاربر نوع مشتری',
                'verbose_name_plural': 'کاربران نوع مشتری',
            },
        ),
    ]
