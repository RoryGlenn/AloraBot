from . import basicFunctions
import tkinter
import PIL
import pyautogui
from tkinter import *
import random
import keyboard
from pynput.mouse import Button, Controller

currentPhase = "Base"
markOfGrace = False
waitColor = 0;
defaultAttempts = 0
waiting = False
log_handle = None

def endProcess():
    global currentPhase
    global waiting
    global defaultAttempts

    currentPhase = "Teleport Home"
    waiting = False
    defaultAttempts = 0
    basicFunctions.upOrient()

def pollinveachCourse(current_phase, logger):
    global markOfGrace
    global waiting
    global currentPhase
    global waitColor
    global defaultAttempts
    global log_handle
    log_handle = logger

    currentPhase = current_phase

    reset_timer = 25
    basicFunctions.finishOrient()

    if currentPhase == "Base":
        if not waiting:
            basicFunctions.upOrient()
            print("Moving towards agility course")
            log_handle.send_info(["Moving towards agility course", 'success'])
            pyautogui.moveTo(1000 + random.randint(-8, 8), 45 + random.randint(-8, 8))
            defaultAttempts = 0
            pyautogui.click()
            pyautogui.moveTo(500, 500)
            waiting = True
        elif waiting and defaultAttempts < 30:
            moved, waitColor = basicFunctions.moving(waitColor)
            if moved:
                defaultAttempts = 0
            else:
                basicFunctions.upOrient()
                defaultAttempts += 1
                print("Waiting..." + str(defaultAttempts))
        elif waiting and defaultAttempts > 29:
            currentPhase = "Barrel"
            defaultAttempts = 0

    elif currentPhase == "Barrel":
        if basicFunctions.checkDefault("Barrel"):
            print("Barrel found!")
            log_handle.send_info(["Barrel found", 'success'])
            pyautogui.click()
            defaultAttempts = 0
            if not markOfGrace:
                currentPhase = "Market Stall"
            else:
                currentPhase = "Mark of Grace"
            reset_timer = 5000
        else:
            defaultAttempts += 1
            if defaultAttempts > 50:
                endProcess()

    elif currentPhase == "Mark of Grace":
        if basicFunctions.checkDefault("Mark of Grace"):
            print("Mark of grace found!")
            log_handle.send_info(["Mark of grace found!", 'success'])
            pyautogui.click()
            defaultAttempts = 0
            currentPhase = "Market Stall"
            reset_timer = 5000
        else:
            defaultAttempts += 1
            if defaultAttempts > 50:
                endProcess()

    elif currentPhase == "Market Stall":
        if basicFunctions.checkDefault("Market Stall"):
            markOfGrace = False
            print("Market stall found!")
            log_handle.send_info(["Market stall found!", 'success'])
            pyautogui.click()
            defaultAttempts = 0
            currentPhase = "Banner"
            reset_timer = 5000
        else:
            defaultAttempts += 1
            if defaultAttempts > 50:
                endProcess()

    elif currentPhase == "Banner":
        if basicFunctions.checkDefault("Banner"):
            print("Banner found!")
            log_handle.send_info(["Banner found!", 'success'])
            pyautogui.click()
            defaultAttempts = 0
            currentPhase = "Leap Gap"
            reset_timer = 5000
        else:
            defaultAttempts += 1
            if defaultAttempts > 50:
                endProcess()
    elif currentPhase == "Leap Gap":
        if basicFunctions.checkDefault("Leap Gap"):
            print("Gap found!")
            log_handle.send_info(["Gap found!", 'success'])
            pyautogui.click()
            defaultAttempts = 0
            currentPhase = "Tree One"
            reset_timer = 5000
        else:
            defaultAttempts += 1
            if defaultAttempts > 50:
                endProcess()
    elif currentPhase == "Tree One":
        if basicFunctions.checkDefault("TreeOne"):
            print("Tree found!")
            log_handle.send_info(["Tree found!", 'success'])
            pyautogui.click()
            defaultAttempts = 0
            currentPhase = "Rough Wall"
            reset_timer = 5000
        else:
            defaultAttempts += 1
            if defaultAttempts > 50:
                endProcess()
    elif currentPhase == "Rough Wall":
        if basicFunctions.checkDefault("Rough Wall"):
            print("Rough wall found!")
            log_handle.send_info(["Rough wall found!", 'success'])
            pyautogui.click()
            defaultAttempts = 0
            currentPhase = "Monkeybars"
            reset_timer = 5000
        else:
            defaultAttempts += 1
            if defaultAttempts > 50:
                endProcess()
    elif currentPhase == "Monkeybars":
        if basicFunctions.checkDefault("Monkeybars"):
            print("Monkeybars found!")
            log_handle.send_info(["Monkeybars found!", 'success'])
            pyautogui.click()
            defaultAttempts = 0
            currentPhase = "Tree Two"
            reset_timer = 5000
        else:
            defaultAttempts += 1
            if defaultAttempts > 50:
                endProcess()
    elif currentPhase == "Tree Two":
        if basicFunctions.checkDefault("TreeTwo"):
            print("Tree found!")
            log_handle.send_info(["Tree found!", 'success'])
            pyautogui.click()
            defaultAttempts = 0
            currentPhase = "Drying Line"
            reset_timer = 5000
        else:
            defaultAttempts += 1
            if defaultAttempts > 50:
                endProcess()
    elif currentPhase == "Drying Line":
        if basicFunctions.checkDefault("Drying Line"):
            print("Drying line found!")
            log_handle.send_info(["Drying line found!", 'success'])
            pyautogui.click()
            defaultAttempts = 0
            currentPhase = "Teleport Home"
            reset_timer = 5000
        else:
            defaultAttempts += 1
            if defaultAttempts > 50:
                endProcess()

    elif currentPhase == "Teleport Home":
        print("Teleporting Home...")
        log_handle.send_info(["Teleporting Home...", 'success'])
        keyboard.write(";;home")
        keyboard.press("Enter")
        currentPhase = "Base"
        reset_timer = 6000

    return reset_timer