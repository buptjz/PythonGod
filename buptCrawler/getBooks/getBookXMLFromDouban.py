# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os,sys,re
sys.path.insert(0, os.path.split(os.path.split(os.getcwd())[0])[0])
sys.path.insert(0, "School/JZCrawler")  
from django.conf import settings
# Set the DJANGO_SETTINGS_MODULE environment variable.   
os.environ['DJANGO_SETTINGS_MODULE'] = "buptCrawler.settings"
from django.db.models.loading import get_models
loaded_models = get_models()
from buptCrawler.getBooks.models  import Book
import utility,time

def doubanBookComments():
    comentsUrlStart = "http://api.douban.com/book/subject/isbn/"
    comentsUrlEnd = "/reviews?start-index=1&max-results=20"
    commentsFilePath = "/Users/wangjz/Desktop/down/comments/"
    usCommentsFile ="/Users/wangjz/Desktop/down/usCommentsFile.txt"
    apikey="&apikey=0ff0dcf23a3d64d02fd296d6aeb82e70"
    books= Book.objects.all()
    
    for abook in books:
	if len(abook.ISBN) > 9:
	    print("bookISBN: "+ abook.ISBN)
	    success,rawdata=utility.downloadUrl(comentsUrlStart+abook.ISBN+comentsUrlEnd+apikey,'api.douban.com')
	    
	    if not success:
		#Append the unsuccess url to a unsuccesfulFile
		ucf = open(usCommentsFile,"w+")
		ucf.write(abook.ISBN)
		ucf.close()  
	    else:
		data=utility.zh2unicode(rawdata).encode('utf-8')
		#Use regular expression to find the isbn in the page.
		fileName = commentsFilePath+"COMMENTS_ISBN_"+abook.ISBN+".XML"
		commentxml = open(fileName,"w")
		commentxml.write(data)
		commentxml.close()
		
	    time.sleep(2)

def doubanBookXML():
    doubanXML_URL = "http://api.douban.com/book/subject/isbn/"
    xmlFilePath = "/Users/wangjz/Desktop/down/books_xml/"
    usFilePath ="/Users/wangjz/Desktop/down/usFile.txt"
    apikey="?apikey=0ff0dcf23a3d64d02fd296d6aeb82e70"
    books= Book.objects.all()
    
    for abook in books:
	if len(abook.ISBN) > 9:
	    print("bookISBN: "+ abook.ISBN)
	    success,rawdata=utility.downloadUrl(doubanXML_URL+abook.ISBN+apikey,'api.douban.com')
	    
	    if not success:
		#Append the unsuccess url to a unsuccesfulFile
		unsuccessFile = open(usFilePath,"w+")
		unsuccessFile.write(abook.ISBN)
		unsuccessFile.close()  
	    else:
		data=utility.zh2unicode(rawdata).encode('utf-8')
		#Use regular expression to find the isbn in the page.
		fileName = xmlFilePath+"BOOKINFO_ISBN_"+abook.ISBN+".XML"
		bookxml = open(fileName,"w")
		bookxml.write(data)
		bookxml.close()
		
	    time.sleep(2)
    

def main():
    print('start getXmls!')
    #doubanBookXML()
    doubanBookComments()
    

if __name__ =='__main__':
    main()