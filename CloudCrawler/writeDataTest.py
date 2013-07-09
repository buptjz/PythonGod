from datetime import datetime
import xlwt
 
#Create workbook and worksheet
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('temperatures')
 
#Set up a date format style to use in the spreadsheet
excel_date_fmt = 'M/D/YY h:mm'
style = xlwt.XFStyle()
style.num_format_str = excel_date_fmt
  
#The format of the date string we'll be building
python_str_date_fmt = '%d %b-%H%M-%Y'
date_object = datetime.strptime(date_string,python_str_date_fmt)
 
#Write the data, using the style defined above.
sheet.write(row,0,date_object, style)