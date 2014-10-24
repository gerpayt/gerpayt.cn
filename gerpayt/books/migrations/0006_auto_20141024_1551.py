# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20141024_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='link',
            field=models.CharField(unique=True, max_length=120, verbose_name='\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='title',
            field=models.CharField(max_length=120, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='booktag',
            name='title',
            field=models.CharField(max_length=16, verbose_name='\u6807\u9898'),
        ),
    ]
