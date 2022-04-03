"""basicFunctions.py - Scans for pixel colors on screen"""

import random
from typing import Any, Tuple
from PIL.Image import Image
from pynput.mouse import Controller
import keyboard
import pyautogui


_MARK_OF_GRACE_ = False


class RGBMage:
    """RGB Values for Mage"""
    RED = 15
    GREEN = 15
    BLUE = 15
    MAX = 255
    MIN = 0


class ObjName:
    """Object names"""
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
    HARVEST_TRAP = 'HarvestTrap'


def mage(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if px_test[1] > RGBMage.RED or px_test[0] < RGBMage.GREEN or px_test[2] < RGBMage.BLUE:
        return False
    _x += 56
    _y += 33
    for _ in range(0, 5):
        # checking for yellow, mage tooltip (no blue)
        px_test = color.getpixel(_x, _y)
        if px_test[0] == RGBMage.MAX and \
                px_test[1] == RGBMage.MAX and \
                px_test[2] == RGBMage.MIN:
            return True
        _x += 1
    return False


def rock_small(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if not (px_test[1] > px_test[0] + 30 or px_test[1] > px_test[2] + 30):
        return False
    _x += 31
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.ROCK_SMALL)


def rock_large(_x: int, _y: int, px_test: str, color: Image) -> bool:
    _x += 68
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.ROCK_LARGE)


def bank(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if px_test[0] > 175 or px_test[1] > 175 or px_test[2] > 175:
        return False
    _x += 54
    _y += 31
    return check_tooltip_blue(_x, _y, color, ObjName.BANK)


def barrel(_x: int, _y: int, px_test: str, color: Image) -> bool:
    # Pollinveach agility defaults
    if not (px_test[1] > 160 and px_test[0] < 150 and px_test[2] < 100):
        return False
    _x += 54
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.BARREL)


def barrel_red(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if not (px_test[0] > 160 and px_test[1] < 150 and px_test[2] < 100):
        return False
    _x += 54
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.BARREL_RED)


