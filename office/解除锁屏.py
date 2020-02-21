#原理较简单，每两分钟模拟人工手动按两下alt， 让计算机误以为是人在操作， 防止5分钟的定时锁屏
import pyautogui,time,datetime
while True:
    time.sleep(120)
    pyautogui.hotkey('alt')
    pyautogui.hotkey('alt')
    now=datetime.datetime.now()
    print(now)
