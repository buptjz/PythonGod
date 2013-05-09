from django.conf.urls.defaults import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buptCrawler.views.home', name='home'),
    # url(r'^buptCrawler/', include('buptCrawler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),7
    ('^public/',include('buptCrawler.display.urls')),
    ('^display/',include('buptCrawler.display.urls')),    #( r'^css/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/School/JZCrawler/buptCrawler/static/css/' }),
   #( r'^images/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': '/School/JZCrawler/buptCrawler/static/images/' }),
    ( r'^css/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/MyProject/buptCrawler/static/css/' }),
    ( r'^images/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': '/MyProject/buptCrawler/static/images/' }),
    ( r'^scripts/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/MyProject/buptCrawler/static/scripts/' }),
    ( r'^video/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/MyProject/buptCrawler/static/video/' }),
    ( r'^swf/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/MyProject/buptCrawler/static/swf/' }),
)
