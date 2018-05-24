'''
本文需求来自一个备件管理模块
比较简单，不涉及价格，但涉及库位，故为简单的出入库管理系统
原理是此python使用easygui作为界面，数据来源读写都在excel表格中
相当于使用excel作为简易数据库
创作人邮箱10054053@qq.com
我对python着了迷，甚至前一段想直接使用numpy作为数据库 ：-D

'''
#解释：easygui,图形界面，简漏了一些，不过省时省力

import easygui as g
#xlrd读取是excel文件的
import xlrd,os
#xlutils是用来修改写入excel文件的
from xlutils.copy import copy
#datetime，取时间的
import datetime
#定义now的格式
def now():
    return datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')

#print (now())

def switch(choice):
    if choice=='入库':
        check_in()
        
    if choice=='出库':
        check_out()
    if choice=='新增':
        new_material()
        
    if choice=='导出':
        daochu()
    if choice=='搜索':
        search()
    if choice=='库存':
        kucun() 
    if choice=='移库':
        move()
    if choice=='盘点':
        pandian()
    if choice=='预警':
        warning()
    if choice=='历史':
        history()
        
    return 'end'

def exist(x):
    beijian = xlrd.open_workbook(workbook)
    table0 = beijian.sheet_by_name('data')
    nrows = table0.nrows
    mode=0
    
         
    #历遍主数据，如果查到有一样的，mode取1，没查到取0，查到时记录行号i0
    for i in range(nrows ):
        #print (table.row_values(i)[0])
        
        if table0.row_values(i)[0]==x:
            #print ('same',rk)
            return True
            break
        else:
            continue
    if mode==0:
        g.msgbox('无此物编,或请新增 ', title='录入错误')
        menu()


def history():
    record=g.boolbox(msg='历史?', title=' ', choices=('单品历史', '整体历史限500条,更多请选择【导出】功能'), image=None, default_choice='Yes', cancel_choice='No')
    beijian = xlrd.open_workbook(workbook)
    table0 = beijian.sheet_by_name('history')
    nrows = table0.nrows
    list=[]
    if record==False:

        
        for i in range(0,500):
            j=nrows-1-i
            if j >=0:
                #print (j)
                list.append('\n'+table0.row_values(j)[0]+table0.row_values(j)[1]+table0.row_values(j)[2]+' 数量：'+str(table0.row_values(j)[3])+table0.row_values(j)[4]+table0.row_values(j)[5]+' 时间：'+table0.row_values(j)[6]+' 库位:'+table0.row_values(j)[7])
        
    else:
        rk = g.enterbox("请输入物品编码：\n",title="历史")
        if exist(rk) ==True:
            for i in range(nrows):
                if table0.row_values(nrows-1-i)[0]==rk:
                    list.append('\n'+table0.row_values(nrows-1-i)[0]+table0.row_values(nrows-1-i)[1]+table0.row_values(nrows-1-i)[2]
                                +' 数量：'+str(int(table0.row_values(nrows-1-i)[3]))
                                +table0.row_values(nrows-1-i)[4]
                                +table0.row_values(nrows-1-i)[5]
                                +' 时间：'+table0.row_values(nrows-1-i)[6]
                                +' 库位：'+table0.row_values(nrows-1-i)[7]
                                )
    g.msgbox(list)
                
                
                    
                
        
    
    menu()
def move():
    rk = g.enterbox("请输入物品编码：\n",title="移库")
    if exist(rk) ==True:
        beijian = xlrd.open_workbook(workbook)
        table0 = beijian.sheet_by_name('data')
        nrows = table0.nrows
        for i in range(nrows ):
            if table0.row_values(i)[0]==rk:
                i0=i
                break
        print (i0)
        newkuwei=g.enterbox(msg=table0.row_values(i)[0]+'\n'+'请输入新库位，默认值为原库位',title='移库',default=table0.row_values(i0)[2])
        beijian1 = copy(beijian)
        beijian1.get_sheet('data').write(i0,2,newkuwei)
        try:
            beijian1.save(workbook)
            g.msgbox("修改成功")
        except:
            g.msgbox("保存失败，有人已打开excel表 \n 请关闭beijian.xls,再试")
    else:
        menu()




        
