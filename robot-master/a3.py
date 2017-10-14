#-*- coding: utf-8 -*-
import base64, requests
d = open('testxf.pcm', 'rb').read()
data = {
    "format": "pcm",
    # "format": "wav",
    "rate": 16000,
    "channel": 1,
    "token": "your token",
    "cuid": "your mac",
    "len": len(d),
    "speech": base64.encodestring(d).replace('\n', '')
}
result = requests.post('http://vop.baidu.com/server_api', json=data, headers={'Content-Type': 'application/json'})
data_result = result.json()
print data_result['err_msg']
if data_result['err_msg']=='success.':
    print "语音结果：" + data_result['result'][0].encode('utf-8')
else:
    print data_result
