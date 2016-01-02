# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='description',
            field=models.CharField(max_length=50, default='salam bar hamegan '),
            preserve_default=False,
        ),
    ]
