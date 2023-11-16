from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import winsound

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(random.uniform(random.uniform(.099, 0.1), random.uniform(.11, .12)))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


time.sleep(1)
while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('av4.png', region = (460,190,340,70), confidence=0.8) != None:

        if pyautogui.locateOnScreen('av.png', region = (790,200,160,200), confidence=0.8) != None:
            v3 = pyautogui.locateOnScreen('av.png', region = (790,200,160,200), confidence=0.8)
            c = pyautogui.center(v3)
            pyautogui.click(c)
            if pyautogui.locateOnScreen('al.png', region=(476, 323, 500, 300), confidence=0.8) != None:
                click(793,563)
            time.sleep(0.2)
            pic = pyautogui.screenshot(region = (778,259,161,372))
            for x in range(0,161,5):
                for y in range(0,372,5):
                    r,g,b = pic.getpixel((x,y))
                    if r == 113:
                        click(x+778,y+259)
            winsound.Beep(440,1000)


        if pyautogui.locateOnScreen('av3.png', region = (790,200,160,200), confidence=0.8) != None:
            v = pyautogui.locateOnScreen('av3.png', region = (790,200,160,200), confidence=0.8)
            a = pyautogui.center(v)
            pyautogui.click(a)
            if pyautogui.locateOnScreen('al.png', region=(476, 323, 500, 300), confidence=0.8) != None:
                click(793,563)
            time.sleep(0.2)
            pic = pyautogui.screenshot(region = (778,259,161,372))
            for x in range(0,161,5):
                for y in range(0,372,5):
                    r,g,b = pic.getpixel((x,y))
                    if r == 113:
                        click(x+778,y+259)
            winsound.Beep(440,1000)

        else:
            click(random.randint(900,915),random.randint(172,184))


