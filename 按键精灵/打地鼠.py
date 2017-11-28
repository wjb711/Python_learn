##打地鼠外挂
##网页地址http://www.3366.com/flash/86840.shtml
import time
import pyautogui as p
from pyautogui import typewrite as w
from pyautogui import hotkey as h
while True:
    button7location = p.locateOnScreen('1.png')
    #print (button7location)
    try:
        button7x, button7y = p.center(button7location)
        p.click(button7x, button7y)
    except:
        pass
