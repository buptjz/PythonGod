import urllib2,urllib
import sys
import os
import string
import socket
import cookielib

def getTypeRequest(url):
    headers = {
        '(Request-Line)':'GET /section/1 HTTP/1.1',
        'Host':'api.douban.com',
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


def downloadUrl(id,url,downFolder):
    downFileName = downFolder+'/%d.html'%(id,)
    print 'downloading',url,'as',downFileName
    socket.setdefaulttimeout(2)
    try:
        fp = getTypeRequest(url)
    except:
        print '[failed when getRequest]'
        return 0
    else:
        op = open(downFileName,"wb")
        try:
            html = fp.read()
        except:
            op.close()
            fp.close()
            print '[failed]'
            return 0
        else:
            print '[success]'
            #html.decode('gbk').encode('utf-8')#byr give us gbk,we should convert it to utf-8
            op.write(html)
            op.close()
            fp.close()
            return 1

def spider(url,pages,downFolder):
    
    i = 0
    while i <pages:
        downloadUrl(i+1,url,downFolder)
        i+=1
    print '\nDownload',i,'pages.'
    
    
def main():
    url = 'http://api.douban.com/book/subject/2023011/reviews?start-index=1&max-results=10'
    pages = 1
    downloadFolder = "/Users/wangjz/Desktop/down/comments"
    if not os.path.isdir(downloadFolder):
        os.mkdir(downloadFolder)
    spider(url,pages,downloadFolder)

if __name__ =='__main__':
    main()
