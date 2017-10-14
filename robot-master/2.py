#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 aibot.me, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: util_voice.py
Author: darrenwang(darrenwang@aibot.me)
Date: 2017/03/24 11:29:50
Brief: 
"""

import sys
import json
import time
import base64
import urllib
import urllib2
import requests


class BaiduRest:
    def __init__(self, cu_id, api_key, api_secert):
        self.token_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
        self.getvoice_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
        self.upvoice_url = 'http://vop.baidu.com/server_api'

        self.cu_id = cu_id
        self.get_token(api_key, api_secert)
        return
    
    
    def get_token(self, api_key, api_secert):
        token_url = self.token_url % (api_key,api_secert)
        r_str = urllib2.urlopen(token_url).read()
        token_data = json.loads(r_str)
        self.token_str = token_data['access_token']
        return True
    
    #语音合成
    def text2audio(self, text, filename):
        get_url = self.getvoice_url % (urllib2.quote(text), self.cu_id, self.token_str)
        voice_data = urllib2.urlopen(get_url).read()
        voice_fp = open(filename,'wb+')
        voice_fp.write(voice_data)
        voice_fp.close()
        return True
    
    
    ##语音识别
    def audio2text(self, filename):
        data = {}
        data['format'] = 'wav'
        data['rate'] = 8000
        data['channel'] = 1
        data['cuid'] = self.cu_id
        data['token'] = self.token_str

        wav_fp = open(filename,'rb')
        voice_data = wav_fp.read()
        data['len'] = len(voice_data)
        #data['speech'] = base64.b64encode(voice_data).decode('utf-8')
        data['speech'] = base64.b64encode(voice_data).replace('\n', '')
        #post_data = json.dumps(data)
        result = requests.post(self.upvoice_url, json=data, headers={'Content-Type': 'application/json'})
        data_result = result.json()
        print data_result
        return data_result['result'][0]



def test_voice():
    api_key = "SrhYKqzl3SE1URnAEuZ0FKdT" 
    api_secert = "hGqeCkaMPb0ELMqtRGc2VjWdmjo7T89d"
    bdr = BaiduRest("test_python", api_key, api_secert)
    
    #生成
    start = time.time()
    bdr.text2audio("你好啊", "out.wav")
    using = time.time() - start
    print using


    #识别
    start = time.time()
    result = bdr.audio2text("test.wav")
    #result = bdr.audio2text("weather.pcm")
    using = time.time() - start
    print using, result

    return True



if __name__ == "__main__":
    test_voice()