def warning():
    yujing=g.boolbox(msg='预警?', title=' ', choices=('修改预警值', '预警报告'), image=None, default_choice='Yes', cancel_choice='No')
    if yujing==False:
        beijian = xlrd.open_workbook(workbook)
        table0 = beijian.sheet_by_name('data')
        nrows = table0.nrows
        mode=0
    #历遍主数据，如果查到有一样的，mode取1，没查到取0，查到时记录行号i0
        list=[]
        for i in range(nrows ):
        #print (table.row_values(i)[0])
            if int(table0.row_values(i)[4])<int(table0.row_values(i)[5]):
        
        
                list.append('\n'+table0.row_values(i)[0]+' '+table0.row_values(i)[1]+' 库位: '+table0.row_values(i)[2]+' '+table0.row_values(i)[3]+'  库存:'+str(int(table0.row_values(i)[4]))+' 预警: '+str(int(table0.row_values(i)[5]))+' ')

        g.msgbox(list)

    else:
        wubian=g.enterbox("请输入精确物编：\n",title="盘点")
        beijian = xlrd.open_workbook(workbook)
        table0 = beijian.sheet_by_name('data')
        nrows = table0.nrows
        mode=0
    #历遍主数据，如果查到有一样的，mode取1，没查到取0，查到时记录行号i0
        list=[]
        for i in range(nrows ):
        #print (table.row_values(i)[0])
            if wubian==table0.row_values(i)[0]:
                print (wubian)
                new_yujing=g.enterbox("请输入新预警值：\n",title=table0.row_values(i)[0],default=int(table0.row_values(i)[5]))
                if new_yujing==None:
                    menu()
                beijian1 = copy(beijian)

                beijian1.get_sheet('data').write(i,5,int(new_yujing))
                try:
                    beijian1.save(workbook)
                    g.msgbox("修改成功")
                except:
                    g.msgbox("保存失败，有人已打开excel表 \n 请关闭beijian.xls,再试")
    
    menu()
    
def pandian():
    kuwei0=g.enterbox("请输入精确库位：\n",title="盘点")
    if kuwei0==None:
        menu()
        
    beijian = xlrd.open_workbook(workbook)
    table0 = beijian.sheet_by_name('data')
    nrows = table0.nrows
    list0=[]
    #历遍主数据，如果查到有一样的，mode取1，没查到取0，查到时记录行号i0
    for i in range(nrows ):
        #print (table.row_values(i)[0])
        
        if table0.row_values(i)[2]==kuwei0:
            #print ('same',rk)
            #list0.append(
            list0.append('\n'+table0.row_values(i)[0]+' '+table0.row_values(i)[1]+' 库位1: '+table0.row_values(i)[2]+' '+table0.row_values(i)[3]+'  库存:'+str(int(table0.row_values(i)[4]))+' 预警: '+str(int(table0.row_values(i)[5]))+' ')
        else:
            pass
    g.msgbox(list0)
    menu()


def search():
    
    rk = g.enterbox("请输入关键词：\n",title="搜索")
    #print ('rk',rk)
    if rk==None:
        menu()
        
    beijian = xlrd.open_workbook(workbook)
    table0 = beijian.sheet_by_name('data')
    nrows = table0.nrows
    mode=0
    #历遍主数据，如果查到有一样的，mode取1，没查到取0，查到时记录行号i0
    list=[]
    for i in range(nrows ):
        #print (table.row_values(i)[0])
        
        if rk in table0.row_values(i)[1]:
            list.append('\n'+table0.row_values(i)[0]+' '+table0.row_values(i)[1]+' 库位: '+table0.row_values(i)[2]+' '+table0.row_values(i)[3]+'  库存:'+str(int(table0.row_values(i)[4]))+' 预警: '+str(int(table0.row_values(i)[5]))+' ')
        else:
            pass
    if list==[]:
        g.msgbox('没有结果，请尝试其它关键词',title='搜索结果')
    else:
        g.msgbox(list,title='搜索结果')
    menu()

