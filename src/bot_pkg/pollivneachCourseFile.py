"""pollivneachCourseFile.py - ..."""

from . import basic_functions
import pyautogui
from tkinter import *
import random
import keyboard

currentPhase = "Base"
markOfGrace = False
wait_color = 0
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
    basic_functions.up_orient()


def pollinveachCourse(current_phase, logger):
    global markOfGrace
    global waiting
    global currentPhase
    global wait_color
    global defaultAttempts
    global log_handle
    log_handle = logger

    currentPhase = current_phase

    reset_timer = 25
    basic_functions.finish_orient()

    if currentPhase == "Base":
        if not waiting:
            basic_functions.up_orient()
            print("Moving towards agility course")
            log_handle.send_info(["Moving towards agility course", 'success'])
            pyautogui.moveTo(1000 + random.randint(-8, 8),
                             45 + random.randint(-8, 8))
            defaultAttempts = 0
            pyautogui.click()
            pyautogui.moveTo(500, 500)
            waiting = True
        elif waiting and defaultAttempts < 30:
            moved, wait_color = basic_functions.is_moving(wait_color)
            if moved:
                defaultAttempts = 0
            else:
                basic_functions.up_orient()
                defaultAttempts += 1
                print("Waiting..." + str(defaultAttempts))
        elif waiting and defaultAttempts > 29:
            currentPhase = "Barrel"
            defaultAttempts = 0

    elif currentPhase == "Barrel":
        if basic_functions.check_default("Barrel"):
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
        if basic_functions.check_default("Mark of Grace"):
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
        if basic_functions.check_default("Market Stall"):
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
        if basic_functions.check_default("Banner"):
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
        if basic_functions.check_default("Leap Gap"):
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
        if basic_functions.check_default("TreeOne"):
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
        if basic_functions.check_default("Rough Wall"):
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
        if basic_functions.check_default("Monkeybars"):
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
        if basic_functions.check_default("TreeTwo"):
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
        if basic_functions.check_default("Drying Line"):
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
