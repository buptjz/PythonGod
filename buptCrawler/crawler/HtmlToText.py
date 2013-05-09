# -*- coding: utf-8 -*-

import os,sys,re

sys.path.insert(0, os.path.split(os.path.split(os.getcwd())[0])[0])
sys.path.insert(0, "School/JZCrawler")  
from django.conf import settings
# Set the DJANGO_SETTINGS_MODULE environment variable.   
os.environ['DJANGO_SETTINGS_MODULE'] = "buptCrawler.settings"

from buptCrawler.crawler.models  import Link
from HTMLParser import HTMLParser


def cutSpace(string):
    space = "&nbsp;"
    return string.replace(space," ")
    
def strip_tags(html):
    html = html.strip()
    html = html.strip("\n")
    result = []
    parse = HTMLParser()
    parse.handle_data = result.append
    parse.feed(html)
    parse.close()
    return "".join(result)
def strpTime():
    links = Link.objects.all()
    i = 0
    for link in links:
	#try:
	    #stripedtime = strip_tags(link.publishtime)
	    #link.publishtime = stripedtime
	#except:
	    #pass
	time = link.publishtime
	if time:
	    stripTime = cutSpace(link.publishtime)
	    link.publishtime = stripTime
	    try:
		link.save()
		i = i+1
		print "success",i
	    except Exception,e:
		print 'savlindbdis body error---',e
		
def formatTimeBuptOA():
    transTo11 = ['12','11','10','09','08','07','06']
    transTo12 = ['01','02','03','04','05']
    links = Link.objects.all()
    i = 0
    for link in links:
	time = link.publishtime
	if time:
	    i+=1
	    time = time.split('-')[0]
	    if time in transTo11:
		formatTime = '2011-%s' %(link.publishtime)
		link.publishtime = formatTime
		try:
		    link.save()
		    print link.publishtime 
		except Exception,e:
		    print 'error',e
		    
	    elif time in transTo12:
		formatTime = '2012-%s' %(link.publishtime)
		link.publishtime = formatTime
		try:
		    link.save()
		    print link.publishtime 
		except Exception,e:
		    print 'error',e
		    
	    else:
		print '%s  unknown  %s' %(time,i)
		    
def dealTimeBuptOA():
    links = Link.objects.all()
    i = 0
    for link in links:
	time = link.publishtime
	number = link.id
	if number<=4905 and number>=4278 and time:
	    i+=1
	    #formatTime = time.replace('2011','2010')
	    formatTime = time.replace('2012','2011')
	    link.publishtime = formatTime
	    try:
		link.save()
		print '%s  ~  %s' %(formatTime,i)
	    except Exception,e:
		print 'error',e
	    
from stripogram import html2text, html2safehtml

def htmlToText(original_html):
    #clean_html = html2safehtml(original_html,valid_tags=("b", "a", "i", "br", "p"))
    # Don't process <img> tags, just strip them out. Use an indent of 4 spaces 
    # and a page that's 80 characters wide.
    text = html2text(original_html,ignore_tags=("img",),indent_width=4,page_width=80)
    #text = html2text(original_html)
    return text	    

def strpTitle():
    links = Link.objects.all()
    i = 0
    for link in links:
	number = link.id
	if number>=8459:
	    title = link.title
	    if title:
		stripTitle = htmlToText(title)
		link.descriptions = stripTitle
		try:
		    link.save()
		    i = i+1
		    print "success",i
		except Exception,e:
		    print 'savlindbdis body error---',e

def changeSource():
    links = Link.objects.all()
    i = 0
    for link in links:
	source = link.sourcesite
	if source:
	    changedSource = source.replace('buptOA','a_buptOA')
	    link.keywords = changedSource
	    try:
		link.save()
		i = i+1
		print "success",i
	    except Exception,e:
		print 'savlindbdis body error---',e
		
def main():
    changeSource()
    #strpTime()
    #formatTimeBuptOA()
    #dealTimeBuptOA()
    #strpTitle()
    #2269 3991
	    
if __name__ =='__main__':
    main()
    


