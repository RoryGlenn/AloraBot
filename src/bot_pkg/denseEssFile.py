import os
import random

import keyboard
import pyautogui
from path_config import RES_1366
from pynput.mouse import Controller

from . import basicFunctions
from .basicFunctions import checkDefault, grabColor

# import tkinter
# import PIL
# from tkinter import *

"""

.. = go back one folder
. = look at the folder we are currently in

For example,
cd .. will take you back one folder
cd . will do nothing

"""

# print(f"res_1366: {res_1366}") # res_1366: C:\Users\justy\Desktop\alora 3.0\src\data\1366x768

mouse = Controller()

currentPhase = "Base"
secondsMining = 140

bankExitPic = os.path.join(RES_1366, 'settings.PNG')
pickaxeChiselPic = os.path.join(RES_1366, 'Pickaxe Chisel2.PNG')
locationPic = os.path.join(RES_1366, 'location.PNG')
waitColor = 0
log_handle = None

defaultAttempts = 0
waiting = False


def endProcess():
    global currentPhase
    global waiting
    global defaultAttempts
    currentPhase = "Teleport Home"
    waiting = False
    defaultAttempts = 0
    basicFunctions.downOrient()


def denseEssProcess(current_phase, waiting_, seconds_mining, logger):
    global waiting
    global currentPhase
    global waitColor
    global secondsMining
    global log_handle
    global defaultAttempts

    log_handle = logger
    secondsMining = seconds_mining
    # current_phase = current_phase
    # waiting = waiting_
    reset_timer = 25

    basicFunctions.finishOrient()

    if currentPhase == "Base":
        if not waiting and defaultAttempts < 40:
            # Check in the "expected" spot for ease of access, then process for methodical checking
            # print("Looking for mage")
            log_handle.send_info(['Looking for mage', 'success'])
            if basicFunctions.checkDefault("Mage"):
                print("Mage found!")
                log_handle.send_info(['Mage found', 'success'])
                pyautogui.click()
                waiting = True
                defaultAttempts = 0
                reset_timer = 3000
            else:
                defaultAttempts += 1
                if defaultAttempts > 39:
                    keyboard.press("left")
                    keyboard.release("left")
                    print("Desperately looking for mage")
                    log_handle.send_info(
                        ['Desperately looking for mage', 'error'])

        elif not waiting and 39 < defaultAttempts < 70:
            if basicFunctions.checkDefault("Mage"):
                log_handle.send_info(['Mage found', 'success'])
                pyautogui.click()
                waiting = True
                defaultAttempts = 0
                reset_timer = 3000
            else:
                defaultAttempts += 1
                keyboard.press("left")
                keyboard.release("left")

        elif not waiting and defaultAttempts > 69:
            endProcess()

        elif waiting:
            try:
                if defaultAttempts < 50:
                    location = pyautogui.locateOnScreen(locationPic)
                    locationPoint = pyautogui.center(location)
                    pyautogui.moveTo(
                        locationPoint.x + random.randint(-5, 5), locationPoint.y + random.randint(-5, 5))
                    pyautogui.click()
                    print("Warping!")
                    log_handle.send_info(['Warning!', 'error'])
                    currentPhase = "RockHop"
                    reset_timer = 4000
                    basicFunctions.downOrient()
                    waiting = False
                else:
                    endProcess()
            except:
                log_handle.send_info(['Looking for fast travel', 'success'])
                print("Looking for fast travel")
                defaultAttempts += 1

    elif currentPhase == "RockHop":
        if not waiting and defaultAttempts < 21:
            print("Looking for small rock")
            log_handle.send_info(['Looking for small rock', 'success'])
            waitColor = grabColor()
            if basicFunctions.checkDefault("Small Rock"):
                print("Small rock found!")
                log_handle.send_info(['Small rock found', 'success'])
                pyautogui.click()
                waiting = True
                defaultAttempts = 0
                reset_timer = 2000
            else:
                defaultAttempts += 1

        elif not waiting and 20 < defaultAttempts < 40:
            print("Desperately looking for small rock")
            log_handle.send_info(
                ['Desperately looking for small rock', 'error'])
            if checkDefault("Small Rock"):
                print("Small rock found!")
                log_handle.send_info(['Small rock found', 'success'])
                pyautogui.click()
                waiting = True
                defaultAttempts = 0
                reset_timer = 2000
            else:
                keyboard.press("left")
                keyboard.release("left")
                print("Time to reset.")
                log_handle.send_info(['Time to reset', 'error'])

                defaultAttempts += 1

        elif defaultAttempts > 39:
            endProcess()

        elif waiting:
            print("Waiting..." + str(defaultAttempts))
            log_handle.send_info(
                ["Waiting..." + str(defaultAttempts), 'error'])
            if grabColor() == waitColor:
                defaultAttempts += 1
            else:
                defaultAttempts = 0
                waitColor = grabColor()
            if defaultAttempts > 10:
                defaultAttempts = 0
                currentPhase = "MinesMap"
                waiting = False
                print("Clicking on map.")
                log_handle.send_info(['Clicking on map', 'success'])

    elif currentPhase == "MinesMap":
        if not waiting:
            waitColor = grabColor()
            pyautogui.moveTo(1014, 149)
            pyautogui.click()
            waiting = True
            pyautogui.moveTo(300, 300)
        else:
            print("Waiting..." + str(defaultAttempts))
            log_handle.send_info(
                ["Waiting..." + str(defaultAttempts), 'error'])
            if grabColor() == waitColor:
                defaultAttempts += 1
            else:
                defaultAttempts = 0
                waitColor = grabColor()
            if defaultAttempts > 10:
                currentPhase = "Large Rock"
                basicFunctions.downOrient()
                waiting = False
                defaultAttempts = 0
                print("Clicking on rock :)")
                log_handle.send_info(['Clicking on rock', 'success'])

    elif currentPhase == "Large Rock":

        if checkDefault("Large Rock") and defaultAttempts < 30:
            print("Mining")
            log_handle.send_info(['Mining', 'success'])
            pyautogui.click()
            defaultAttempts = 0
            currentPhase = "Teleport Home"
            reset_timer = (1000 * int(secondsMining))

        elif 29 < defaultAttempts < 50:
            if checkDefault("Large Rock"):
                print("Mining")
                log_handle.send_info(['Mining', 'success'])
                pyautogui.click()
                defaultAttempts = 0
                currentPhase = "Teleport Home"
                reset_timer = (1000 * int(secondsMining))
            else:
                defaultAttempts += 1

        elif defaultAttempts > 49:
            endProcess()

        else:
            defaultAttempts += 1
            if defaultAttempts > 29:
                keyboard.press("right")
                keyboard.release("right")
                print("Desperately looking for large rock")
                log_handle.send_info(
                    ["Desperately looking for large rock", 'error'])

    elif currentPhase == "Teleport Home":
        basicFunctions.downOrient()
        print("Teleporting Home...")
        log_handle.send_info(["Teleporting Home", 'success'])
        keyboard.write(";;home")
        keyboard.press("Enter")
        currentPhase = "Bank"
        reset_timer = 3000

    elif currentPhase == "Bank":
        if not waiting:
            if checkDefault("Bank") and defaultAttempts < 30:
                pyautogui.click()
                waiting = True
                defaultAttempts = 0
                print("Walking to bank...")
                log_handle.send_info(["Walking to bank...", 'success'])

            elif 30 < defaultAttempts < 60:
                if checkDefault("Bank"):
                    pyautogui.click()
                    waiting = True
                    defaultAttempts = 0
                    print("Walking to bank...")
                    log_handle.send_info(["Walking to bank...", 'success'])
                else:
                    defaultAttempts += 1
            elif defaultAttempts > 59:
                endProcess()

            else:
                defaultAttempts += 1
                if defaultAttempts > 29:
                    keyboard.press("left")
                    keyboard.release("left")
                    print("Desperately looking for bank")
                    log_handle.send_info(
                        ["Desperately looking for bank", 'error'])

        else:
            try:
                location = pyautogui.locateOnScreen(bankExitPic)
                location = pyautogui.center(location)
                print("found picture!")
                log_handle.send_info(["Found picture", 'success'])
                print(str(location.x) + ", " + str(location.y))
                currentPhase = "Deposit"
                waiting = False
                reset_timer = 3000
            except:
                print("Looking for deposit picture...")
                log_handle.send_info(
                    ["Looking for deposit picture...", 'error'])

    elif currentPhase == "Deposit":
        if not waiting:
            location = pyautogui.locateOnScreen(bankExitPic)
            location = pyautogui.center(location)
            pyautogui.moveTo(location.x + 5, location.y - 35)
            pyautogui.click()
            waiting = False
            currentPhase = "Base"
            basicFunctions.downOrient()
            defaultAttempts = 0

    return reset_timer
