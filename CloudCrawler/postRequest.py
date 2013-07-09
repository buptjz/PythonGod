# -*- coding: utf-8 -*-
#!/usr/bin/env python
#Weather Crawler
import urllib
import urllib2
import BeautifulSoup
import infos
import time
from ExcelWriter import *

def postTypeRequest(url,postData):
    #There is Chinese Character in the post request encode it first
    time.sleep(1)
    try:
        data = urllib.urlencode(postData)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()
        page_utf8 = the_page.decode("UTF-8")
    except:
        print(u'网络访问出现问题，请稍后重试')
        return False
    return page_utf8

def getGeneralData():
    retDic = {}
    qualityList = []
    coreBaddieList = []
    for p in infos.PLACES:
        if p == infos.PLACES[len(infos.PLACES)-1]:
            print u'【获取】',
            print unicode(p, "utf-8")
        else:
            print u'【获取】',
            print unicode(p, "utf-8"),
        
        postdata = {'StationName':p}
        page = postTypeRequest(infos.GetGENERALURL,postdata)
        if page == False:
            coreBaddie = 'Err'
            quality = 'Err'
            #return False
        else:
            soup = BeautifulSoup.BeautifulSoup(page)
            coreBaddie = str(soup.findAll('span')[4].contents[0]) #首要污染物
            quality = str(soup.findAll('span')[7].contents[0]) #空气质量指数
        
        coreBaddieList.append(coreBaddie)
        qualityList.append(quality)
        
    retDic = {'quality':qualityList,'coreBaddie':coreBaddieList}
    return retDic

def getData(category):
    realtimeDensity = False
    NullValuePlace = 0
    valuesDic = {}
    rtList = []
    avg24List = []
    for p in infos.PLACES:
        
        if p == infos.PLACES[len(infos.PLACES)-1]:
            print u'【获取】',
            print unicode(p, "utf-8")
        else:
            print u'【获取】',
            print unicode(p, "utf-8"),
            
        postdata = {'StationName':p,'WRWType':category} 
        page = postTypeRequest(infos.GETDETAILURL,postdata)
        if page == False:
            rtDensity = 'Err'
            density24 = 'Err'
            #return False,False
        else:
            soup = BeautifulSoup.BeautifulSoup(page)
            rtDensity = str(soup.findAll('span')[2].contents[0]) #real time浓度
            #'\r\n               6\r\n                   '这类不纯
            rtDensity = rtDensity.split()[0]
            density24 = str(soup.findAll('span')[7].contents[0]) #24浓度
        rtList.append(rtDensity)
        avg24List.append(density24)
        
        if density24 == '--':
            NullValuePlace += 1

    if NullValuePlace >= 12:
        realtimeDensity = True
        pass #use the realtimedensity
    else:
        realtimeDensity = False
        pass #use 24h average
    
    valuesDic = {'24':avg24List,'rt':rtList}
    return valuesDic,realtimeDensity
        
def runMainFunc(fileName): 
    allData = []
    print(u'【开始】获取 空气质量指数 和 首要污染物 ')
    generalData = getGeneralData()
    if generalData == False:
        hold = input()
        return False
    print(u'【结束】获取 空气质量指数 和 首要污染物 ')
    print(generalData)
    print(u'……………………………………………………………………………………………………………………')

    allData.append({'shName':u'空气质量指数','col':None,'data':generalData['quality'],'isReal':None})
    allData.append({'shName':u'首要污染物','col':None,'data':generalData['coreBaddie'],'isReal':None})

    for c in infos.ITEMSCHECK:
        print(u'【开始】获取 '+c)
        values,isRealTime = getData(c)
        if values == False:
            hold = input()
            return False
        
        print(u'【结束】获取 '+c)
        
        if isRealTime:
            s = u'【实时信息】：'
            print(c+s)
            print(values['rt'])
            allData.append({'shName':c,'col':None,'data':values['rt'],'isReal':isRealTime})
        else:
            s = u'【24均值】'
            print(c+s)
            print(values['24'])
            allData.append({'shName':c,'col':None,'data':values['24'],'isReal':isRealTime})
        print(u'……………………………………………………………………………………………………………………')
    
    currentTime = time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(time.time()))
    print(u'写入Excel表格')
    
    #写入表格
    for w in allData:
        writer = writeData(fileName,w['shName'],w['col'],w['data'],w['isReal'])
        if writer == False:
            hold = input()
            return False
    
    print(u'获取当日信息结完成')
    print(currentTime)
    hold = input()