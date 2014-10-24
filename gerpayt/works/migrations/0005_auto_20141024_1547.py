# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_auto_20141023_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workcate',
            name='image',
            field=models.ImageField(upload_to=b'works', verbose_name='\u56fe\u7247', blank=True),
        ),
        migrations.AlterField(
            model_name='workitem',
            name='image',
            field=models.ImageField(upload_to=b'works', verbose_name='\u7f29\u7565\u56fe', blank=True),
        ),
    ]
