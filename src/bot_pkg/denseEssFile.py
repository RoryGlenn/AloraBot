"""denseEssFile.py - ..."""

import os
import random

import keyboard
import pyautogui

from path_config import RES_1366

from pynput.mouse import Controller
from .basic_functions import DefaultMouseMove, Orient, ObjName


DMM = DefaultMouseMove()
ORIENT = Orient()

mouse = Controller()

currentPhase = "Base"
secondsMining = 140

bankExitPic = os.path.join(RES_1366, 'settings.PNG')
pickaxeChiselPic = os.path.join(RES_1366, 'Pickaxe Chisel2.PNG')
locationPic = os.path.join(RES_1366, 'location.PNG')
wait_color = 0
log_handle = None

defaultAttempts = 0
waiting = False


class CurrentPhase:
    BASE = "Base"
    ROCK_HOP = "RockHop"
    MINES_MAP = "MinesMap"
    ROCK_LARGE = "Large Rock"
    HOME = "Teleport Home"
    BANK = "Bank"
    DEPOSIT = "Deposit"


def endProcess() -> None:
    global currentPhase
    global waiting
    global defaultAttempts
    currentPhase = "Teleport Home"
    waiting = False
    defaultAttempts = 0
    ORIENT.down_orient()


def base() -> int:
    global waiting
    global defaultAttempts
    global currentPhase
    global DMM

    reset_timer = 25

    if not waiting and defaultAttempts < 40:
        # Check in the "expected" spot for ease of access, then process for methodical checking
        log_handle.send_info(['Looking for mage', 'success'])
        if DMM.check_default_lookup(ObjName.MAGE):
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
        if DMM.check_default_lookup(ObjName.MAGE):
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
                pyautogui.moveTo(locationPoint.x + random.randint(-5, 5),
                                 locationPoint.y + random.randint(-5, 5))
                pyautogui.click()
                print("Warping!")
                log_handle.send_info(['Warning!', 'error'])
                currentPhase = "RockHop"
                reset_timer = 4000
                ORIENT.down_orient()
                waiting = False
            else:
                endProcess()
        except Exception as exception:
            log_handle.send_info(['Looking for fast travel', 'success'])
            print("Looking for fast travel")
            defaultAttempts += 1
    return reset_timer


def rock_hop() -> int:
    global waiting
    global defaultAttempts
    global currentPhase
    global wait_color

    reset_timer = 25

    if not waiting and defaultAttempts < 21:
        print("Looking for small rock")
        log_handle.send_info(['Looking for small rock', 'success'])
        wait_color = DMM.grab_color()
        if DMM.check_default_lookup(ObjName.ROCK_SMALL):
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
        if DMM.check_default_lookup(ObjName.ROCK_SMALL):
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
        if DMM.grab_color() == wait_color:
            defaultAttempts += 1
        else:
            defaultAttempts = 0
            wait_color = DMM.grab_color()
        if defaultAttempts > 10:
            defaultAttempts = 0
            currentPhase = "MinesMap"
            waiting = False
            print("Clicking on map.")
            log_handle.send_info(['Clicking on map', 'success'])
    return reset_timer


def mines_map() -> None:
    global currentPhase
    global waiting
    global defaultAttempts
    global wait_color

    if not waiting:
        wait_color = DMM.grab_color()
        pyautogui.moveTo(1014, 149)
        pyautogui.click()
        waiting = True
        pyautogui.moveTo(300, 300)
    else:
        print("Waiting..." + str(defaultAttempts))
        log_handle.send_info(
            ["Waiting..." + str(defaultAttempts), 'error'])
        if DMM.grab_color() == wait_color:
            defaultAttempts += 1
        else:
            defaultAttempts = 0
            wait_color = DMM.grab_color()
        if defaultAttempts > 10:
            currentPhase = "Large Rock"
            ORIENT.down_orient()
            waiting = False
            defaultAttempts = 0
            print("Clicking on rock :)")
            log_handle.send_info(['Clicking on rock', 'success'])


def rock_large() -> int:
    global currentPhase
    global defaultAttempts
    global secondsMining

    reset_timer = 25

    if DMM.check_default_lookup(ObjName.ROCK_LARGE) and defaultAttempts < 30:
        print("Mining")
        log_handle.send_info(['Mining', 'success'])
        pyautogui.click()
        defaultAttempts = 0
        currentPhase = "Teleport Home"
        reset_timer = (1000 * int(secondsMining))
    elif 29 < defaultAttempts < 50:
        if DMM.check_default_lookup(ObjName.ROCK_LARGE):
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
    return reset_timer


def teleport_home():
    global currentPhase
    ORIENT.down_orient()
    print("Teleporting Home...")
    log_handle.send_info(["Teleporting Home", 'success'])
    keyboard.write(";;home")
    keyboard.press("Enter")
    currentPhase = "Bank"
    reset_timer = 3000
    return reset_timer


def bank() -> int:
    global DMM
    global defaultAttempts
    global currentPhase
    global waiting

    reset_timer = 25

    if not waiting:
        if DMM.check_default_lookup(ObjName.BANK) and defaultAttempts < 30:
            pyautogui.click()
            waiting = True
            defaultAttempts = 0
            print("Walking to bank...")
            log_handle.send_info(["Walking to bank...", 'success'])
        elif 30 < defaultAttempts < 60:
            if DMM.check_default_lookup(ObjName.BANK):
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
            currentPhase = CurrentPhase.DEPOSIT
            waiting = False
            reset_timer = 3000
        except Exception as exception:
            print("Looking for deposit picture...")
            log_handle.send_info(
                ["Looking for deposit picture...", 'error'])
    return reset_timer


def deposit() -> None:
    global defaultAttempts
    global currentPhase
    global waiting

    if not waiting:
        location = pyautogui.locateOnScreen(bankExitPic)
        location = pyautogui.center(location)
        pyautogui.moveTo(location.x + 5, location.y - 35)
        pyautogui.click()
        waiting = False
        currentPhase = CurrentPhase.BASE
        ORIENT.down_orient()
        defaultAttempts = 0


def denseEssProcess(current_phase, waiting_, seconds_mining, logger) -> None:
    global currentPhase
    global secondsMining
    global log_handle

    log_handle = logger
    secondsMining = seconds_mining
    reset_timer = 25

    ORIENT.finish_orient()

    if currentPhase == CurrentPhase.BASE:
        reset_timer = base()
    elif currentPhase == CurrentPhase.ROCK_HOP:
        reset_timer = rock_hop()
    elif currentPhase == CurrentPhase.MINES_MAP:
        mines_map()
    elif currentPhase == CurrentPhase.ROCK_LARGE:
        reset_timer = rock_large()
    elif currentPhase == CurrentPhase.HOME:
        reset_timer = teleport_home()
    elif currentPhase == CurrentPhase.BANK:
        reset_timer = bank()
    elif currentPhase == CurrentPhase.DEPOSIT:
        deposit()
    return reset_timer
