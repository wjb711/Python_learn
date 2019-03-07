import mmap
import contextlib

from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view
from xml.dom import minidom
from xml.dom import Node
import datetime
import sys



def MyFun(today,level,folder):
    EvtxPath = "c:/windows/System32/Winevt/Logs/System.evtx" #日志文件的路径

    with open(EvtxPath,'r') as f:
        with contextlib.closing(mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)) as buf:
            fh = FileHeader(buf,0)
			# 构建一个xml文件，根元素是Events
            print ("")
            print ("")
			# 遍历事件
            for xml, record in evtx_file_xml_view(fh):
                
                #print(xml)
                #dom = xml.dom.minidom.parse(xml)
                xmldoc = minidom.parseString(xml)
                root=xmldoc.documentElement
                #print(root.nodeName)
                #print(root.nodeValue)
                Provider = root.getElementsByTagName('Provider')[0].getAttribute("Name")
                TimeCreated=root.getElementsByTagName('TimeCreated')[0].getAttribute("SystemTime")
                EventID = root.getElementsByTagName('EventID')[0].firstChild.data
                Computer=root.getElementsByTagName('Computer')[0].firstChild.data
                Level=root.getElementsByTagName('Level')[0].firstChild.data
                #t0 = root.getElementsByTagName('Keywords')
                #Provider0=Provider[0]
                if today in TimeCreated and Level==level:
                    print (TimeCreated[:19],Computer,Provider,Level,EventID)
                    with open(folder+'/'+today+'.log','a') as f:
                        f.write(TimeCreated[:19]+":"+Computer+":"+Provider+":"+Level+":"+EventID+'\n')
                else:
                    #print (TimeCreated)
                    pass
##                value=item.firstChild.data
##                if value=="2":
##                    print(xml)
##                    #print(t0[0].firstChild.data)
##                    a=input('a')
##                else:
##                    pass


if __name__ == '__main__':
    level=sys.argv[1]
    folder=sys.argv[2]
    today=datetime.datetime.now().strftime("%Y-%m-%d")
    #print(today)
    MyFun(today,level,folder)
