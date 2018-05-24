import datetime,time
from easygui import fileopenbox
import os

date=datetime.datetime.now()
date1=date.strftime("%Y%m%d%H%M%S")
#print(date)
file_path=fileopenbox()
f = open(file_path,'r',encoding='UTF-16')
f0=open(date1+'.csv',"a+")
f0.write( 'so number-so item'+','+'TO_VBAP_KWMENG'+','+'T_CUSTOMER'+','+'T01_FINE_SPEC_ID'+','+'T01_FS_CATALOG_SAP_NOmaterial'+','+\
          'T_PRINTED_IM_CARD_RESTR'+','+'T01_CARDBODY_MATERIAL'+','+'T_RAW_IM_CARD_RESTR'+','+'T_MILLING'+','+'T_PLUG_IN'+','+\
          'T01_FS_PUNCH_SHAPE'+','+'T_RAW_CHIP_RESTR'+','+'T_CHIP_RESTR'+','+'T_OCA_CARD1'+','+'T_ECA_PERS'+','+'T_ATR_CHECK'+','+\
          'T01_MANUAL_INSPECTION'+','+'T01_FS_PIN_PUK_SAP_NO'+','+'T01_FS_VAP_SAP_NO'+','+'T_BOM_CB_QUANTITY'+','+\
          'T01_FS_WRAPPING_SAP_NO'+','+'T01_FS_PACKAGING_SAP_NO'+','+'\n')

order=[]
T_MILLING={}
T_PLUG_IN={}
T_RAW_IM_CARD_RESTR={}
T01_CARDBODY_MATERIAL={}
T_PRINTED_IM_CARD_RESTR={}
T01_FS_CATALOG_SAP_NO={}
T01_FINE_SPEC_ID={}
TO_VBAP_KWMENG={}
T_CUSTOMER={}
T01_FS_PUNCH_SHAPE={}
T_RAW_CHIP_RESTR={}
T_BOM_CB_QUANTITY={}


T_CHIP_RESTR={}
T_OCA_CARD1={}
T_ECA_PERS={}
T_ATR_CHECK={}
T01_MANUAL_INSPECTION={}
T01_FS_PIN_PUK_SAP_NO={}
T01_FS_VAP_SAP_NO={}

T01_FS_WRAPPING_SAP_NO={}
T01_FS_PACKAGING_SAP_NO={}

list1=[T_CHIP_RESTR,T_OCA_CARD1,T_ECA_PERS,T_ATR_CHECK,T01_MANUAL_INSPECTION,T01_FS_PIN_PUK_SAP_NO,T01_FS_VAP_SAP_NO,T_BOM_CB_QUANTITY,T01_FS_WRAPPING_SAP_NO,T01_FS_PACKAGING_SAP_NO,T_RAW_CHIP_RESTR,T01_FS_PUNCH_SHAPE,T_CUSTOMER,TO_VBAP_KWMENG,T_MILLING,T_PLUG_IN,T_RAW_IM_CARD_RESTR,T01_CARDBODY_MATERIAL,T_PRINTED_IM_CARD_RESTR,T01_FS_CATALOG_SAP_NO,T01_FINE_SPEC_ID]
t=0