def kucun():
    
    
    beijian = xlrd.open_workbook(workbook)
    table0 = beijian.sheet_by_name('data')
    nrows = table0.nrows
    mode=0
    #历遍主数据，如果查到有一样的，mode取1，没查到取0，查到时记录行号i0
    list=[]
    for i in range(nrows ):
        #print (table.row_values(i)[0])
        
        
        list.append('\n'+table0.row_values(i)[0]+' '+table0.row_values(i)[1]+' 库位: '+table0.row_values(i)[2]+' '+table0.row_values(i)[3]+'  库存:'+str(int(table0.row_values(i)[4]))+' 预警: '+str(int(table0.row_values(i)[5]))+' ')

    g.msgbox(list)

        
    menu()
#import image
#主界面，包含标题，信息，选项等内容
def daochu():
    #print ('hello')
    beijian = xlrd.open_workbook(workbook)
    beijian1 = copy(beijian)
    now1=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    beijian1.save(now1+'.xls')
    os.system(now1+'.xls')
    print ('end')
    menu()
    

def menu():
    title='捷德备件管理系统'
    msg='请问要执行哪类操作？'
    ok_button='确定？'
    #image='python.png'
    #g.msgbox(msg,title)
    choices=['搜索','入库','出库','新增','移库','库存','历史','导出','预警','盘点','退出']
    #choice=g.choicebox(msg,title,choices)
    #g.msgbox(choice,title,ok_button,image)
    #g.ccbox(msg,choices=('y','n'))
    #用while做循环，并且调用自制的swich工具
    while True:
        choice=g.buttonbox(msg,title,choices)
    #g.indexbox(msg,title,choices)
        if switch(choice) == 'end':
            break
def check_in():
#print ('入库')
    #这里其实可以使用条码枪
    rk = g.enterbox("请输入物品编码：\n",title="入库")
    #print ('rk',rk)
    if rk==None:
        menu()
        
    beijian = xlrd.open_workbook(workbook)
    table0 = beijian.sheet_by_name('data')
    nrows = table0.nrows
    mode=0
    #历遍主数据，如果查到有一样的，mode取1，没查到取0，查到时记录行号i0
    for i in range(nrows ):
        #print (table.row_values(i)[0])
        
        if table0.row_values(i)[0]==rk:
            #print ('same',rk)
            mode=1
            i0=i
        else:
            pass
    if mode==0:
        g.msgbox('无此物编,或请新增 '+rk, title='录入错误')
        menu()
    else:
        information=table0.row_values(i0)[1]
        #print (information)
        ok_button='确定？'
        g.msgbox(rk+"\n"+'信息: '+table0.row_values(i0)[1]+"\n"+'当前库存: '+str(int(table0.row_values(i0)[4]))+"\n"+'库位:'+table0.row_values(i0)[2],ok_button,image='image/'+rk+'.jpg')
        title = '入库'
        fieldNames = ['来源','数量(必填)*','备注']
        fieldValues = []
        #msg=rk+'\n'+'信息: '+table0.row_values(i0)[1]+"\n"+'当前库存: '+str(int(table0.row_values(i0)[4]))+"\n"+'预警库存: '+str(int(table0.row_values(i0)[5]))
        msg='hello'
        fieldValues = g.multenterbox(msg,title,fieldNames)
        if fieldValues==None:
            menu()
        if fieldValues[1]=='':
            g.msgbox("数量不能为空，可以取消")
            menu()
        #print(fieldValues[1])
        #beijian = xlrd.open_workbook('beijian.xls')
        kuwei=g.enterbox('库位',default=table0.row_values(i0)[2])
        if kuwei==None:
            g.msgbox("操作取消")
            menu()

        table = beijian.sheet_by_name('history')
        nrows = table.nrows
        beijian1 = copy(beijian)
        beijian1.get_sheet('history').write(nrows,0,rk)
        beijian1.get_sheet('history').write(nrows,1,information)
        beijian1.get_sheet('history').write(nrows,2,fieldValues[0])
        beijian1.get_sheet('history').write(nrows,3,int(fieldValues[1]))
        beijian1.get_sheet('history').write(nrows,4,fieldValues[2])
        beijian1.get_sheet('history').write(nrows,5,'原库存'+str(int(table0.row_values(i0)[4]))+'+'+'变化量'+fieldValues[1]+'='+'最新库存'+str(int(table0.row_values(i0)[4])+int(fieldValues[1])))
        beijian1.get_sheet('history').write(nrows,6,now())
        beijian1.get_sheet('history').write(nrows,7,kuwei)
        beijian1.get_sheet('data').write(i0,4,int(table0.row_values(i0)[4])+int(fieldValues[1]))
        beijian1.get_sheet('data').write(i0,2,kuwei)
        #int(table0.row_values(i0)[4])+int(fieldValues[1])
        try:
            beijian1.save(workbook)
            g.msgbox('ID: '+rk+"\n"+'信息: '+information+"\n"+'来源: '+fieldValues[0]+"\n"+'数量: '+fieldValues[1]+"\n"+'库位: '+kuwei+"\n"+'时间: '+now()+"\n"+'原库存'+str(int(table0.row_values(i0)[4]))+'+'+'变化量'+fieldValues[1]+'='+'最新库存'+str(int(table0.row_values(i0)[4])+int(fieldValues[1])),"入库成功")
            #g.msgbox('原库存'+str(int(table0.row_values(i0)[4]))+'+'+'变化量'+fieldValues[1]+'='+'最新库存'+str(int(table0.row_values(i0)[4])+int(fieldValues[1])))
        except:
            g.msgbox("保存失败，有人已打开excel表 \n 请关闭beijian.xls,再试")
            
        menu()


