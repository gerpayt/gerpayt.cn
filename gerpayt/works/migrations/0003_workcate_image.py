# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_auto_20141020_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='workcate',
            name='image',
            field=models.ImageField(default='', upload_to=b'', verbose_name='\u56fe\u7247', blank=True),
            preserve_default=False,
        ),
    ]
