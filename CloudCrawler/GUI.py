# -*- coding: utf-8 -*-
#!/usr/bin/env python
#Write Data into Excel file

import tkFileDialog
from Tkinter import *  #引入模块
from postRequest import *
import os
import infos
import ttk

FILEPATH = None

def runMain(ev=None):
 
    runMainFunc(FILEPATH.get())
    
def openFileDialog():
    global FILEPATH
    print os.getcwd()
    filename = tkFileDialog.askopenfilename(initialdir = os.getcwd())
    writeSetting(filename)
    FILEPATH.set(filename)
    print FILEPATH.get()

def writeSetting(path):
    settingsFile = open('settings.txt','w')    
    settingsFile.write(path)
    settingsFile.close()
    
def getSettings():
    
    settingsFile = open('settings.txt','r')
    path = settingsFile.read()
    settingsFile.close()
    return path
    

#config函数就是通过设置组件的参数来改变组件的，这里改变的是font字体大小
def main():
    global FILEPATH
  
    top=Tk()   #主窗口
    top.geometry('600x380')  #设置了主窗口的初始大小600x400
    
    #label=Label(top,text=infos.DISPLAYINFO,font='Helvetica -18 bold',justify = 'left')  #设置标签字体的初始大小
    label=Label(top,text=infos.DISPLAYINFO,justify = 'left')  #设置标签字体的初始大小
    label.place(width = 545,height = 200,relx = 0.04,rely = 0.04)
    
    label2=Label(top,text="Excel文件",justify = 'left')  #设置标签字体的初始大小
    label2.place(width = 70,height = 35,relx = 0.04,rely = 0.49)
    
    FILEPATH = StringVar()
    entry = Entry(top,textvariable = FILEPATH)
    path = getSettings()
    FILEPATH.set(path)
    entry.place(width = 420,height = 35,relx = 0.04,rely = 0.59)

    openWindowButton= Button(top,text=' 选择.. ',command=openFileDialog,activeforeground='white',activebackground='red')
    openWindowButton.place(width=124,height = 35,relx = 0.75,rely = 0.59)
    
    startButton= Button(top,text=' 获取数据 ',command=runMain,activeforeground='white',activebackground='red',borderwidth=3)
    startButton.place(width=550,height = 65,relx = 0.04,rely = 0.72)    

    #pbar = ttk.Progressbar(top, length=200, maximum=100)
    #pbar.place(width=550,height =25,relx = 0.04,rely = 0.91)    
    
    mainloop()
    
if __name__ =='__main__':
    main()