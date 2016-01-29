# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=25, verbose_name='عنوان')),
                ('context', models.TextField(verbose_name='متن نظر')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Member')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(default=0, verbose_name='نمره')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='user.Member')),
                ('tasker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Member')),
            ],
            options={
                'verbose_name': 'امتیاز',
                'verbose_name_plural': 'امتیازها',
            },
        ),
    ]
