# encoding: utf-8

import os, sys

from django.db import models

from django.conf import settings

class WorkCate(models.Model):
    id = models.AutoField(u'分类ID', auto_created=True, serialize=False, primary_key=True)
    title = models.CharField(u"标题", max_length=64)
    link = models.CharField(u"地址", max_length=16, unique=True)
    image = models.ImageField(u"图片", blank=True, upload_to='works')
    introduction = models.TextField(u"简介", blank=True)
    add_time = models.DateTimeField(u"添加时间", blank=True, null=True, auto_now_add=True)
    sort = models.IntegerField(u"排序", default=0, null=True)
    other_info = models.TextField(u"其他信息", blank=True, null=True, serialize=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort', '-add_time']


class WorkItem(models.Model):
    id = models.AutoField(u'作品ID', auto_created=True, serialize=False, primary_key=True)
    title = models.CharField(u"标题", max_length=64)
    link = models.CharField(u"地址", max_length=16, unique=True)
    category = models.ForeignKey(WorkCate, verbose_name=u"分类")
    image = models.ImageField(u"缩略图", blank=True, upload_to='works')
    introduction = models.TextField(u"简介", blank=True, null=True)
    add_time = models.DateTimeField(u"添加时间", blank=True, null=True, auto_now_add=True)
    sort = models.IntegerField(u"排序", default=0, null=True)
    other_info = models.TextField(u"其他信息", blank=True, null=True, serialize=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort', '-add_time']
