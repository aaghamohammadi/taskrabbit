# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_taskmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