def check_out():
#print ('入库')
    #这里其实可以使用条码枪
    rk = g.enterbox("请输入物品编码：\n",title="出库")
    #print ('rk',rk)
    if rk==None:
        menu()
        
    beijian = xlrd.open_workbook(workbook)
    table0 = beijian.sheet_by_name('data')
    nrows = table0.nrows
    mode=0
    #历遍主数据，如果查到有一样的，mode取1，没查到取0，查到时记录行号i0
    for i in range(nrows ):
        #print (table.row_values(i)[0])
        
        if table0.row_values(i)[0]==rk:
            #print ('same',rk)
            mode=1
            i0=i
        else:
            pass
    if mode==0:
        g.msgbox('无此物编,或请新增 '+rk, title='录入错误')
        menu()
    else:
        information=table0.row_values(i0)[1]
        #print (information)
        ok_button='确定？'
        g.msgbox(rk+"\n"+'信息: '+table0.row_values(i0)[1]+"\n"+'当前库存: '+str(int(table0.row_values(i0)[4]))
                 +"\n"+' 库位: '+table0.row_values(i0)[2]+"\n"+' 预警库存: '+str(int(table0.row_values(i0)[5])),ok_button,image='image/'+rk+'.jpg')
        #g.msgbox(rk+"\n"+'信息: '+table0.row_values(i0)[1]+"\n"+'当前库存: '+str(int(table0.row_values(i0)[4]))+"\n"+'库位:'+table0.row_values(i0)[2]+"\n",ok_button,image='image/'+rk+'.jpg')
        title = '出库'
        fieldNames = ['去向','数量(必填)*','备注']
        fieldValues = []
        msg=rk+'\n'+'信息: '+table0.row_values(i0)[1]+"\n"+'当前库存: '+str(int(table0.row_values(i0)[4]))+"\n"+'预警库存: '+str(int(table0.row_values(i0)[5]))+"\n"+' 库位: '+table0.row_values(i0)[2]
        fieldValues = g.multenterbox(msg,title,fieldNames)
        if fieldValues==None:
            menu()
        if fieldValues[1]=='':
            g.msgbox("数量不能为空，可以取消")
            menu()
        else:
            fieldValues[1]=str(0-int(fieldValues[1]))
        #print(fieldValues[1])
        #beijian = xlrd.open_workbook('beijian.xls')
        table = beijian.sheet_by_name('history')
        nrows = table.nrows
        beijian1 = copy(beijian)
        beijian1.get_sheet('history').write(nrows,0,rk)
        beijian1.get_sheet('history').write(nrows,1,information)
        beijian1.get_sheet('history').write(nrows,2,fieldValues[0])
        beijian1.get_sheet('history').write(nrows,3,int(fieldValues[1]))
        beijian1.get_sheet('history').write(nrows,4,fieldValues[2])
        beijian1.get_sheet('history').write(nrows,5,'原库存'+str(int(table0.row_values(i0)[4]))+'+'+'变化量'+fieldValues[1]+'='+'最新库存'+str(int(table0.row_values(i0)[4])+int(fieldValues[1])))
        beijian1.get_sheet('history').write(nrows,6,now())
        beijian1.get_sheet('data').write(i0,4,int(table0.row_values(i0)[4])+int(fieldValues[1]))
        #int(table0.row_values(i0)[4])+int(fieldValues[1])
        try:
            beijian1.save(workbook)
            g.msgbox('ID: '+rk+"\n"+'信息: '+information+"\n"+'来源: '+fieldValues[0]+"\n"+'数量: '+fieldValues[1]+"\n"+'库位: '+fieldValues[2]+"\n"+'时间: '+now()+"\n"+'原库存'+str(int(table0.row_values(i0)[4]))+'+'+'变化量'+fieldValues[1]+'='+'最新库存'+str(int(table0.row_values(i0)[4])+int(fieldValues[1])),"出库成功")
            #g.msgbox('原库存'+str(int(table0.row_values(i0)[4]))+'+'+'变化量'+fieldValues[1]+'='+'最新库存'+str(int(table0.row_values(i0)[4])+int(fieldValues[1])))
        except:
            g.msgbox("保存失败，有人已打开excel表 \n 请关闭beijian.xls,再试")
            
        menu()


        
