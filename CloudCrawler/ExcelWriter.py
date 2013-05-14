# -*- coding: utf-8 -*-
#!/usr/bin/env python
#Write Data into Excel file
from xlrd import open_workbook
from xlutils.copy import copy
 
def writeData(filePath,sheetName,column,data,isRealTime):
  try:
    rb = open_workbook(filePath)
    
    rs = rb.sheet_by_name(sheetName)
    sheetNames = rb.sheet_names()
    sheetIndex= sheetNames.index(sheetName)
    
    wb = copy(rb)
    #rs = rb.sheet_by_name(sheetName)
    
    #通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(sheetIndex)    
    
  except:
    print(u"打开文件失败，请确认目录正确")
    return
  #通过sheet_by_index()获取的sheet没有write()方法
  #rs = rb.sheet_by_index(0)

  if column == None:
    column = rs.ncols
    
  #写入数据
  row = 0
  for item in data:
    row = row + 1
    ws.write(row,column,item) #需要转中文转化
      
      
  if isRealTime == None:
    pass
  else:
    row += 1
    if isRealTime == True:
      ws.write(row,column,"1")
    elif isRealTime == False:
      ws.write(row,column,"0")    
      
  try:
    wb.save(filePath)
  except:
    print(u"文件保存失败，请确认excel文件没有被其他应用使用")
    return
  
