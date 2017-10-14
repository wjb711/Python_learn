#coding=utf-8
import recorder
import wave
import urllib2
import pycurl
import json
import re
import turing
import tts
def get_token():
    apiKey = "wxNGGTpSQTKYjROe5gpgBKDO"
    secretKey = "f4a44a0f4c5d12173c34e5b258ef1f98"

    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;

    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']
global ask
def dump_res(buf):
    global ask
    buf=str(buf)
    pattern = re.compile(r'\["(.*?)"\]')
    item = re.findall(pattern, buf)
    if item:
        print u'我'
        print item[0].decode('utf-8')
        ask=item[0]
    else:
        ask='None'


def use_cloud(token):
    fp = wave.open('output.wav','r')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)

    cuid = "123456" #my xiaomi phone MAC
    srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
    http_header = [
        'Content-Type: audio/pcm; rate=8000',
        'Content-Length: %d' % f_len
    ]
    print srv_url
    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url)) #curl doesn't support unicode
    c.setopt(c.HTTPHEADER, http_header)   #must be list, not dict
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, dump_res)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform()

if __name__ == "__main__":
    token = get_token()
    while True:
        #raw_input()
        isOk=recorder.recorder()
        if isOk:
            use_cloud(token)
            global ask
            if ask.find('None')!=0:
                ans=turing.turing('12345',ask)
                print u'机器人'
                print ans
                tts.speak(ans)
