# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('customer', models.ForeignKey(to='user.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_model',
            field=models.ForeignKey(to='service.TaskModel'),
        ),
        migrations.AddField(
            model_name='task',
            name='tasker',
            field=models.ForeignKey(related_name='tasks', to='user.Tasker'),
        ),
        migrations.AddField(
            model_name='order',
            name='task',
            field=models.ForeignKey(to='service.Task'),
        ),
    ]
