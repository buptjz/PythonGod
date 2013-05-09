# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django,time,urllib,urllib2,re
import time
import uuid
import hmac
import hashlib
import simplejson as Json
import socket
import cookielib

def getTypeRequest(url,host):
    headers = {
        '(Request-Line)':'GET /section/1 HTTP/1.1',
        'Host':host,
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        'Referer':'http://api.douban.com',
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

def downloadUrl(url,host):
    socket.setdefaulttimeout(20)
    try:
        fp = getTypeRequest(url,host)
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