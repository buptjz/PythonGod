# -*- coding: utf-8 -*-
#!/usr/bin/env python
#Write Data into Excel file
from xlrd import open_workbook
from xlutils.copy import copy
 
 
def writeData(filePath,sheetName,column,data):
  try:
    rb = open_workbook(filePath)
    rs = rb.sheet_by_name(sheetName)
    wb = copy(rb)
    #通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(0)    
  except:
    print("打开文件失败，请确认目录正确")
    return
  #通过sheet_by_index()获取的sheet没有write()方法
  #rs = rb.sheet_by_index(0)

  if column == None:
    column = rs.ncols
  row = 1
  for item in data:
      ws.write(row,column,item) #需要转中文转化
      row = row + 1

  try:
    wb.save(filePath)
  except:
    print("文件保存失败，请确认excel文件没有被其他应用使用")
    return
  
