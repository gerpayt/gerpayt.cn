# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20141023_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='link',
            field=models.CharField(unique=True, max_length=64, verbose_name='\u5730\u5740'),
        ),
    ]
