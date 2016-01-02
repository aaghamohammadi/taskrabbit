# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20160102_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('customer', models.ForeignKey(to='user.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='service_images/')),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='task_model',
            field=models.ForeignKey(to='service.TaskModel'),
        ),
        migrations.AddField(
            model_name='skill',
            name='tasker',
            field=models.ForeignKey(to='user.Tasker', related_name='tasks'),
        ),
        migrations.AddField(
            model_name='order',
            name='skill',
            field=models.ForeignKey(to='service.Skill'),
        ),
    ]
