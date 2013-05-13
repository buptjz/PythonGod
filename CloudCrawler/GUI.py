# -*- coding: utf-8 -*-
#!/usr/bin/env python
#Write Data into Excel file

from Tkinter import *  #引入模块
from postRequest import *

def runMain(ev=None):
    runMainFunc()

#config函数就是通过设置组件的参数来改变组件的，这里改变的是font字体大小
def main():
    top=Tk()   #主窗口
    top.geometry('600x400')  #设置了主窗口的初始大小600x400
    label=Label(top,text='Hello world!',font='Helvetica -12 bold')  #设置标签字体的初始大小
    label.pack(fill=Y,expand=1)
    
    startButton= Button(top,text=' 获取数据 ',command=runMain,activeforeground='white',activebackground='red')
    startButton.pack(expand=1)
    mainloop()
    
if __name__ =='__main__':
    main()