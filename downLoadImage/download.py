#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Multi thread 
import os
import hashlib
import threading
import Queue
import urllib2
import socket 

queue = Queue.Queue()
prefixUrl = "http://gallery.photo.net/photo/"
suffixUrl = "-md.jpg"
errorImageList = []
count = []

class MutilThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        #按照顺序执行，先put所有的的queue然后再逐步处理；
        #while queue.qsize() != 0:
        while True:
            imageID = self.queue.get()
            #size = queue.qsize()
            #print "Thread's Size: %s" % size
            getImageFromWeb(imageID)
            self.queue.task_done()

def DownloadImage():
    name = "/home/wangjz/Desktop/photonet_dataset.txt"
    url_li = getImageUrls(name)
    #先将所有的item，put到queue;
    for i in range(4):
        t = MutilThread(queue)
        t.setDaemon(True)
        t.start()
    for imageID in url_li:
        queue.put(imageID)
        queue.join()

def getImageFromWeb(imageID):
    count.append("")
    print("Current download count is ---------" + str(len(count)))
    url = prefixUrl+imageID+suffixUrl
    print(url)
    socket.setdefaulttimeout(60)
    try:
        openURL = urllib2.urlopen(url)
        data = openURL.read()
        dirname = "/home/wangjz/Desktop/image/"
        path = dirname+imageID+".jpg"
        with open(path, "wb") as jpg:
            jpg.write(data)
        openURL.close()
    except Exception as e:
        print e
        print "Happens when download Image : "+ imageID
        errorImageList.append(imageID) 

def getImageUrls(fileName):
    urlsList= []
    dataSet = open(fileName)
    lines = dataSet.readlines();
    for line in lines:
        imageID = line.split()[1]
        urlsList.append(imageID)
    return urlsList

def main():
    DownloadImage()
    errorFile = "/home/wangjz/Desktop/errorImages.txt"
    ef = open(errorFile,'w')
    ef.writelines(errorImageList)
    ef.close()
    #a = getImageUrls(name)
    #print(a)
    
if __name__=='__main__':
    main()