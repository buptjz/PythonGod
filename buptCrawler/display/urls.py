#coding=utf8
#http://127.0.0.1:8000/display/searchResultJson?keyword=教一
from django.conf.urls.defaults import patterns, include, url
import settings
urlpatterns = patterns('',
    (r'^buptOARequest$', 'buptCrawler.display.views.buptOARequest'),
    (r'^buptOASearch$', 'buptCrawler.display.views.buptOASearch'),
    
    (r'^eventList$','buptCrawler.display.views.eventList'),
    
    (r'^searchResultJson$','buptCrawler.display.views.searchResultJson'),#for mobile
    (r'^searchResult$','buptCrawler.display.views.searchResult'),
    (r'^searchResultWithIndex$','buptCrawler.display.views.searchResultWithIndex'),
    (r'^classification$','buptCrawler.display.views.classification'),
    (r'^aboutUs$','buptCrawler.display.views.aboutUs'),
    (r'^defaultPage$','buptCrawler.display.views.defaultPage'),
    (r'^searchPage$','buptCrawler.display.views.searchPage'),
    
    (r'^testLizi$','buptCrawler.display.views.testLizi'),
    (r'^testYanbing$','buptCrawler.display.views.testYanbing'),
    (r'^testYanbing2$','buptCrawler.display.views.testYanbing2'),
    (r'^jwPlayer$','buptCrawler.display.views.testYanbing2'),
    
     (r'^send_score$','buptCrawler.display.views.send_score'),
    #(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.STATIC_PATH}),
)
