import cv2
import numpy as np
import pyautogui
import keyboard
from pynput.mouse import Controller as Controller
from pynput.mouse import Button
import time
import tkinter as tk
import random
from win32gui import GetWindowText, GetForegroundWindow
from tkinter import *

print("SevenA Minecraft HackingTool")
TriggerBot_Status = False
AntiAfk_Status = False
Enabled = True

def AntiAfk_Move():
    mouse = Controller()
    a = random.randint(5,15)
    afk = random.randint(0,100)
    if afk < 25:
        keyboard.press("w")
        time.sleep(0.1)
        keyboard.release("w")
    elif afk < 50:
        keyboard.press("a")
        time.sleep(0.1)
        keyboard.release("a")
    elif afk < 75:
        keyboard.press("s")
        time.sleep(0.1)
        keyboard.release("s")
    else:
        keyboard.press("d")
        time.sleep(0.1)
        keyboard.release("d")
    pyautogui.dragTo(1200, 540, button='left', duration=0.5)
    print('AntiAFK: Otomatik Hareket Edildi')
    time.sleep(a)

window = Tk()

window.title("SevenA")
w = 250
h = 350

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.configure(background="#010221")


lbl = Label(window, bg="#010221", fg="#07aaaf", font=5, text="AntiAFK", padx = 30, pady = 10)

lbl.grid(column=0, row=0)

lbl2 = Label(window, bg="#010221", fg="#07aaaf", font=5, text="Devre Dışı")

def AntiAFK_ChangeStatus():
    global AntiAfk_Status
    if AntiAfk_Status == True:
        lbl2.configure(text= "Devre Dışı")
        AntiAfk_Status = False
        print("AntifAFK Devre Dışı")
    else:
        lbl2.configure(text= "Aktif")
        AntiAfk_Status = True
        print("AntiAFK Aktif")

lbl2.grid(column=1, row=0)

btn = Button(window, bg="#010221", fg="#07aaaf", text="Tıkla", command=AntiAFK_ChangeStatus)

btn.grid(column=0, row=1)

#---------------------------------------------------


lbl3 = Label(window, bg="#010221", fg="#07aaaf", font=5, text="TriggerBot", padx = 30, pady = 10)

lbl3.grid(column=0, row=3)

lbl4 = Label(window, bg="#010221", fg="#07aaaf", font=5, text="Devre Dışı")

def TriggerBot_ChangeStatus():
    global TriggerBot_Status
    if TriggerBot_Status == True:
        lbl4.configure(text= "Devre Dışı")
        TriggerBot_Status = False
        print("TriggerBot Devre Dışı")
    else:
        lbl4.configure(text= "Aktif")
        TriggerBot_Status = True
        print("TriggerBot Aktif")

lbl4.grid(column=1, row=3)

btn2 = Button(window, bg="#010221", fg="#07aaaf", text="Tıkla", command=TriggerBot_ChangeStatus)

btn2.grid(column=0, row=4)

#---------------------------------------------------

def looping():
    if keyboard.is_pressed('k'):
        TriggerBot_ChangeStatus()
        time.sleep(1.05)
        
    window.after(100, looping)
    current_window = (GetWindowText(GetForegroundWindow()))
    if current_window.find("Minecraft") != -1:
        if TriggerBot_Status == True:
            img = pyautogui.screenshot(region=(958, 538, 2, 2))
            img = np.array(img)
            frame = np.array(img).sum()
            if frame == 940 or frame == 528 or frame == 260 or frame == 504 or frame == 518 or frame == 520 or frame == 488 or frame == 868 or frame == 1008 or frame == 328 or frame == 220 or frame == 468 or frame == 580 or frame == 588 or frame == 772 or frame == 384 or frame == 828 or frame == 760 or frame == 380 or frame == 796 or frame == 500 or frame == 496 or frame == 804 or frame == 672 or frame == 668 or frame == 590 or frame == 262 or frame == 636 or frame == 508 or frame == 572 or frame == 692 or frame == 816 or frame == 784:
                pyautogui.click()
                time.sleep(0.45)
                print('TriggerBot: Vuruş Yapıldı')
            #print('colorValue: ' + str(frame))
        elif AntiAfk_Status == True:
            AntiAfk_Move()

window.after(100, looping)
window.mainloop()


