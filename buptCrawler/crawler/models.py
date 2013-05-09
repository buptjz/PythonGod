# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.db import models
from djangosphinx.models import SphinxSearch

class IndexDB(models.Model):
    keyword = models.CharField("keyword", max_length=200, null=True)
    docIDs = models.TextField(u"docIDs",null = True)
    category = models.IntegerField(null=True)
    value = models.IntegerField(null=True)
    
class Link(models.Model):
    url = models.URLField("URL", max_length=1000, verify_exists=False)
    title = models.CharField(u"标题",max_length=300,null = True)
    author = models.CharField(u"作者",max_length=200,null = True)
    publishtime = models.CharField(u"发布时间",max_length=60,null = True)
    classification = models.CharField(u"类别",max_length=200,null = True)
    sourcesite = models.CharField(u"来源",max_length=200,null = True)
    content = models.TextField(u"文本内容", null=True)
    addtime = models.DateTimeField(u"添加时间",null = True, auto_now_add=True)
    body = models.TextField(u"html内容", null=True)
    keywords = models.CharField(u"关键字",max_length=500,null=True)
    descriptions = models.CharField(u"描述",max_length=700,null=True)
    mtime = models.CharField(max_length=20,null = True)
    size = models.IntegerField(null=True)  
    
    def __unicode__(self):
        return self.url
    def _repr(self):
        return self.url

