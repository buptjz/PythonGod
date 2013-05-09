http://product.dangdang.com/product.aspx?product_id=22813131
http://m.dangdang.com/product.php?pid=22813131
http://api.douban.com/book/subject/2023011/reviews?start-index=1&max-results=10
http://api.douban.com/book/subject/isbn/7543639130
http://api.douban.com/book/subject/isbn/9787540456825
patternStarlevel=re.compile(r"""n>I S B N：(.+?)</s""",re.DOTALL)
patternStarlevel=re.compile(ur"""" src="(.+?)alt="" id="largePic".+?I S B N\xef\xbc\x9a(.+?)</s""",re.DOTALL)
http://api.douban.com/book/subject/isbn/{isbnID}/reviews?start-index=1&max-results=10
src="http://img31.ddimg.cn/66/4/22813131-1_b.jpg" alt="" id="largePic"
patternStarlevel=re.compile(ur"""" src="(.+?)alt="" id="largePic".+?I S B N\xef\xbc\x9a(.+?)</s""",re.DOTALL

def getImg(url):
    '''从核心代码中照图图片地址，并且下载保存、命名'''
    regImg = '<img src="(.*?)"  alt="" />'
    dir = 'F:\\My_Document\\Desktop\\temp\\'
    pageHtml = getPage(url)
    #找到所有图片地址
    imglist = re.findall(regImg,pageHtml)
    #print imglist
    for index in xrange(1,len(imglist)+1):
        finename = dir + str(index) + '.jpg'
        urllib.urlretrieve(imglist[index-1], finename)
        print finename + ' ok!'
