from logging import root
import cv2
from tkinter import *
from PIL import ImageGrab, Image, ImageTk
import sys
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\minua\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
import pyautogui
import keyboard

def Snip_tool():
    #screenshot = pyautogui.screenshot()
    #img_array = np.array(screenshot)
    #image = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    #cv2.imshow('image', image)
    #print('screenshot taken')
    #img = ImageTk.PhotoImage(image=Image.fromarray(img_array))

    #root = Tk()
    #screen_width = root.winfo_screenwidth()
    #screen_height = root.winfo_screenheight()
    #root.geometry(f'{screen_width}x{screen_height}')
    #canvas = Canvas(root, width = screen_width, height = screen_height)
    #canvas.pack()
    #canvas.create_image(20, 20, anchor = 'nw', image = img)

    root = Tk()
    global n, coords
    n=0
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f'{screen_width}x{screen_height}')
    root.attributes("-alpha", 0.5)
    root.overrideredirect(True)
    canvas = Canvas(root, width = screen_width, height = screen_height)
    canvas.pack()

    x1=y1=coords=None

    def key_press(e):
        root.destroy()
    def key_release(e):
        root.destroy()

    root.bind('<Key>', key_press)
    root.bind('<KeyRelease>', key_release)

    def cur_press_event(event):
        global n,coords,a
        if n==0:
            n+=1
            coords=event.x,event.y
        elif n==1:
            n+=1
            a=canvas.create_rectangle(coords[0],coords[1],event.x,event.y, fill = 'purple')

        else:
            canvas.coords(a, coords[0] ,coords[1], event.x, event.y)

    def setn(event):
        global n,x1,y1,coords
        n=0
        x1,y1 = event.x, event.y
        if coords is not None:
            print(*coords)
            print(x1,y1)

            root.withdraw()

            img = ImageGrab.grab(bbox= (coords[0],coords[1],x1, y1))
            img_array = np.array(img)
            print(type(img_array))
            image = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

            win = cv2.namedWindow('Snip Window')
            cv2.imshow('Snip Window', image)
            cv2.createButton('Snip', Snip_tool, None, cv2.QT_PUSH_BUTTON,1)
        x1=y1=coords=None

    root.bind('<B1-Motion>', cur_press_event)
    root.bind('<ButtonRelease-1>',setn)