# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_tasker_wage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(null=True, choices=[('M', 'مرد'), ('F', 'زن')], blank=True, max_length=1),
        ),
    ]