def mark_of_grace(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if not (px_test[0] > 120 and px_test[1] < 140 and px_test[2] < 100):
        return False
    _x += 54
    _y += 33
    for _ in range(0, 10):
        px_test = color.getpixel((_x, _y))
        if px_test[0] == 255 and px_test[1] == 144 and px_test[2] == 64:
            return True
        _x += 1
    return False


def market_stall(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if not (100 < px_test[0] < 200 and 100 < px_test[1] < 200 and 100 < px_test[2] < 200):
        return False
    _x += 54
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.MARKET_STALL)


def banner(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if not (px_test[0] < 160 and px_test[2] < 160 and px_test[1] > 190):
        return False
    _x += 54
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.BANNER)


def leap_gap(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if not (px_test[0] > 100 and px_test[1] > 100 and px_test[2] < 100):
        return False
    _x += 34
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.LEAP_GAP)


def tree_one(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if not (px_test[0] > 100 and px_test[1] > 100 and px_test[2] < 100):
        return False
    _x += 54
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.TREE_ONE)


def tree_two(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if not (px_test[1] > px_test[0] and px_test[1] > px_test[2]):
        return False
    _x += 54
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.TREE_TWO)


def rough_wall(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if not (px_test[0] < 150 and px_test[1] > 180 and px_test[2] < 150):
        return False
    _x += 54
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.ROUGH_WALL)


def monkey_bars(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if not (px_test[0] < 125 and px_test[1] > 150 and px_test[2] < 125):
        return False
    _x += 54
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.MONKEY_BARS)


def drying_line(_x: int, _y: int, px_test: str, color: Image) -> bool:
    if not (px_test[0] < 140 and px_test[1] > 150 and px_test[2] < 140):
        return False
    _x += 54
    _y += 33
    return check_tooltip_blue(_x, _y, color, ObjName.DRYING_LINE)


def grab_color() -> Any:
    """Returns color"""
    screen_shot = pyautogui.screenshot()
    color_test = screen_shot.getpixel(pyautogui.position())
    return color_test


def is_moving(wait_color: int) -> Tuple[bool, Any]:
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


def check_tooltip(obj_name: str) -> bool:
    """Checks tool tip"""
    global OBJ_FUNC_LOOKUP
    _x, _y = pyautogui.position()
    color = pyautogui.screenshot()
    px_test = color.getpixel(_x, _y)
    return OBJ_FUNC_LOOKUP.get(obj_name)(_x, _y, px_test, color)


class DefaultMove:
    
def default_mage() -> bool:
    pyautogui.moveTo(
        327 + random.randint(-50, 50), 327 + random.randint(-5, 5))
    return check_tooltip(ObjName.MAGE)


def default_rock_small() -> bool:
    pyautogui.moveTo(
        541 + random.randint(-100, 100), 519 + random.randint(-20, 20))
    return check_tooltip(ObjName.ROCK_SMALL)


def default_rock_large() -> bool:
    pyautogui.moveTo(
        640 + random.randint(-100, 100), 441 + random.randint(-20, 20))
    return check_tooltip(ObjName.ROCK_LARGE)


def default_bank() -> bool:
    pyautogui.moveTo(
        854 + random.randint(-30, 30), 320 + random.randint(-10, 10))
    return check_tooltip(ObjName.BANK)


def default_barrel() -> bool:
    global _MARK_OF_GRACE_
    pyautogui.moveTo(
        634 + random.randint(-50, 50), 307 + random.randint(-20, 20))
    if check_tooltip(ObjName.BARREL):
        return True

    if check_tooltip(ObjName.BARREL_RED):
        _MARK_OF_GRACE_ = True
        return True
    return False


def default_mark_of_grace() -> bool:
    pyautogui.moveTo(
        446 + random.randint(-30, 30), 295 + random.randint(-20, 20))
    return check_tooltip(ObjName.MARK_OF_GRACE)


def default_market_stall() -> bool:
    global _MARK_OF_GRACE_
    if not _MARK_OF_GRACE_:
        pyautogui.moveTo(
            534 + random.randint(-30, 30), 237 + random.randint(-20, 20))
    else:
        pyautogui.moveTo(
            629 + random.randint(-30, 30), 336 + random.randint(-20, 20))
    return check_tooltip(ObjName.MARKET_STALL)


def default_banner() -> bool:
    pyautogui.moveTo(
        652 + random.randint(-30, 30), 274 + random.randint(-20, 20))
    return check_tooltip(ObjName.BANNER)


def default_leap_gap() -> bool:
    pyautogui.moveTo(
        640 + random.randint(-30, 30), 415 + random.randint(-20, 20))
    return check_tooltip(ObjName.LEAP_GAP)


def default_tree_one() -> bool:
    pyautogui.moveTo(
        594 + random.randint(-30, 30), 344 + random.randint(-20, 20))
    return check_tooltip(ObjName.TREE_ONE)


def default_tree_two() -> bool:
    pyautogui.moveTo(
        591 + random.randint(-30, 30), 294 + random.randint(-20, 20))
    return check_tooltip(ObjName.TREE_TWO)


def default_rough_wall() -> bool:
    pyautogui.moveTo(
        452 + random.randint(-30, 30), 361 + random.randint(-20, 20))
    return check_tooltip(ObjName.ROUGH_WALL)


def default_monkey_bars() -> bool:
    pyautogui.moveTo(
        380 + random.randint(-30, 30), 340 + random.randint(-20, 20))
    return check_tooltip(ObjName.MONKEY_BARS)


def default_drying_line() -> bool:
    pyautogui.moveTo(
        650 + random.randint(-30, 30), 378 + random.randint(-20, 20))
    return check_tooltip(ObjName.DRYING_LINE)


def default_harvest_trap() -> bool:
    """Is this right???"""
    pyautogui.moveTo(
        536 + random.randint(-10, 10), 403 + random.randint(-133, 133))
    return check_tooltip(ObjName.DRYING_LINE)


def check_default(obj_name: str) -> bool:
    return DEFAULT_LOOKUP.get(obj_name)()


def down_orient() -> None:
    global MOUSE
    pyautogui.moveTo(911, 44)
    pyautogui.click()
    MOUSE.scroll(0, -10)
    keyboard.press("down")


def up_orient() -> None:
    global MOUSE
    MOUSE.scroll(0, -10)
    keyboard.press("up")


def finish_orient() -> None:
    keyboard.release("down")
    keyboard.release("up")


MOUSE = Controller()

OBJ_FUNC_LOOKUP = {
    ObjName.MAGE: mage,
    ObjName.ROCK_SMALL: rock_small,
    ObjName.ROCK_LARGE: rock_large,
    ObjName.BANK: bank,
    ObjName.BARREL: barrel,
    ObjName.BARREL_RED: barrel_red,
    ObjName.MARK_OF_GRACE: mark_of_grace,
    ObjName.MARKET_STALL: market_stall,
    ObjName.BANNER: banner,
    ObjName.LEAP_GAP: leap_gap,
    ObjName.TREE_ONE: tree_one,
    ObjName.TREE_TWO: tree_two,
    ObjName.ROUGH_WALL: rough_wall,
    ObjName.MONKEY_BARS: monkey_bars,
    ObjName.DRYING_LINE: drying_line
}

DEFAULT_LOOKUP = {
    ObjName.MAGE: default_mage,
    ObjName.ROCK_SMALL: default_rock_small,
    ObjName.ROCK_LARGE: default_rock_large,
    ObjName.BANK: default_bank,
    ObjName.BARREL: default_barrel,
    # ObjName.BARREL_RED: default_barrel_red,
    ObjName.MARK_OF_GRACE: default_mark_of_grace,
    ObjName.MARKET_STALL: default_market_stall,
    ObjName.BANNER: default_banner,
    ObjName.LEAP_GAP: default_leap_gap,
    ObjName.TREE_ONE: default_tree_one,
    ObjName.TREE_TWO: default_tree_two,
    ObjName.ROUGH_WALL: default_rough_wall,
    ObjName.MONKEY_BARS: default_monkey_bars,
    ObjName.DRYING_LINE: default_drying_line,
    ObjName.HARVEST_TRAP: default_harvest_trap
}
