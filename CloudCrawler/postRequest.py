# -*- coding: utf-8 -*-
#!/usr/bin/env python
#Weather Crawler
import urllib
import urllib2
import BeautifulSoup
import infos
from ExcelWriter import *

filePath = "C:\\Users\\Charles\\Desktop\\2.xls"

def postTypeRequest(url,postData):
    #There is Chinese Character in the post request encode it first
    data = urllib.urlencode(postData)
    
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    page_utf8 = the_page.decode("UTF-8")    
    return page_utf8

def getGeneralData():
    retDic = {}
    qualityList = []
    coreBaddieList = []
    for p in infos.PLACES:
        postdata = {'StationName':p}
        page = postTypeRequest(infos.GetGENERALURL,postdata)
        soup = BeautifulSoup.BeautifulSoup(page)
        
        coreBaddie = str(soup.findAll('span')[4].contents[0]) #首要污染物
        coreBaddieList.append(coreBaddie)
        
        quality = str(soup.findAll('span')[7].contents[0]) #空气质量指数
        if quality == '--':
            pass
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
        postdata = {'StationName':p,'WRWType':category} 
        page = postTypeRequest(infos.GETDETAILURL,postdata)
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
    print(u'【开始】获取 空气质量指数 和 首要污染物 ')
    generalData = getGeneralData()
    print(u'【结束】获取 空气质量指数 和 首要污染物 ')
    print(generalData)
    print(u'……………………………………………………………………………………………………………………')
    
    writeData(fileName,u'空气质量指数',None,generalData['quality'],None)
    writeData(fileName,u'首要污染物',None,generalData['coreBaddie'],None)
    
    for c in infos.ITEMSCHECK:
        print(u'【开始】获取 '+c)
        values,isRealTime = getData(c)
        print(u'【结束】获取 '+c)
        
        if isRealTime:
            s = u'【实时信息】：'
            print(c+s)
            print(values['rt'])
        else:
            s = u'【24均值】'
            print(c+s)
            print(values['24'])
            
        if isRealTime == True:
            writeData(fileName,c,None,values['rt'],isRealTime)
        elif isRealTime == False:
            writeData(fileName,c,None,values['24'],isRealTime)
        print(u'……………………………………………………………………………………………………………………')