for line in f:
    line=line.split('\t')
    try:
        order0=line[10]+'-'+line[12][-3:-1]
        #print (line[12][-3:-1])
        #input('abc')

    
        if line[2]=='T_BOM_CB_QUANTITY':
            if order0!=t:
                order.append(order0)
                t=order0
            T_BOM_CB_QUANTITY[order0]=line[6].replace(',','')
        if line[2]=='T_MILLING':
            if order0!=t:
                order.append(order0)
                t=order0
            T_MILLING[order0]=line[6]


        if line[2]=='T_CHIP_RESTR':
            if order0!=t:
                order.append(order0)
                t=order0
            T_CHIP_RESTR[order0]=line[6]
        if line[2]=='T_OCA_CARD1':
            if order0!=t:
                order.append(order0)
                t=order0
            T_OCA_CARD1[order0]=line[6]
        if line[2]=='T_ECA_PERS':
            if order0!=t:
                order.append(order0)
                t=order0
            T_ECA_PERS[order0]=line[6]
        if line[2]=='T_ATR_CHECK':
            if order0!=t:
                order.append(order0)
                t=order0
            T_ATR_CHECK[order0]=line[6]
        if line[2]=='T01_MANUAL_INSPECTION':
            if order0!=t:
                order.append(order0)
                t=order0
            T01_MANUAL_INSPECTION[order0]=line[6]
        if line[2]=='T01_FS_PIN_PUK_SAP_NO':
            if order0!=t:
                order.append(order0)
                t=order0
            T01_FS_PIN_PUK_SAP_NO[order0]=line[6]
        if line[2]=='T01_FS_VAP_SAP_NO':
            if order0!=t:
                order.append(order0)
                t=order0
            T01_FS_VAP_SAP_NO[order0]=line[6]
        if line[2]=='T01_FS_WRAPPING_SAP_NO':
            if order0!=t:
                order.append(order0)
                t=order0
            T01_FS_WRAPPING_SAP_NO[order0]=line[6]
        if line[2]=='T01_FS_PACKAGING_SAP_NO':
            if order0!=t:
                order.append(order0)
                t=order0
            T01_FS_PACKAGING_SAP_NO[order0]=line[6]


















        if line[2]=='T_CUSTOMER':
            if order0!=t:
                order.append(order0)
                t=order0
            T_CUSTOMER[order0]=line[6]
        if line[2]=='T01_FS_PUNCH_SHAPE':
            if order0!=t:
                order.append(order0)
                t=order0
            T01_FS_PUNCH_SHAPE[order0]=line[6]
        if line[2]=='T_RAW_CHIP_RESTR':
            if order0!=t:
                order.append(order0)
                t=order0
            T_RAW_CHIP_RESTR[order0]=line[6]
            
        if line[2]=='TO_VBAP_KWMENG':
            if order0!=t:
                order.append(order0)
                t=order0
            TO_VBAP_KWMENG[order0]=line[6].replace(',','')
               
            #print (line)
        if line[2]=='T_PLUG_IN':
            if order0!=t:
                order.append(order0)
                t=order0
            T_PLUG_IN[order0]=line[6]
               
            #print (line)
        if line[2]=='T_RAW_IM_CARD_RESTR':
            if order0!=t:
                order.append(order0)
                t=order0
            T_RAW_IM_CARD_RESTR[order0]=line[6]
               
            #print (line)
        if line[2]=='T01_CARDBODY_MATERIAL':
            if order0!=t:
                order.append(order0)
                t=order0
            T01_CARDBODY_MATERIAL[order0]=line[6]
               
            #print (line)
        if line[2]=='T_PRINTED_IM_CARD_RESTR':
            if order0!=t:
                order.append(order0)
                t=order0
            T_PRINTED_IM_CARD_RESTR[order0]=line[6]
               
            #print (line)
        if line[2]=='T01_FS_CATALOG_SAP_NO':
            if order0!=t:
                order.append(order0)
                t=order0
            T01_FS_CATALOG_SAP_NO[order0]=line[6]
               
            #print (line)
        if line[2]=='T01_FINE_SPEC_ID':
            if order0!=t:
                order.append(order0)
                t=order0
            T01_FINE_SPEC_ID[order0]=line[6]
    except:
        pass

        #print (line)
#print (order)

for i in order:
    for x in list1:
        try:
            x[i]
        except:
            x[i]=''
    #print (i,T01_FINE_SPEC_ID[i],T01_FS_CATALOG_SAP_NO[i],T_PRINTED_IM_CARD_RESTR[i],T01_CARDBODY_MATERIAL[i],T_RAW_IM_CARD_RESTR[i],T_MILLING[i],T_PLUG_IN[i])
    f0.write(i+','+TO_VBAP_KWMENG[i]+','+T_CUSTOMER[i]+','+T01_FINE_SPEC_ID[i]+','+T01_FS_CATALOG_SAP_NO[i]+','\
             +T_PRINTED_IM_CARD_RESTR[i]+','+T_RAW_IM_CARD_RESTR[i]+','+T01_CARDBODY_MATERIAL[i]+','+T_MILLING[i]+','+T_PLUG_IN[i]+','+\
             T01_FS_PUNCH_SHAPE[i]+','+T_RAW_CHIP_RESTR[i]+','+T_CHIP_RESTR[i]+','+T_OCA_CARD1[i]+','+T_ECA_PERS[i]+','+T_ATR_CHECK[i]+','+T01_MANUAL_INSPECTION[i]+','+\
             T01_FS_PIN_PUK_SAP_NO[i]+','+T01_FS_VAP_SAP_NO[i]+','+T_BOM_CB_QUANTITY[i]+','+T01_FS_WRAPPING_SAP_NO[i]+','+T01_FS_PACKAGING_SAP_NO[i]+'\n')
f0.close()
f.close()
os.system('explorer.exe '+date1+'.csv')
time.sleep(2)
os.remove(date1+'.csv')
print ('done')

##for i in order:
##    try:
##        T_PLUG_IN[i]
##    except:
##        T_PLUG_IN[i]=''
##for i in order:
##    try:
##        T_MILLING[i]
##    except:
##        T_MILLING[i]=''
##for i in order:
##    try:
##        T_MILLING[i]
##    except:
##        T_MILLING[i]=''
##for i in order:
##    try:
##        T_MILLING[i]
##    except:
##        T_MILLING[i]=''
##for i in order:
##    try:
##        T_MILLING[i]
##    except:
##        T_MILLING[i]=''
##for i in order:
##    try:
##        T_MILLING[i]
##    except:
##        T_MILLING[i]=''

         # ,T_PLUG_IN[i],T_RAW_IM_CARD_RESTR[i],T01_CARDBODY_MATERIAL[i],\
         # T_PRINTED_IM_CARD_RESTR[i],T01_FS_CATALOG_SAP_NO[i],T01_FINE_SPEC_ID[i])

    #print (line.split('\t'))
