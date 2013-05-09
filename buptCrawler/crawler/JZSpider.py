from Tools import PriorityQueue,Parser
import urllib2,urllib
import sys
import os
import string
import socket
import cookielib


def signIn():
    #cookie
    cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    postdata=urllib.urlencode({
        'id':'wtv888',
        'passwd':'wjz000',
        'CookieDate':'2',
    })
    
    headers = {
        '(Request-Line)':'POST /user/ajax_login.json HTTP/1.1',
        'Host':'bbs.byr.cn',
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        'Referer':'http://bbs.byr.cn/',
        'application/json':'text/javascript, */*; q=0.01',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With':'XMLHttpRequest',
        'Content-Length':'36'
    }
    
    req = urllib2.Request(
        url = 'http://bbs.byr.cn/user/ajax_login.json',
        data = postdata,
        headers = headers
    )
    result = urllib2.urlopen(req).read()
    result = result.decode('gbk').encode('utf-8')
    
    
def getTypeRequest(url):
    headers = {
        #'(Request-Line)':'GET /section/1 HTTP/1.1',
        '(Request-Line)':'GET /broad.nsf/e28ed69f46b9e7ff482567b4002a2622/362f5987428b8ae5482579b80003bf6e?OpenDocument HTTP/1.1',
        'Host':'bbs.byr.cn',
        #'Host':'buptoa.bupt.edu.cn',
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
def buptOARequest(url):
    headers = {
        '(Request-Line)':'GET /section/1 HTTP/1.1',
        'Host':'buptoa.bupt.edu.cn',
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        'Referer':'http://bbs.byr.cn/',
        'application/json':'text/javascript, */*; q=0.01',
        'Connection':'keep-alive',
    }

    req = urllib2.Request(
        url = url,
        headers = headers
    )
    result = urllib2.urlopen(req)
    return result


def updatePriQueue(priQueue,url,beginurl):
    extraPrior = url.endswith('.html') and 20 or 0
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
    p = Parser(html)
    for v in p.links:#p.links = ['http://bbs.byr.cn/board/Job?p=2', 'http://bbs.byr.cn/board/Job?p=3',.........]
        if not downlist.count(v):
            updatePriQueue(priQueue,v,beginurl)

def downloadUrl(id,url,priQueue,downlist,downFolder,beginurl):
    downFileName = downFolder+'/%d.html'%(id,)
    print 'downloading',url,'as',downFileName
    
    socket.setdefaulttimeout(2)
    try:
        #fp = urllib2.urlopen(url)
        #fp = buptOARequest(url)
        fp = getTypeRequest(url)
    except:
        print '[failed]'
        return 0
    else:
        downlist.push(url)
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

            analyseHtml(url,html,priQueue,downlist,beginurl)
            return 1

def spider(beginurl,pages,downFolder):
    priQueue = PriorityQueue()              #保存待下载url的链接 
    downlist = PriorityQueue()              #已下载url集合，防止重复下载
    priQueue.push((1,beginurl))
    i = 0
    while not priQueue.empty() and i <pages:
        k,url = priQueue.pop()
        if downloadUrl(i+1,url,priQueue,downlist,downFolder,beginurl):
            i+=1
    print '\nDownload',i,'pages.'
def main():
    #beginurl = sys.argv[1]                  #初始的url地址
    #pages = string.atoi(sys.argv[2])        #抓取网页的数目
    #downloadFolder = sys.argv[3]            #指定保存网页的文件夹
    #beginurl = "http://www.baidu.com/"
    #beginurl = 'http://bbs.byr.cn/board/CPP'
    beginurl = 'http://buptoa.bupt.edu.cn/'
    pages = 3000
    downloadFolder = "/Users/wangjz/Desktop/down/buptoa"
    if not os.path.isdir(downloadFolder):
        os.mkdir(downloadFolder)

    #signIn()
    spider(beginurl,pages,downloadFolder)

if __name__ =='__main__':
    main()
