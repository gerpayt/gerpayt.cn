# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkCate',
            fields=[
                ('id', models.AutoField(verbose_name='\u5206\u7c7bID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='\u6807\u9898')),
                ('link', models.CharField(unique=True, max_length=16, verbose_name='\u5730\u5740')),
                ('introduction', models.TextField(null=True, verbose_name='\u7b80\u4ecb', blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4', null=True)),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='\u6392\u5e8f')),
                ('other_info', models.TextField(null=True, verbose_name='\u5176\u4ed6\u4fe1\u606f', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkItem',
            fields=[
                ('id', models.AutoField(verbose_name='\u4f5c\u54c1ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='\u6807\u9898')),
                ('link', models.CharField(unique=True, max_length=16, verbose_name='\u5730\u5740')),
                ('introduction', models.TextField(null=True, verbose_name='\u7b80\u4ecb', blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4', null=True)),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='\u6392\u5e8f')),
                ('other_info', models.TextField(null=True, verbose_name='\u5176\u4ed6\u4fe1\u606f', blank=True)),
                ('category', models.ForeignKey(verbose_name='\u5206\u7c7b', to='works.WorkCate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
