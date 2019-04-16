#爬取基金网上的赎回费率
from pyquery import PyQuery as pq
#d = pq(url='http://fundf10.eastmoney.com/jjfl_519929.html',encoding="utf-8")

#print(d(".w650.comm.jjfl ").eq(2).find('td').eq(5))
with open('b0.txt','r') as f:
    x0=f.readlines()
for x in x0:
    x=x.replace('\n','')
    
    #print ('http://fundf10.eastmoney.com/jjfl_'+x+'.html')
    try:
        #print ('http://fundf10.eastmoney.com/jjfl_'+x+'.html')
        d = pq(url='http://fundf10.eastmoney.com/jjfl_'+x+'.html',encoding="utf-8")
        print(x, d('title').text()[:8], d(".w650.comm.jjfl ").eq(2).find('td').eq(5))
    except:
        pass
