from tkinter import *
import ntplib
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import pyperclip
from threading import Thread
import keyboard
import threading
import os
import webbrowser
import ctypes
import ctypes  # An included library with Python install.
import os
from path_config import inc

log_handle = None


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def setAngle():
    click(911, 49)  # navigation
    time.sleep(1)

    win32api.SetCursorPos((683, 382))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
    time.sleep(0.2)
    win32api.SetCursorPos((433, 382))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0)

    time.sleep(2)
    win32api.mouse_event(0x0800, 0, 0, -800, 0)
    time.sleep(1)
    win32api.mouse_event(0x0800, 0, 0, -600, 0)
    time.sleep(1)
    win32api.mouse_event(0x0800, 0, 0, -600, 0)

    time.sleep(1)

    win32api.SetCursorPos((683, 382))  # middle
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
    time.sleep(0.2)
    win32api.SetCursorPos((683, 482))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0)

    time.sleep(2.5)


def RightClick(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


def LayFunction():
    time.sleep(2)
    i = 0
    while True:
        if i != 5:
            path = os.path.join(inc, 'lay.png')
            laybutonu = pyautogui.locateOnScreen(
                path, confidence=0.8, grayscale=False)
            if laybutonu != None:
                layx, layy = pyautogui.center(laybutonu)
                time.sleep(0.5)
                click(layx, layy)
                time.sleep(0.1)
                click(layx, layy)
                i = i + 1
            time.sleep(2.8)

        else:
            print("lay Bitti")
            log_handle.send_info(["Lay bitti", 'error'])
            time.sleep(1.5)
            break


def GreenFunction():
    while True:
        path = os.path.join(inc, 'red.png')
        aramabutonured = pyautogui.locateOnScreen(
            path, confidence=0.65, grayscale=False)

        if aramabutonured != None:
            redx, redy = pyautogui.center(aramabutonured)
            time.sleep(1)
            RightClick(redx - 1, redy - 1)

            time.sleep(0.8)
            path = os.path.join(inc, 'reset2.png')
            resetButonu = pyautogui.locateOnScreen(
                path, confidence=0.88, grayscale=False)
            if resetButonu != None:
                resetx, resety = pyautogui.center(resetButonu)
                time.sleep(0.5)
                click(resetx, resety)
            else:
                win32api.SetCursorPos((korx, kory - 70))
        path = os.path.join(inc, 'green.png')
        aramabutonu = pyautogui.locateOnScreen(
            path, confidence=0.65, grayscale=False)
        if aramabutonu != None:
            korx, kory = pyautogui.center(aramabutonu)
            time.sleep(1)
            RightClick(korx - 1, kory - 1)

            time.sleep(0.8)
            path = os.path.join(inc, 'reset.png')
            resetButonu = pyautogui.locateOnScreen(
                path, confidence=0.88, grayscale=False)
            if resetButonu != None:
                resetx, resety = pyautogui.center(resetButonu)
                time.sleep(0.5)
                click(resetx, resety)
            else:
                win32api.SetCursorPos((korx, kory - 70))
            time.sleep(3)
        else:
            print("Green Circle is not Found")
            log_handle.send_info(["Green Circle is not Found", 'error'])
        time.sleep(0.5)


def start(setup, logger):
    global log_handle
    log_handle = logger
    if not setup:
        setAngle()
        LayFunction()

    GreenFunction()

# pencere = Tk()

# pencere.title("Runescape BOT")
# pencere.geometry("160x190")
# pencere.configure(background='black')
# pencere.attributes('-topmost', True)
# uygulama = Frame(pencere)
# uygulama.grid()


# button ekleme bölümü


# button1 = Button(uygulama, text = " START " , width=20,height=5, command=lambda:start(),fg = "red" ,bg="black")
# button1.grid(padx=3, pady=3)


# pencere.mainloop()
