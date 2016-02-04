# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('review', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='user.Member'),
        ),
        migrations.AddField(
            model_name='rating',
            name='tasker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Member'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user.Member'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='review.CommentSet'),
        ),
    ]