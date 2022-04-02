"""basicFunctions.py - Scans for pixel colors on screen"""

import random
from typing import Any, Tuple
import keyboard
import pyautogui
from pynput.mouse import Controller
from PIL.Image import Image

mouse = Controller()


class MageRGB:
    RED = 15
    GREEN = 15
    BLUE = 15
    MAX = 255
    MIN = 0


class Object:
    MAGE = 'Mage'
    ROCK_SMALL = "Small Rock"
    ROCK_LARGE = "Large Rock"
    BANK = 'Bank'
    BARREL = 'Barrel'
    BARREL_RED = "Red Barrel"
    MARK_OF_GRACE = "Mark of Grace"
    MARKET_STALL = "Market Stall"
    BANNER = "Banner"
    LEAP_GAP = "Leap Gap"
    TREE_ONE = "TreeOne"
    TREE_TWO = "TreeTwo"
    ROUGH_WALL = "Rough Wall"
    MONKEY_BARS = "Monkeybars"
    DRYING_LINE = "Drying Line"
    # HARVEST_TRAP = 'HarvestTrap'


def grab_color():
    """Returns color"""
    screen_shot = pyautogui.screenshot()
    color_test = screen_shot.getpixel(pyautogui.position())
    return color_test


def is_moving(wait_color) -> Tuple[bool, Any]:
    """Returns True if character moving"""
    if wait_color == grab_color():
        return False, wait_color
    return True, grab_color()


def check_tooltip_blue(_x: int, _y: int, color: Image, obj_name: str) -> bool:
    """checking for blue, rock tooltip (no red)"""
    for _ in range(0, 10):
        px_test = color.getpixel((_x, _y))
        if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
            print(f"{obj_name} test succeeded")
            return True
        _x += 1

    print(f"{obj_name} second test failed")
    return False


def check_tooltip(object) -> bool:
    """Checks tool tip"""
    _x, _y = pyautogui.position()
    color = pyautogui.screenshot()
    px_test = color.getpixel((_x, _y))

    # Dense Ess defaults
    if object == Object.MAGE:
        if px_test[1] > MageRGB.RED or px_test[0] < MageRGB.GREEN or px_test[2] < MageRGB.BLUE:
            return False
        _x += 56
        _y += 33
        for _ in range(0, 5):
            # checking for yellow, mage tooltip (no blue)
            px_test = color.getpixel((_x, _y))
            if px_test[0] == MageRGB.MAX and px_test[1] == MageRGB.MAX and px_test[2] == MageRGB.MIN:
                print("Found Mage tooltip")
                return True
            _x += 1
        print("Could not find mage tool tip")
        return False
    elif object == Object.ROCK_SMALL:
        if not (px_test[1] > px_test[0] + 30 or px_test[1] > px_test[2] + 30):
            return False
        _x += 31
        _y += 33
        return check_tooltip_blue(_x, _y, color, Object.ROCK_SMALL)
    elif object == Object.ROCK_LARGE:
        _x += 68
        _y += 33
        return check_tooltip_blue(_x, _y, color, Object.ROCK_LARGE)
    elif object == Object.BANK:
        if px_test[0] > 175 or px_test[1] > 175 or px_test[2] > 175:
            print(f"{Object.BANK} first test failed")
            return False
        _x += 54
        _y += 31
        return check_tooltip_blue(_x, _y, color, Object.BANK)
    elif object == Object.BARREL:
        # Pollinveach agility defaults
        if not (px_test[1] > 160 and px_test[0] < 150 and px_test[2] < 100):
            print("First test failed")
            return False
        _x += 54
        _y += 33
        return check_tooltip_blue(_x, _y, color)
    elif object == Object.BARREL_RED:
        if not (px_test[0] > 160 and px_test[1] < 150 and px_test[2] < 100):
            print("First test failed")
            return False
        _x += 54
        _y += 33
        return check_tooltip_blue(_x, _y, color)
    elif object == Object.MARK_OF_GRACE:
        if not (px_test[0] > 120 and px_test[1] < 140 and px_test[2] < 100):
            print("First test failed")
            return False
        _x += 54
        _y += 33
        for _ in range(0, 10):
            px_test = color.getpixel((_x, _y))
            if px_test[0] == 255 and px_test[1] == 144 and px_test[2] == 64:
                print("Test succeeded")
                return True
            _x += 1
        print("Second test failed")
        return False
    elif object == Object.MARKET_STALL:
        if not (100 < px_test[0] < 200 and 100 < px_test[1] < 200 and 100 < px_test[2] < 200):
            print("First test failed")
            return False
        _x += 54
        _y += 33
        return check_tooltip_blue(_x, _y, color)
    elif object == Object.BANNER:
        if not (px_test[0] < 160 and px_test[2] < 160 and px_test[1] > 190):
            print("First test failed")
            return False
        _x += 54
        _y += 33
        return check_tooltip_blue(_x, _y, color)
    elif object == Object.LEAP_GAP:
        if not (px_test[0] > 100 and px_test[1] > 100 and px_test[2] < 100):
            print("First test failed")
            return False
        _x += 34
        _y += 33
        return check_tooltip_blue(_x, _y, color)
    elif object == Object.TREE_ONE:
        if not (px_test[0] > 100 and px_test[1] > 100 and px_test[2] < 100):
            print("First test failed")
            return False
        _x += 54
        _y += 33
        return check_tooltip_blue(_x, _y, color)
    elif object == Object.ROUGH_WALL:
        if not (px_test[0] < 150 and px_test[1] > 180 and px_test[2] < 150):
            print("First test failed")
            return False
        _x += 54
        _y += 33
        return check_tooltip_blue(_x, _y, color)
    elif object == Object.MONKEY_BARS:
        if not (px_test[0] < 125 and px_test[1] > 150 and px_test[2] < 125):
            print("First test failed")
            return False
        _x += 54
        _y += 33
        return check_tooltip_blue(_x, _y, color)
    elif object == Object.TREE_TWO:
        if not (px_test[1] > px_test[0] and px_test[1] > px_test[2]):
            print("First test failed")
            return False
        _x += 54
        _y += 33
        return check_tooltip_blue(_x, _y, color)
    elif object == Object.DRYING_LINE:
        if not (px_test[0] < 140 and px_test[1] > 150 and px_test[2] < 140):
            print("First test failed")
            return False
        _x += 54
        _y += 33
        return check_tooltip_blue(_x, _y, color)


