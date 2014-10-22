# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workitem',
            name='image',
            field=models.ImageField(default='', upload_to=b'', verbose_name='\u7f29\u7565\u56fe', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workcate',
            name='introduction',
            field=models.TextField(verbose_name='\u7b80\u4ecb', blank=True),
        ),
    ]
