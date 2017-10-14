'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
'''
from datetime import *  
import time  
now = date(2012,9,17)
now0=date(2012,1,1)
print ('now.year:',now.year)  
print ('now.month:',now.month)  
print ('now.day:',now.day)
print (now-now0)
#date.replace(year, month,
