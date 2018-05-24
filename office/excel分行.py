'''
说实话，此脚本是拼凑出来的，不是很清楚细节
日后慢慢研究
'''
import xlwt;
import xlrd;
from xlutils.copy import copy;
  


for i in range(1,20000):
    oldWb = xlrd.open_workbook("fileName.xls", formatting_info=True);
    oldWbS = oldWb.sheet_by_index(0)
    newWb = copy(oldWb);
    newWs = newWb.get_sheet(0);
    print (i,oldWbS.cell(i,14).value)
    v=oldWbS.cell(i,14).value
    if v>3000:
        print (i,'>3000',"fenlie")
        inserRowNo = i
        newWs.write(inserRowNo, 14, 3000);
#newWs.write(inserRowNo, 1, "value2");
#newWs.write(inserRowNo, 2, "value3");
 
        for rowIndex in range(inserRowNo, oldWbS.nrows):
            for colIndex in range(oldWbS.ncols):
                newWs.write(rowIndex + 1, colIndex, oldWbS.cell(rowIndex, colIndex).value);
        newWb.save('fileName.xls')
        oldWb = xlrd.open_workbook("fileName.xls", formatting_info=True);
        oldWbS = oldWb.sheet_by_index(0)
        newWb = copy(oldWb);
        newWs = newWb.get_sheet(0);
        #print (oldWbS.cell(i-1,14),oldWbS.cell(i,14),oldWbS.cell(i+1,14).value-3000,oldWbS.cell(i+2,14))
        newWs.write(i+1, 14, v-3000)
        #newWs.write(i-1, 14, 401)
        newWb.save('fileName.xls')
        print (oldWbS.cell(i+1,14).value)
        #input('hello')
        
        newWb.save('fileName.xls')
        
print ("save with same name ok")
