# -*- coding: utf-8 -*-
from django.db import models

class Book(models.Model):
	id = models.AutoField(primary_key=True)
	ISBN = models.CharField("ISBN号",max_length=30)
	bookname = models.CharField("书名",max_length=300)
	ddbookurl= models.CharField("当当网该书网址",max_length=100)
	
	author = models.CharField("作者",max_length=50)
	publisher = models.CharField("出版社",max_length=50)
	bookclass = models.CharField("图书所属类别",max_length=100)
	contentinfo = models.CharField("内容简介",max_length=1500)
	publishtime = models.CharField("出版时间",max_length=20)
	publishnumber = models.CharField("版次",max_length=20)
	pagenumber = models.CharField("页数",max_length=10)
	facetype= models.CharField("装帧",max_length=20)
	pagesize = models.CharField("开本",max_length=10)
	imageurl = models.CharField("封面图片链接",max_length=200)
	price= models.CharField("定价",max_length=20)
	ddprice= models.CharField("当当价",max_length=20)
	
	tags= models.CharField("标签",max_length=100)
	rating= models.CharField("得分",max_length=30)

	authorinfo= models.CharField("作者简介",max_length=1000)
	addtime = models.DateTimeField("信息添加时间",auto_now=True)
	
	def __unicode__(self):
		return self.name
	def _repr(self):
		return self.name
