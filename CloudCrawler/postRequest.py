# -*- coding: utf-8 -*-
#!/usr/bin/env python
#Cloud Crawler
import urllib
import urllib2

places = {'南三环','永乐店','八达岭','怀柔'}
categories = {'NO2','PM2.5','PM10'}
url = 'http://zx.bjmemc.com.cn/ashx/Data.ashx?Action=GetWRWInfo_ByStationAndWRWType'

for p in places:
    for c in categories:
        postdata = {'StationName':p,'WRWType':c}
        data = urllib.urlencode(postdata)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()
        
        f=open("/Users/wangjz/Desktop/test/"+p+c+".txt","w")        
        f.write(the_page)
        f.close()
        #print the_page