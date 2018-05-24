
#datetime，取时间的
#import datetime
import win32com.client
from win32timezone import *
import win32timezone
#import easygui as g


def excel_file():

    f=open('config.txt','r')

    excel0=f.readlines()[0].replace('\n','')

    f=open('config.txt','r')

    excel1=f.readlines()[1].replace('\n','')
    return excel0,excel1

def 保存(excel1):
    try:
        copy(xlrd.open_workbook(excel1,formatting_info=True)).save(excel1)
    except:
        g.msgbox(excel1+'被其他人打开，请先关闭')
        exit()
def max_oder_num():
    for i in range (6,10000):
        order=(str(订单记录.Cells(i,5).Value)+'-'+str(订单记录.Cells(i,6).Value)).replace('.0','')
        if order =='None-None':
            break
    return i-1
def search(last_item):
    for i in range (6,10000):
        order=(str(订单记录.Cells(i,5).Value)+'-'+str(订单记录.Cells(i,6).Value)).replace('.0','')
        if order ==last_item:
            
            break
    return i

def last_item():
    for i in range (6,10000):
        order=个部.Cells(i,7).Value
        if order is None:
            #print (order)
            break
    return i-1,str(个部.Cells(i-1,7).Value)

    
if __name__=="__main__":
    excel0,excel1=excel_file()
    print ('excel0源 is:',excel0,'\n', 'excel目标 is ',excel1)

    excel = win32com.client.Dispatch('Excel.Application')
    workbook0 = excel.Workbooks.Open(excel0)
    workbook1 = excel.Workbooks.Open(excel1)
    订单记录 = workbook0.WorkSheets('订单记录')
    个部 = workbook1.WorkSheets('个部')
    current_line,current_item=last_item()
    print ('last item is ',current_line,current_item)
    max_line=max_oder_num()
    print ('excel源文件最大订单行数为:',max_line)
    meet_line=search(current_item)
    print (current_item, 'is in ',meet_line)
    个部.Cells(1,3).Value = "hello2"
    item_number=max_line-meet_line
    if item_number==0:
        lasttime=str(订单记录.Cells(max_line,2))[0:19]+':订单号:'+(str(订单记录.Cells(max_line,5).Value)+'-'+str(订单记录.Cells(max_line,6).Value)).replace('.0','')
        print (lasttime)
        #g.msgbox('最近没有更新内容，上次更新时间为'+lasttime)
    else:
        #g.msgbox(str(item_number)+'项更新')
        for i in range(item_number):
            order=(str(订单记录.Cells(meet_line+1+i,5).Value)+'-'+str(订单记录.Cells(meet_line+1+i,6).Value)).replace('.0','')
            date=str(订单记录.Cells(meet_line+1+i,2).Value)[0:10]
            time=str(订单记录.Cells(meet_line+1+i,2).Value)[11:16]
            number=订单记录.Cells(meet_line+1+i,8).Value
            customer=订单记录.Cells(meet_line+1+i,7).Value
            个部.Cells(current_line+1+i,6).Value = '新订单'
            个部.Cells(current_line+1+i,3).Value = '机器人'
            个部.Cells(current_line+1+i,4).Value = date
            个部.Cells(current_line+1+i,5).Value = time
            个部.Cells(current_line+1+i,7).Value = order
            个部.Cells(current_line+1+i,8).Value = number
            个部.Cells(current_line+1+i,9).Value = customer
    
    #workbook0.DisplayAlerts = False
    #workbook1.DisplayAlerts = False
    workbook0.Save()
    workbook1.Save()
    
    
    #w.save() 
    excel.Quit()
    

