#文件服务器下载web
from flask import Flask,request,render_template,redirect

import os


#如果是文件，提供下载链接
#如果是文件夹，提供index目录链接
def template2(f,url):

    z=os.listdir(f)
    z.sort()
    #y=lambda x:'<li><a href=../%s/%s>%s</a></li>'%(f,x,x) if '.' in x else '<li><a href=/a?q=../%s/%s>%s</a></li>'%(f,x,x)

    #print(list(map(y,z)))
    list0=[]
    for z0 in z:
        #if '.' in z0:
        #    print('file:',f.replace('\\','/')+'/'+z0)
        if os.path.isfile(f.replace('\\','/')+'/'+z0):
            list0.append('<li><a href=../%s/%s>%s</a></li>'%(url,z0,z0))
        else:
            list0.append('<li><a href=/a?q=/../%s/%s>%s</a></li>'%(url,z0,z0))
    return str(f)+''.join(list0).replace('///','/').replace('//','/')


#自定义静态文件（下载目录）
app = Flask(__name__,static_folder='c:\cv')

@app.route('/',methods=['GET','POST'])

#需要给两个参数，第一个物理绝对路径app.static_folder，第二个网页相对路径app.static_url_path
def hello():
    global location
    global url
    location=app.static_folder
    url=app.static_url_path
    #global location
    #global url
    print(location,app.static_url_path)
    return template2(location,url)


#目录查询写法
@app.route('/a',methods=['GET','POST'])

def a():
    x0=request.args.get("q")
    if '.' not in x0:
        z=os.listdir(location+x0)
    return template2(location+x0,url+x0)


if __name__ == '__main__':



    app.run(host='0.0.0.0',port=5001,debug=True)
