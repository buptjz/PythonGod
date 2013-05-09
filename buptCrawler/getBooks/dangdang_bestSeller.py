# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os,sys,re

sys.path.insert(0, os.path.split(os.path.split(os.getcwd())[0])[0])
sys.path.insert(0, "School/JZCrawler")  

from django.conf import settings
# Set the DJANGO_SETTINGS_MODULE environment variable.   
os.environ['DJANGO_SETTINGS_MODULE'] = "buptCrawler.settings"

import django,time,urllib,urllib2,re
import time
import uuid
import hmac
import hashlib
import simplejson as Json
import socket
import cookielib

from django.db.models.loading import get_models
loaded_models = get_models()
from buptCrawler.getBooks.models  import Book

def getTypeRequest(url):
    headers = {
        '(Request-Line)':'GET /section/1 HTTP/1.1',
        'Host':'bang.dangdang.com',
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        'Referer':'http://bbs.byr.cn/',
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

def zh2unicode(stri): 
    """转换编码到unicode,编码方式从utf-8,gbk,iso-8859-1,big5,ascii中选择.""" 
    encc = ''
    for c in ('ascii', 'utf-8', 'gb2312', 'gbk', 'gb18030', 'big5'): 
	try: 
	    return stri.decode(c)
        except: 
	    pass
    return stri

def downloadUrl(url):
    socket.setdefaulttimeout(20)
    try:
        fp = getTypeRequest(url)
    except:
        print '[failed]when getRequest : ' + url
        return (0,'')
    else:
        try:
            html = fp.read()
        except:
            fp.close()
            print '[failed] when read : ' + url
            return (0,'')
        else:
            print '[success] read url : ' + url
            fp.close()
            return (1,html)

	
def dangdang_bestseller_detail():
    	
    books= Book.objects.all()
    for abook in books:
	success,rawdata=downloadUrl(abook.ddbookurl)
	if not success:
	    #Append the unsuccess url to a unsuccesfulFile
	    #usFilePath ="/Users/wangjz/Desktop/down/usFile.txt"
	    #unsuccessFile = open(usFilePath,"wb")
	    #unsuccessFile.write(url)
	    #unsuccessFile.close()  
	    print('unsuccess with url'+abook.ddbookurl)
	else:
	    data=zh2unicode(rawdata).encode('utf-8')
	    #Use regular expression to find the isbn in the page.
	    patternStarlevel=re.compile(ur"""I S B N\xef\xbc\x9a(.+?)</s""",re.DOTALL)
	    matches=patternStarlevel.findall(data)
	    isbn_number = matches[0]
    
	    #If isbn exists, then create an Book and save it to database
	    #if isbn_number:
		#abook.ISBN = isbn_number
		#try:
		    #abook.save()
		#except Exception,e:
		    #print 'savlindbdis body error---',e
    

	time.sleep(0.5)
#----------------------------------------------------------------------
def dangdang_bestseller():
    
    url="http://bang.dangdang.com/book/bestSeller/?&page="
    page = 17
    while page < 26:
	requestURL = url+str(page)
	page = page+1
	sucess,rawdata = downloadUrl(requestURL)
	patternStarlevel=re.compile(r"""book_pic">.+?<img src="(.+?)"/></a>.+?<li class="bookname blue"><a href="(.+?)".+?>(.+?)</a>.+?class="author">(.+?)</li>.+?<li class="press">(.+?)</li>.+?date">(.+?)</li>.+?pre arial">(.+?)</span>.+?new arial">(.+?)</span>""",re.DOTALL)
	matches=list(patternStarlevel.findall(rawdata))
	booklist=[]
	for i in matches:
	    i=list(i)
	    
	    #dangdang_bestseller_detail(i[1])	    
	    aBook = None         
	    aBook, create = Book.objects.get_or_create(ddbookurl = i[1])
	    if create:
		    try:
			aBook.save()
		    except Exception,e:
			print 'savlindbdis body error---',e
	#Wait for seconds to not be denied
	time.sleep(2)

    
def main():
    print('start crawling!')
    #dangdang_bestseller()
    dangdang_bestseller_detail()

if __name__ =='__main__':
    main()
