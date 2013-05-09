#coding=utf-8
import os
import re

def start():
	file=open('/Users/wangjz/Desktop/topic2.txt','r')
	tp=open('/Users/wangjz/Desktop/1.txt','w+')
	r1=re.compile(r'反垄断')
	while 1:
		line=file.readline()
		if line:
			if r1.search(line):
				words = line.split('\t',4)
				for word in words:
					tp.writelines('%s%s'%(word,os.linesep))
		else:
			break
		
	file.close()
	tp.close()


def main():
	start()
	
if __name__ =='__main__':
	main()