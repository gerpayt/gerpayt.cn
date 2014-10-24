# encoding: utf-8

from django.db import models

from django.conf import settings

class BookTag(models.Model):
    id = models.AutoField(u'标签ID', auto_created=True, serialize=False, primary_key=True)
    title = models.CharField(u"标题", max_length=32)
    link = models.CharField(u"地址", max_length=32, unique=True)
    image = models.ImageField(u"图片", blank=True, upload_to='books/image/tag')
    introduction = models.TextField(u"简介", blank=True)
    add_time = models.DateTimeField(u"添加时间", blank=True, null=True, auto_now_add=True)
    sort = models.IntegerField(u"排序", default=0, null=True)
    other_info = models.TextField(u"其他信息", blank=True, null=True, serialize=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort', '-add_time']

class BookItem(models.Model):
    id = models.AutoField(u'作品ID', auto_created=True, serialize=False, primary_key=True)
    title = models.CharField(u"标题", max_length=120)
    link = models.CharField(u"地址", max_length=120, unique=True)
    tag = models.ManyToManyField(BookTag, verbose_name=u"标签")
    image = models.ImageField(u"缩略图", blank=True, upload_to='books/image/%Y%m')
    file = models.FileField(u"文件", blank=True, upload_to='books/files/%Y%m')
    introduction = models.TextField(u"简介", blank=True, null=True)
    add_time = models.DateTimeField(u"添加时间", blank=True, null=True, auto_now_add=True)
    sort = models.IntegerField(u"排序", default=0, null=True)
    other_info = models.TextField(u"其他信息", blank=True, null=True, serialize=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort', '-add_time']
