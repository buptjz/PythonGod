# -*- coding: utf-8 -*-
#!/usr/bin/env python
import urllib
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

def getImageWithURL(imageURL,fileName):
    try:
	urllib.urlretrieve(imageURL, fileName)
	print "[ Success ] download Image : " + imageURL
    except:
	print "[ Error ] download image : "+imageURL
	#Append the unsuccess url to a unsuccesfulFile
	ucf = open("/Users/wangjz/Desktop/down/images/unsImage.txt","w+")
	ucf.write(fileName)
	ucf.close()  
	    
    
    
def getImages():
    imageFilePath = "/Users/wangjz/Desktop/down/images/"
    books= Book.objects.all()
    for abook in books:
	if len(abook.imageurl) > 3:
	    length = len(abook.imageurl)
	    url = abook.imageurl[0:length-5] + "e.jpg"
	    isbn = abook.ISBN
	    fileName = imageFilePath+"BOOK_IMAGE_"+isbn+".jpg"
	    getImageWithURL(url,fileName)
	time.sleep(3)

def getImageURL():
    patternStarlevel=re.compile(ur"""__bigpic_pub"><img src="(.+?)" alt="" id="largePic".+?I S B N\xef\xbc\x9a(.+?)</s""",re.DOTALL)
    books= Book.objects.all()
    for abook in books:
	success,rawdata=utility.downloadUrl(abook.ddbookurl,'api.douban.com')
	if not success:
	    print('unsuccess with url'+abook.ddbookurl)
	else:
	    data=utility.zh2unicode(rawdata).encode('utf-8')
	    #Use regular expression to find the isbn in the page.
	    matches=patternStarlevel.findall(data)
	    imageUrl = matches[0][0]
	    print(imageUrl)
	    abook.imageurl = imageUrl
	    try:
		    abook.save()
	    except Exception,e:
		    print 'savlindbdis body error---',e
	time.sleep(2)
	    
def main():
    print('start getXmls!')
    getImages()
    
    

if __name__ =='__main__':
    main()