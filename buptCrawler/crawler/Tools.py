import bisect
import string
import re

class PriorityQueue(list):
    def __init__(self):
        list.__init__(self)
        self.map = {}

    def push(self,item):
        if self.count(item) == 0:
            bisect.insort(self,item)#insert and sort
            self.map[item[1]] = item

    def pop(self):
        r = list.pop(self)#(1, 'http://bbs.byr.cn/board/Job')
        del self.map[r[1]]#r[1]="http://bbs.byr.cn/board/Job"
        return r

    def getitem(self,url):
        if self.map.has_key(url):
            return self.map[url]
        else:
            return None

    def empty(self):
        return len(self) == 0

    def remove(self,item):
        list.remove(self,item)
        del self.map[item[1]]
        
    #Binary search
    def count(self,item):
        if len(self) == 0:
            return 0
        left = 0
        right = len(self)-1
        mid = -1
        while left<=right:
            mid = (left+right)/2
            if self[mid] < item:
                left = mid+1
            elif self[mid] >item:
                right= mid-1
            else:
                break
        return self[mid] == item and 1 or 0
        
        

class Parser():
    def __init__(self,html):
        self.links = []
        re_pattern = "\shref=[\"']?([^\"'\s>]+)[\"'\s>]"
        re_href = re.compile(re_pattern,re.IGNORECASE)
        for m in re_href.finditer(html):
            href = m.group(1)
            location = href.find("user")
            if location == -1:
                #href = "http://bbs.byr.cn" + href#BYRbbs only gives the relative path href,so..
                href = "http://buptoa.bupt.edu.cn" + href
                #href = "http://zsb.bupt.edu.cn/" + href
                self.links.append(href)
                
class ParserForBKEmploy():#for the javascript reason
    def __init__(self,html,url):
        self.links = []
        re_pattern = "\shref=[\"']?([^\"'\s>]+)[\"'\s>]"
        re_href = re.compile(re_pattern,re.IGNORECASE)
        for m in re_href.finditer(html):
            href = m.group(1)
            location = href.find("user")
            if location == -1:
                #href = "http://bbs.byr.cn" + href#BYRbbs only gives the relative path href,so..
                #href = "http://buptoa.bupt.edu.cn" + href
                href = "http://zsb.bupt.edu.cn/" + href
                self.links.append(href)
                
         # location.href='?page=2'"      
        re_patternSecond = "location.href=\'(.+?)\'"
        re_hrefSecond  = re.compile(re_patternSecond,re.IGNORECASE)
        for m in re_hrefSecond.finditer(html):
            href = m.group(1)
            urls = url.split("?")
            href = urls[0]+ href
            self.links.append(href)


    
