# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_booktag_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='file',
            field=models.FileField(upload_to=b'', verbose_name='\u6587\u4ef6', blank=True),
        ),
    ]
