import easygui as g
import xlrd,os
from xlutils.copy import copy

def switch(choice):
    if choice=='入库':
        print ('入库')
        rk = g.enterbox("请输入物品编码：\n",title="入库")
        
        beijian = xlrd.open_workbook('beijian.xls')
        table = beijian.sheet_by_name('data')
        nrows = table.nrows
        mode=0
        for i in range(nrows ):
            #print (table.row_values(i)[0])
            
            if table.row_values(i)[0]==rk:
                print ('same',rk)
                mode=1
                i0=i
            else:
                pass
        if mode==0:
            g.msgbox('无此物编,或请新增 '+rk, title='录入错误')
            return '重来'
        else:
            information=table.row_values(i0)[1]
            print (information)
            g.msgbox(table.row_values(i0)[1],rk,ok_button,image='image/'+rk+'.jpg')
            title = '入库'
            fieldNames = ['来源','数量','备注']
            fieldValues = []
            msg=rk+'\n'+table.row_values(i0)[1]
            fieldValues = g.multenterbox(msg,title,fieldNames)
            print(fieldValues[1])
            beijian = xlrd.open_workbook('beijian.xls')
            table = beijian.sheet_by_name('history')
            nrows = table.nrows
            beijian1 = copy(beijian)
            beijian1.get_sheet('history').write(nrows,0,rk)
            beijian1.get_sheet('history').write(nrows,1,information)
            beijian1.get_sheet('history').write(nrows,2,fieldValues[0])
            beijian1.get_sheet('history').write(nrows,3,fieldValues[1])
            beijian1.get_sheet('history').write(nrows,4,fieldValues[2])
            beijian1.save('beijian.xls')
            try:
                beijian1.save('beijian.xls')
                g.msgbox(rk+"\n"+information+"\n"+fieldValues[0]+"\n"+fieldValues[1]+"\n"+fieldValues[2],"入库成功")
            except:
                g.msgbox("保存失败，有人已打开excel表 \n 请关闭beijian.xls,再试")
                return 'back'
            return 'hello'
    if choice=='出库':
        print ('出库')
        rk = g.enterbox("请输入物品编码：\n",title="出库")
        
        beijian = xlrd.open_workbook('beijian.xls')
        table = beijian.sheet_by_name('data')
        nrows = table.nrows
        mode=0
        for i in range(nrows ):
            #print (table.row_values(i)[0])
            
            if table.row_values(i)[0]==rk:
                print ('same',rk)
                mode=1
                i0=i
            else:
                pass
        if mode==0:
            g.msgbox('无此物编,或请新增 '+rk, title='录入错误')
            return '重来'
        else:
            information=table.row_values(i0)[1]
            print (information)
            g.msgbox(table.row_values(i0)[1],rk,ok_button,image='image/'+rk+'.jpg')
            title = '出库'
            fieldNames = ['去向','数量','备注']
            fieldValues = []
            msg=rk+'\n'+table.row_values(i0)[1]
            fieldValues = g.multenterbox(msg,title,fieldNames)
            print(fieldValues[1])
            beijian = xlrd.open_workbook('beijian.xls')
            table = beijian.sheet_by_name('history')
            nrows = table.nrows
            beijian1 = copy(beijian)
            beijian1.get_sheet('history').write(nrows,0,rk)
            beijian1.get_sheet('history').write(nrows,1,information)
            beijian1.get_sheet('history').write(nrows,2,fieldValues[0])
            beijian1.get_sheet('history').write(nrows,3,fieldValues[1])
            beijian1.get_sheet('history').write(nrows,4,fieldValues[2])
            beijian1.save('beijian.xls')
            try:
                beijian1.save('beijian.xls')
                g.msgbox(rk+"\n"+information+"\n"+fieldValues[0]+"\n"+fieldValues[1]+"\n"+fieldValues[2],"出库成功")
            except:
                g.msgbox("保存失败，有人已打开excel表 \n 请关闭beijian.xls,再试")
                return 'back'
        return 'hello'
    if choice=='新增':
        print ('新增')
        beijian = xlrd.open_workbook('beijian.xls')
        table = beijian.sheet_by_name('data')
        nrows = table.nrows
        #ncols = table.ncols
        #nrows代表行数
        
        data='NC'+str(nrows+5010001001)
        
        
        st = g.enterbox("请输入物品描述：\n")

        ccbox = g.ccbox(data+": "+st,title="新增",choices=('确定','取消'))
        if ccbox==True:
            print ('y')
            beijian = xlrd.open_workbook('beijian.xls')
            beijian1 = copy(beijian)
            beijian1.get_sheet('data').write(nrows,0,data)
            beijian1.get_sheet('data').write(nrows,1,st)

            beijian1.save('beijian.xls')
            
        return 'hello'
        
    if choice=='库存':
        print ('库存')
        os.system('storage.xls')
        return 'hello'
        
    return 'end'
#import image
title='捷德备件管理系统'
msg='请问要执行哪类操作？'
ok_button='你确定？'
image='python.png'
#g.msgbox(msg,title)
choices=['入库','出库','新增','库存','退出']
#choice=g.choicebox(msg,title,choices)
#g.msgbox(choice,title,ok_button,image)
#g.ccbox(msg,choices=('y','n'))
while True:
    choice=g.buttonbox(msg,title,choices)
#g.indexbox(msg,title,choices)
    if switch(choice) == 'end':
        break


