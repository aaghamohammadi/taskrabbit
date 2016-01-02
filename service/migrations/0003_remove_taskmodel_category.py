# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20160102_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='category',
        ),
    ]
