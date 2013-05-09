import collections

d=collections.defaultdict(lambda:1)
 
def initDic(filename='SogouLabDic.dic'):
    f=open(filename,'r')
    total=0
    while True:
        line=f.readline()
        if not line:
            break
        word, freq = line.split('\t')[0:2]
        total+=1
        try:
            d[word.decode('gbk')]=int(freq)
        except:
            d[word]=int(freq)
    f.close()
    d['_t_']=total
 
def solve(s):
    l=len(s)
    p=[0 for i in range(l+1)]
    p[l]=1
    div=[1 for i in range(l+1)]
    t=[1 for i in range(l)]
    
    for i in range(l-1,-1,-1):#16~1
        for k in range(1,l-i+1):#1~2,1~3,1~4,1~5....
            tmp=d[s[i:i+k]]
            if k>1 and tmp==1:#cizu and tmp==1
                continue
            if(d[s[i:i+k]]*p[i+k]*div[i]>p[i]*d['_t_']*div[i+k]):
                p[i]=d[s[i:i+k]]*p[i+k]
                div[i]=d['_t_']*div[i+k]
                t[i]=k
    i=0
    while i<l:
        print s[i:i+t[i]]
        i=i+t[i]
 
if __name__ =='__main__':
    initDic()
    s="其中最简单的就是最大匹配的中文分词"
    s=s.decode('utf8')
    solve(s)