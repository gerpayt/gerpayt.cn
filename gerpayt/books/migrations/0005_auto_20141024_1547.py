# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20141023_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='file',
            field=models.FileField(upload_to=b'books/files/%Y%m', verbose_name='\u6587\u4ef6', blank=True),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='image',
            field=models.ImageField(upload_to=b'books/image/%Y%m', verbose_name='\u7f29\u7565\u56fe', blank=True),
        ),
        migrations.AlterField(
            model_name='booktag',
            name='image',
            field=models.ImageField(upload_to=b'books/image/tag', verbose_name='\u56fe\u7247', blank=True),
        ),
    ]
