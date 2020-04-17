from fastapi import FastAPI

from starlette.responses import HTMLResponse

from pydantic import BaseModel

from jinja2 import Template

import json




html_2='''
<html>



<frameset cols="50%,50%">



  <frame src="{{ link1 }}" />

  <frame src="{{ link2 }}" />





</frameset>



</html>
'''



html_4='''
<html>



<frameset cols="50%,50%">

  <frameset rows="50%,50%">


   <frame src="{{ link1 }}" />

   <frame src="{{ link2 }}" />

 </frameset>

   <frameset rows="50%,50%">


   <frame src="{{ link3 }}" />

   <frame src="{{ link4 }}" />

</frameset>
</frameset>


</html>
'''









html_6='''

<html>



<frameset cols="33%,33%,33%">

<frameset rows="50%,50%">

  <frame src="{{ link1 }}" />

  <frame src="{{ link2 }}" />



</frameset>

<frameset rows="50%,50%">

  <frame src="{{ link3 }}" />

  <frame src="{{ link4 }}" />



</frameset>

<frameset rows="50%,50%">

  <frame src="{{ link5 }}" />

  <frame src="{{ link6 }}" />



</frameset>



</frameset>



</html>

'''

html_name='''

<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<title>分屏展板</title>

</head>


<body>



<form action="/names/links">
<h1 style="text-align:center">


<br></br>


请输入表名: <input type="text" name="name1">


<input type="submit" value="提交">

</form></h1>



<h1 style="text-align:center">分屏展示系统，请输入如户名或表名。</h1>



</body>

</html>

'''

html='''

<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<title>分屏展示</title>

</head>

<body>



<form action="/items/links">

<h1 style="text-align:center" name="username" value={{ name1 }}> {{ name1 }}</h1>



link1(必须以http://或https://开头): <input type="text" name="link1" value={{ link1 }} ><br>

link2(必须以http://或https://开头): <input type="text" name="link2" value={{ link2 }} ><br>

link3(必须以http://或https://开头): <input type="text" name="link3" value={{ link3 }} ><br>

link4(必须以http://或https://开头): <input type="text" name="link4" value={{ link4 }} ><br>

link5(必须以http://或https://开头): <input type="text" name="link5" value={{ link5 }} ><br>

link6(必须以http://或https://开头): <input type="text" name="link6" value={{ link6 }} ><br>

<input type="submit" value="提交">

</form>







</body>

</html>

'''



app = FastAPI()







@app.get("/")

def read_root():

    return HTMLResponse(html_name)



@app.get("/names/{item_id}")

def read_name(item_id: str, name1: str = None):

    name1=name1

    try:

        with open(name1+'.json','r') as f:

            data = json.load(f)

    except:

        data={}

        data[name1]=['','','','','','']





    print(data,type(data))



    print('************')

    link1=data[name1][0]

    link2=data[name1][1]

    link3=data[name1][2]

    link4=data[name1][3]

    link5=data[name1][4]

    link6=data[name1][5]

    print(name1,link1, link2)
    for z in data[name1]:
        if z=='':
            z='about:blank'
        elif z[0]!='h':
            z='http://'+z

    print('here:888888888888888888',link1,link2,link3,link4,link5,link6)
    return HTMLResponse(Template(html).render(name1=name1,link1=link1,link2=link2,link3=link3,link4=link4,link5=link5,link6=link6))





@app.get("/items/{item_id}")

def read_item(item_id: str, link1: str = None,link2: str = None,link3: str = None,link4: str = None,link5: str = None,link6: str = None,username: str = None):

    list0=[link1,link2,link3,link4,link5,link6]
    list1=[]
    for y in list0:
        if y =='':
            y='about:blank'
        elif y is None:
            break
        elif y[0]!='h':
            y='http://'+y
        list1.append(y)
#    for item in list0:
#       list1.append(item)
    link1,link2,link3,link4,link5,link6=list1




#    x={}

#    x[username]=[link1,link2,link3,link4,link5,link6]


#    print("x:",x)

#    print(username,link1,link2)

    #dict = {'a': 'wo', 'b': 'zai', 'c': 'zhe', 'd': 'li'}

#    string = json.dumps(x)

#    with open(str(username)+'.json','w')as f:

#        f.write(string)



#    return {"item_id": item_id, "link1": link1,"link2":link2,"link3":link3,"link4":link4,"link5":link5,"link6":link6,'name1':username}
    #d=input('d:')
    if link3=='about:blank':
        return HTMLResponse(Template(html_2).render(link1=link1,link2=link2))
    elif link5=='about:blank':
        return HTMLResponse(Template(html_4).render(link1=link1,link2=link2,link3=link3,link4=link4))
    return HTMLResponse(Template(html_6).render(link1=link1,link2=link2,link3=link3,link4=link4,link5=link5,link6=link6))
#    return HTMLResponse(Template(html_6).render(link1=link1,link2=link2))
    #return HTMLResponse(Template(html_6).render())