def check_default(object):
    global markOfGrace
    # Dense Ess defaults
    if object == Object.MAGE:
        pyautogui.moveTo(
            327 + random.randint(-50, 50), 327 + random.randint(-5, 5))
        return check_tooltip(Object.MAGE)
    elif object == Object.ROCK_SMALL:
        pyautogui.moveTo(
            541 + random.randint(-100, 100), 519 + random.randint(-20, 20))
        return check_tooltip(Object.ROCK_SMALL)
    elif object == Object.ROCK_LARGE:
        pyautogui.moveTo(
            640 + random.randint(-100, 100), 441 + random.randint(-20, 20))
        return check_tooltip(Object.ROCK_LARGE)
    elif object == Object.BANK:
        pyautogui.moveTo(
            854 + random.randint(-30, 30), 320 + random.randint(-10, 10))
        return check_tooltip(Object.BANK)
    # Pollinveach agility defaults
    elif object == Object.BARREL:
        pyautogui.moveTo(
            634 + random.randint(-50, 50), 307 + random.randint(-20, 20))
        if check_tooltip(Object.BARREL):
            return True
        if check_tooltip(Object.BARREL_RED):
            markOfGrace = True
            return True
        return False
    elif object == Object.MARK_OF_GRACE:
        pyautogui.moveTo(
            446 + random.randint(-30, 30), 295 + random.randint(-20, 20))
        return check_tooltip(Object.MARK_OF_GRACE)
    elif object == Object.MARKET_STALL:
        if not markOfGrace:
            pyautogui.moveTo(
                534 + random.randint(-30, 30), 237 + random.randint(-20, 20))
        else:
            pyautogui.moveTo(
                629 + random.randint(-30, 30), 336 + random.randint(-20, 20))
        return check_tooltip(Object.MARKET_STALL)
    elif object == Object.BANNER:
        pyautogui.moveTo(
            652 + random.randint(-30, 30), 274 + random.randint(-20, 20))
        return check_tooltip(Object.BANNER)
    elif object == Object.LEAP_GAP:
        pyautogui.moveTo(
            640 + random.randint(-30, 30), 415 + random.randint(-20, 20))
        return check_tooltip(Object.LEAP_GAP)
    elif object == Object.TREE_ONE:
        pyautogui.moveTo(
            594 + random.randint(-30, 30), 344 + random.randint(-20, 20))
        return check_tooltip(Object.TREE_ONE)
    elif object == Object.ROUGH_WALL:
        pyautogui.moveTo(
            452 + random.randint(-30, 30), 361 + random.randint(-20, 20))
        return check_tooltip(Object.ROUGH_WALL)
    elif object == Object.MONKEY_BARS:
        pyautogui.moveTo(
            380 + random.randint(-30, 30), 340 + random.randint(-20, 20))
        return check_tooltip(Object.MONKEY_BARS)
    elif object == Object.TREE_TWO:
        pyautogui.moveTo(
            591 + random.randint(-30, 30), 294 + random.randint(-20, 20))
        return check_tooltip(Object.TREE_TWO)
    elif object == Object.DRYING_LINE:
        pyautogui.moveTo(
            650 + random.randint(-30, 30), 378 + random.randint(-20, 20))
        return check_tooltip(Object.DRYING_LINE)
    elif object == "HarvestTrap":  # IS THIS RIGHT???
        pyautogui.moveTo(
            536 + random.randint(-10, 10), 403 + random.randint(-133, 133))
        return check_tooltip("Drying Line")


def down_orient():
    pyautogui.moveTo(911, 44)
    pyautogui.click()
    mouse.scroll(0, -10)
    keyboard.press("down")


def up_orient():
    mouse.scroll(0, -10)
    keyboard.press("up")


def finish_orient():
    keyboard.release("down")
    keyboard.release("up")
