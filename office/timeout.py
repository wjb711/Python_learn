#windows可用的限时timeout函数
from multiprocessing import Process
import time
 
def do_actions():
    """
    Function that should timeout after 5 seconds. It simply prints a number and waits 1 second.
    :return:
    """
    #print(q)
    #print(y)
    i = 0
    while True:
        i += 1
        print(i)
        time.sleep(1)
#超时函数，第一项为时间秒数，第二项为被限时函数名，第三项为被限时函数的内部参数
def timeout(s,func,*args):
    from multiprocessing import Process
    import time
    l0=[]
    for x in args:
        print('x:',x)
        l0.append(x)
        

    action_process = Process(target=func,args=l0)

    print(l0)

    action_process.start()
    action_process.join(timeout=s)
 

    action_process.terminate()
    print("Hey there! I timed out! You can do things after me!")

if __name__ == '__main__':

    timeout(10,do_actions)
