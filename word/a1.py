import xlrd
#from xlwt import Workbook
from xlutils.copy import copy
workbook="a1.xls"
rb = xlrd.open_workbook(workbook)
wb = copy(rb)
s = wb.get_sheet('Sheet2')
s.write(0,0,'A3')
wb.save(workbook)
