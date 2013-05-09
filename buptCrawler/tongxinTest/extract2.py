#coding=utf-8
import os
import re
import sys

#读取文本的每一行，存入列表中
def cmp0(x,y):
        if x[1]>y[1]:
                return 1
        elif x[1]<y[1]:
                return -1
        else:
                return 0
def start():
        file=open('/Users/wangjz/Desktop/topic2.txt','r')
        li=[]
        while True:
                line=file.readline()
                if line:
                        li.append(line)
                else:
                        break
        file.close()
        lines=len(li)
        #新建文本文档，用来保存抽取的信息
        #p=open('topic.txt','w+')
        tp=open('/Users/wangjz/Desktop/2.txt','w+')
        #正则表达式搜索
        content=[]
        dat=[]
        r1=re.compile(r'反垄断')
        for i in li:
                if r1.search(i):
                        content.append(i.split('\t',4))
                else:
                        continue
                
        #写入文件
        for eachList in content:    
                tp.writelines(['%s%s'%(eachline,os.linesep)for eachline in eachList])
        tp.close()

        
def main():
        print 'start'
        start()

if __name__=='__main__':
        main()
