# -*- coding: utf-8 -*-
import os,sys,re
sys.path.insert(0, os.path.split(os.path.split(os.getcwd())[0])[0])
sys.path.insert(0, "School/JZCrawler")  
from django.conf import settings
# Set the DJANGO_SETTINGS_MODULE environment variable.   
os.environ['DJANGO_SETTINGS_MODULE'] = "buptCrawler.settings"

from buptCrawler.crawler.models  import Link,IndexDB

def readKeywords():
	file=open('/School/JZCrawler/buptCrawler/crawler/KeywordsDicOfTheme.txt','r')
        while True:
                line=file.readline()
		if line:
			obj = None 
			word = line.split('\t')[0]
			category = line.split('\t')[1]
			obj, create = IndexDB.objects.get_or_create(keyword =word)
			if create:
				try:
					obj.category = category
					obj.save()
				except Exception,e:
					print 'savlindbdis body error---',e
                else:
                        break
	file.close()


def isSubstring(s1,s2):
	if s1 and s2:
		return s1 in s2
	else:
		return False

def main():
	#readKeywords()
	links = Link.objects.all()
	indexes = IndexDB.objects.all() 
	for index in indexes:
		keyword = index.keyword
		count = 0
		for link in links:
			if isSubstring(keyword,link.content) :
				#index.docIDs = index.docIDs + "\t"+link.id
				allDocIds = []
				if index.docIDs:
					allDocIds = index.docIDs.split(r"+")
				#s="%d"% link.id
				allDocIds.append("%d"% link.id)
				index.docIDs = r"+".join(allDocIds)
				try:
					index.save()
					count = count+1
					print "success",count		
				except Exception,e:	
					print 'savlindbdis body error---',e
	    
if __name__ =='__main__':
	main()
    