#新增物料模块    
def new_material():
    beijian = xlrd.open_workbook(workbook)
    #主数据位于data表
    table = beijian.sheet_by_name('data')
    #nrows代表行数，意思是主数据现在排到了多少行。
    nrows = table.nrows
    #ncols = table.ncols
        
    #自定义流水编号，这里使用NC开头，并使用5000+当前行号，确保唯一性    
    ID='NC'+str(nrows+5010001001)
        
    #录入主数据内容描述   
    st = g.enterbox("请输入物品描述：\n")
    #点取消，退回主菜单
    if st==None:
        menu()
    #确定窗口，包含流水号和物品描述
    yujingzhi = g.enterbox("请输入物品预警值：\n",default=0)
    if yujingzhi==None:
        menu()
    ccbox = g.ccbox(ID+": "+st,title="新增",choices=('确定','取消'))
    if ccbox==True:
            #print ('y')
        #beijian = xlrd.open_workbook('beijian.xls')文件写入，需要先复制一份，再保存覆盖
        #注意，不能在原
        beijian1 = copy(beijian)
        #在最下行，第一列，写入ID流水号码
        beijian1.get_sheet('data').write(nrows,0,ID)
        #在最下行，第一列，写入物品描述
        beijian1.get_sheet('data').write(nrows,1,st)
        beijian1.get_sheet('data').write(nrows,4,0)
        beijian1.get_sheet('data').write(nrows,5,int(yujingzhi))
        beijian1.get_sheet('data').write(nrows,2,'未入库')
        g.msgbox(ID+": "+st+" 新增成功！")
        #保存，并覆盖原有excel表
        try:
            beijian1.save(workbook)
        except:
            g.msgbox("保存失败，有人已打开excel表 \n 请关闭beijian.xls,再试")
        menu()
    #点取消，退回主菜单
    else:
        g.msgbox("已被取消")
        menu()       
  
    
#主模块
if __name__=="__main__":
    workbook='database/beijian.xls'
    #menu()
    #先做一些定义，例如数据存储的excel表名称
    password=g.passwordbox(msg="请输入您的密码",title="捷德备件管理系统")
    if password=='password':
        
    #调用主界面
        menu()
    else:
        g.msgbox('密码错误')
   

