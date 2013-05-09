#coding=utf-8
#author:www.the5fire.com

import flickrapi
import os
import sys
import socket

api_key = '556fe985c9177856175eb239d44a40cb'
api_secrect = '54d0540425091ba4'

if __name__ == '__main__':

    urls = []
    reload(sys)
    print sys.getdefaultencoding()
    sys.setdefaultencoding('utf-8')
    print sys.getdefaultencoding()

    flickr = flickrapi.FlickrAPI(api_key, cache=True)
    try:
        photos = flickr.walk(text='flag',extras='url_z')
    except Exception:
        print 'error'
            
    try:
        for photo in photos:
            myurl = photo.get('url_z')
            if myurl is not None:
                myurl = myurl+'\n'
                urls.append(myurl)
                print myurl
    except Exception,ex: # XXX what error?
        print 'error'
        print Exception,':',ex
        
    file_object = open('flickUrls.txt', 'a')
    file_object.writelines(urls)
    file_object.close( ) 