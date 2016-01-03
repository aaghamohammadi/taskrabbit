# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasker',
            name='availability',
            field=models.ForeignKey(to='user.Availability', blank=True, null=True),
        ),
    ]
