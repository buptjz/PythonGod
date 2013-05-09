# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os,sys,re

sys.path.insert(0, os.path.split(os.path.split(os.getcwd())[0])[0])
sys.path.insert(0, "School/JZCrawler")  

from django.conf import settings
# Set the DJANGO_SETTINGS_MODULE environment variable.   
os.environ['DJANGO_SETTINGS_MODULE'] = "buptCrawler.settings"

from Tools import PriorityQueue,Parser,ParserForBKEmploy

import urllib2,urllib
import sys
import os
import string
import socket
import cookielib
import time
import datetime

from django.db.models.loading import get_models
loaded_models = get_models()
from buptCrawler.crawler.models  import Link as dblink

from stripogram import html2text, html2safehtml


def zh2unicode2(stri): 
    """转换编码到unicode,
    编码方式从utf-8,gbk,iso-8859-1,big5,ascii中选择.""" 
    for c in ('ascii', 'utf-8', 'gb2312', 'gbk', 'gb18030', 'big5'): 
	flag = 0
        try: 
	    decodeString = stri.decode(c)
	    flag = 1
            return decodeString
        except: 
            pass 
    if flag == 0:
	stri.decode("gbk","ignore")
	return stri



def getTypeRequest(url):
    headers = {
        #'(Request-Line)':'GET /section/1 HTTP/1.1',
        'Host':'zsb.bupt.edu.cn',
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        #'Referer':'http://bbs.byr.cn/',
        'application/json':'text/javascript, */*; q=0.01',
        'Connection':'keep-alive',
        'X-Requested-With':'XMLHttpRequest',
    }

    req = urllib2.Request(
        url = url,
        headers = headers
    )
    result = urllib2.urlopen(req)
    return result
                
def updatePriQueue(priQueue,url,beginurl):
    #if (url.find(r"BYR_Bulletin")) == -1:
    if (url.find(r"BKemploy")) == -1:
	return
    isAraticle = True
    if (url.find(r"article")) == -1:
	isAraticle = False
    extraPrior = isAraticle  and 50 or 0
    extraBeginUrl = beginurl in url and 5 or 0
    extraLevel = string.find(url,'/')#
    schemeType = ['http://','ftp://','file://']
    flag = 0
    for type in schemeType:
        if url.startswith(type):
            flag = 1
    if not flag:
        return
    item = priQueue.getitem(url)
    if item:
        newitem = (item[0]+1+extraPrior+extraBeginUrl-extraLevel,item[1])
        priQueue.remove(item)
        priQueue.push(newitem)
    else:
        priQueue.push((1+extraPrior+extraBeginUrl-extraLevel,url))


def analyseHtml(url,html,priQueue,downlist,beginurl):
    p = ParserForBKEmploy(html,url)
    for v in p.links:#p.links = ['http://bbs.byr.cn/board/Job?p=2', 'http://bbs.byr.cn/board/Job?p=3',.........]
        if not downlist.count(v):
            updatePriQueue(priQueue,v,beginurl)

def downloadUrl(id,url,priQueue,downlist,beginurl):
    print 'downloading---' +url
    try:
        responseResult = getTypeRequest(url)#byrForumRequest(url)
    except:
        print '[failed]'
        return 0
    else:
        downlist.push(url)
        try:
            status = responseResult.code
        except:
            pass
        try:
            mimetype=responseResult.headers['Content-type'].split(';')[0]  #to do
        except:
            mimetype = None
            pass
        try:
            mtime = time.mktime(responseResult.headers['Last-Modified']) # to do 
        except:
            mtime = None
            pass        
        try:
            size = int(responseResult.headers['Content-Length']) #to do
        except:
            size = None
            pass
        try:
            htmlbody = responseResult.read()
	    #print "htmlbody ====="+htmlbody.decode("gb2312").encode("utf-8")
        except:
            responseResult.close()
            print '[failed]'
            return 0
        else:
	    responseResult.close()
            print '[success]'

	    htmlbody = zh2unicode2(htmlbody)
	    try:
		htmlbody = htmlbody.encode('utf-8')#byr give us gbk,we should convert it to utf-8
	    except:
		pass
	    bodypattern=re.compile(ur'''id="articleTitle".+?colspan="2" >(.+?)</td>.+?\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4\xef\xbc\x9a(.+?)\xe3\x80\x91</td>\r.+?id="zpxx1">\r\n(.+?)<!---''',re.DOTALL)
	    contentMatch=bodypattern.findall(htmlbody)
	    for aContentMatch in contentMatch:
		obj = None         
		obj, create = dblink.objects.get_or_create(url = url)
		if create:
		    obj.author = "招生办"
		    obj.publishtime = aContentMatch[1]
		    obj.title = aContentMatch[0]
		    obj.classification  ='本科招生'
		    obj.sourcesite = "BKemploy"
		    obj.content  =aContentMatch[2]
		    obj.mtime = mtime
		    obj.size = size
		    obj.status = status
		    obj.addtime = datetime.datetime.now()   
		    obj.body = htmlbody
		    try:
			obj.save()
		    except Exception,e:
			print 'savlindbdis body error---',e
            analyseHtml(url,htmlbody,priQueue,downlist,beginurl)
        return 1

def spider(beginurl,pages):
    priQueue = PriorityQueue()              #保存待下载url的链接 
    downlist = PriorityQueue()              #已下载url集合，防止重复下载
    priQueue.push((1,beginurl))
    i = 0
    while not priQueue.empty() and i <pages:
        k,url = priQueue.pop()
        if downloadUrl(i+1,url,priQueue,downlist,beginurl):
            i+=1
    print '\nDownload',i,'pages.'
    
    
def main():
    #beginurl = 'http://buptoa.bupt.edu.cn/broad.nsf/($All)?OpenView'#初始的url地址
    #beginurl = "http://bbs.byr.cn/board/BYR_Bulletin"
    #beginurl = "http://bbs.byr.cn/board/Recommend"
    beginurl = "http://zsb.bupt.edu.cn/BKemployNews.php"
    pages = 5000      #抓取网页的数目
    socket.setdefaulttimeout(5)
    spider(beginurl,pages)

if __name__ =='__main__':
    main()
