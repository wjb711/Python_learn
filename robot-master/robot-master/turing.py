# -*- coding: utf-8 -*-
import urllib
import json


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def textinfo(dict):
    return dict['text']
def linkinfo(dict):
    return dict['text']+'\n'+dict['url']
def newinfo(dict):
    text = ''
    text= text + dict['text']+'\n'
    for newdict in dict['list']:
        text = text + newdict['article']+'\n'
        text = text + newdict['source']+'\n'
        text = text + newdict['detailurl']+'\n'
        text = text+'-----------------------\n'
    return text

def cookinfo(dict):
    text = ''
    text= text + dict['text']
    cookdict = dict['list']
    text = text + cookdict[0]['name']+'\n'
    text = text + cookdict[0]['icon']+'\n'
    text = text + cookdict[0]['info']+'\n'
    text = text + cookdict[0]['detailurl']+'\n'
    text = text+'-----------------------\n'
    return text

def turing(id,info):
    key = '29ccde937cd544afbd45667b4be9805e'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&userid='+id+'&info='
    request = api + info
    response = getHtml(request)
    dic_json = json.loads(response)
    code=int(dic_json['code'])
    if code==100000:
        return textinfo(dic_json)
    elif code==200000:
        return linkinfo(dic_json)
    elif code==302000:
        return newinfo(dic_json)
    elif code==308000:
        return cookinfo(dic_json)
