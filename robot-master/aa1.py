import urllib.request
import json
from urllib.parse import quote
#http = urllib3.PoolManager()
myword='你会说话不'
url0='http://www.tuling123.com/openapi/api?key=29ccde937cd544afbd45667b4be9805e&userid=12345&info='+myword
url=('\n%s' % quote(url0, safe='/:&?='))
print (url)
fb=urllib.request.urlopen(url)
mybytes=fb.read()
mystr=mybytes.decode('utf8')
print (mystr)
