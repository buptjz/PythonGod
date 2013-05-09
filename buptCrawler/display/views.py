#from django.shortcuts import render_to_response
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from buptCrawler.crawler.models  import Link,IndexDB
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import simplejson

def testYanbing2(request):
    return render_to_response('jwPlayer.html')

def testYanbing(request):
    return render_to_response('bingjie.html')

def testLizi(request):
    return render_to_response('jwPlayer.html')

def searchPage(request):
    return render_to_response('searchPage.html')
def defaultPage(request):
    return render_to_response('defaultPage.html')
def aboutUs(request):
    return render_to_response('aboutUs.html')
def classification(request):
    return render_to_response('classification.html')

def searchResultWithIndex(request):
    links = []
    if request.GET.has_key('keyword') and request.GET.has_key('page'):
	keyword = request.REQUEST['keyword']
	oneIndex = IndexDB.objects.filter(keyword__contains=keyword)[0]
	DocIds = oneIndex.docIDs
	ids = DocIds.split('+')
	for oneID in ids:
#	    aLink = Link.objects.
	    print oneID
	    
    return HttpResponse("no this information")

def searchResult(request):
    if request.GET.has_key('keyword') and request.GET.has_key('page'):
	keyword = request.REQUEST['keyword']
	if request.GET.has_key('classfication'):
	    classfication = request.REQUEST['classfication']
	    links = Link.objects.filter(classification__contains=classfication).order_by('keywords','-publishtime')
	    #linksex = links.exclude(sourcesite='buptOA')
	    #linksin = links.filter(sourcesite='buptOA')
	    #linksin.append(linksex)
	else:   
	    links = Link.objects.filter(body__icontains=keyword).order_by('keywords','-publishtime')
	paginator = Paginator(links , 10)
	page = request.GET.get('page')
    else:
	keyword = request.REQUEST['keyword']
	links = Link.objects.filter(body__icontains=keyword).order_by('keywords','-publishtime')
	paginator = Paginator(links , 10)
	page = "1"
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页码不在范围内，返回最后一页
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('searchresult.html', {"links": contacts,'keyword':keyword})

def searchResultJson(request):
    print("searchResultJson")
    if request.GET.has_key('keyword') and request.GET.has_key('page'):
	keyword = request.REQUEST['keyword']
	if request.GET.has_key('classfication'):
	    classfication = request.REQUEST['classfication']
	    links = Link.objects.filter(classification__contains=classfication).order_by('keywords','-publishtime')
	    
	else:   
	    #links = Link.objects.filter(body__icontains=keyword)
	    links = Link.objects.filter(body__icontains=keyword).order_by('keywords','-publishtime')
	paginator = Paginator(links , 20)
	page = request.GET.get('page')
    else:
	keyword = request.REQUEST['keyword']
	links = Link.objects.filter(body__icontains=keyword).order_by('keywords','-publishtime')
	paginator = Paginator(links , 20)
	page = "1"
    
    
    try:
        contacts = paginator.page(page)	
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页码不在范围内，返回最后一页
        contacts = paginator.page(paginator.num_pages)
	
    result={}
    result['imgurl']='http://'
    result['data']=list(contacts.object_list.values('url','descriptions','publishtime','classification','sourcesite','author'))
    return HttpResponse(simplejson.dumps(result))

def asearchResultJson(request):
    print("searchResultJson")
    if request.GET.has_key('keyword') and request.GET.has_key('page'):
	keyword = request.REQUEST['keyword']
	if request.GET.has_key('classfication'):
	    classfication = request.REQUEST['classfication']
	    links = Link.objects.filter(classification__contains=classfication).order_by('keywords','-publishtime')
	    
	else:   
	    #links = Link.objects.filter(body__icontains=keyword)
	    links = Link.objects.filter(body__icontains=keyword).order_by('keywords','-publishtime')
	paginator = Paginator(links , 20)
	page = request.GET.get('page')
    else:
	keyword = request.REQUEST['keyword']
	links = Link.objects.filter(body__icontains=keyword).order_by('keywords','-publishtime')
	paginator = Paginator(links , 20)
	page = "1"
    try:
        contacts = paginator.page(page)

	
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页码不在范围内，返回最后一页
        contacts = paginator.page(paginator.num_pages)
    #return render_to_response('searchresult.html', {"links": contacts,'keyword':keyword})
    #transform the links on this page into Json format
    for link in contacts.object_list:
	print link.author
	
    result={}
    result['imgurl']='http://'
    result['data']=list(contacts.object_list.values('url','descriptions','publishtime','classification','sourcesite','author'))
    return HttpResponse(simplejson.dumps(result))	
    
		
def eventList(request):
    if request.GET.has_key('keyword'):
	keyword = request.REQUEST['keyword']
	links = Link.objects.filter(body__icontains=keyword)[0:10]
	if links:
	    return render_to_response('index.html', {'links': links,'keyword':keyword})
		#return HttpResponse(body)	
	else:
	    return HttpResponse("no this information")
	
def buptOARequest(request):
    if request.GET.has_key('pageid'):
	pageid = request.REQUEST['pageid']
	links = Link.objects.filter(id=pageid)
	if links:
	    for eachlink in links:
		body = eachlink.url
		#return render_to_response(body)
		return HttpResponse(body)	
	else:
	    return HttpResponse("no this information")
	
def buptOASearch(request):
    if request.GET.has_key('keyword'):
	keyword = request.REQUEST['keyword']
	links = Link.objects.filter(body__icontains=keyword)
	if links:
	    body = []
	    for eachlink in links:
		body.append (eachlink.url)
		body.append("\n")
		#return render_to_response(body)
	    return HttpResponse(body)
	else:
	    return HttpResponse("no this information")