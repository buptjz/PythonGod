#from django.shortcuts import render_to_response
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from buptCrawler.crawler.models  import Link,IndexDB
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import simplejson
from models import RateScore,CurrentPlayer,Player

def get_current_player(request):
    '''客户端发来请求，获取当前选手id'''
    #http://127.0.0.1:8000/display/get_current_player?jid=3
    if request.GET.has_key('jid'):
	print u"[评委%s]\t发来请求,请求获取当前选手" %(request.REQUEST['jid'])
	
	currents = CurrentPlayer.objects.all()
	if currents:
	    current = currents[0]#return the only object
	    return HttpResponse("currentplayerid:"+current.current_player.playerID)
    else:
	return HttpResponse(u"fail get current player 工作人员在调试，请稍后重试")
    
def send_score(request):
    ''''客户端发送来选手得分，存入数据库'''
    #http://127.0.0.1:8000/display/send_score?jid=5&pid=3&score=90
    #This handler deals with the rate system
    if request.GET.has_key('score'):
	_judgerID = request.REQUEST['jid']
	_playerID = request.REQUEST['pid']
	
	_player = Player.objects.get(playerID = _playerID)
	_name = _player.playerName
	
	_score = request.REQUEST['score']
	print u"[评委%s]发送评分\n[选手:%s]\n[得分:%s]\n" %(_judgerID,_playerID,_score)
	p = RateScore.objects.create(judgerID=_judgerID, playerID=_playerID,playerName=_name,score=_score)	

	return HttpResponse("succesrate")    
    else:
	return HttpResponse("failed with send score")

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