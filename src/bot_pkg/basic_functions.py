"""basicFunctions.py - Scans for pixel colors on screen"""

import random
from typing import Any, Tuple
from PIL.Image import Image
from pynput.mouse import Controller
import keyboard
import pyautogui


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


class Orient:
    def __init__(self) -> None:
        self.mouse = Controller()

    def down_orient(self) -> None:
        pyautogui.moveTo(911, 44)
        pyautogui.click()
        self.mouse.scroll(0, -10)
        keyboard.press("down")

    def up_orient(self) -> None:
        self.mouse.scroll(0, -10)
        keyboard.press("up")

    def finish_orient(self) -> None:
        keyboard.release("down")
        keyboard.release("up")


class DefaultMouseMove:
    def __init__(self) -> None:
        self.__mark_of_grace = False

        self.__obj_func_lookup = {
            ObjName.MAGE: self.mage,
            ObjName.ROCK_SMALL: self.rock_small,
            ObjName.ROCK_LARGE: self.rock_large,
            ObjName.BANK: self.bank,
            ObjName.BARREL: self.barrel,
            ObjName.BARREL_RED: self.barrel_red,
            ObjName.MARK_OF_GRACE: self.mark_of_grace,
            ObjName.MARKET_STALL: self.market_stall,
            ObjName.BANNER: self.banner,
            ObjName.LEAP_GAP: self.leap_gap,
            ObjName.TREE_ONE: self.tree_one,
            ObjName.TREE_TWO: self.tree_two,
            ObjName.ROUGH_WALL: self.rough_wall,
            ObjName.MONKEY_BARS: self.monkey_bars,
            ObjName.DRYING_LINE: self.drying_line
        }

        self.__default_lookup = {
            ObjName.MAGE: self.check_mage,
            ObjName.ROCK_SMALL: self.check_rock_small,
            ObjName.ROCK_LARGE: self.check_rock_large,
            ObjName.BANK: self.check_bank,
            ObjName.BARREL: self.check_barrel,
            # ObjName.BARREL_RED: default_barrel_red,
            ObjName.MARK_OF_GRACE: self.check_mark_of_grace,
            ObjName.MARKET_STALL: self.check_market_stall,
            ObjName.BANNER: self.check_banner,
            ObjName.LEAP_GAP: self.check_leap_gap,
            ObjName.TREE_ONE: self.check_tree_one,
            ObjName.TREE_TWO: self.check_tree_two,
            ObjName.ROUGH_WALL: self.check_rough_wall,
            ObjName.MONKEY_BARS: self.check_monkey_bars,
            ObjName.DRYING_LINE: self.check_drying_line,
            ObjName.HARVEST_TRAP: self.check_harvest_trap
        }

    #### DEFAULTS ###
    def check_default_lookup(self, obj_name: str) -> bool:
        return self.__default_lookup.get(obj_name)()

    def check_obj(self, obj_name: str) -> bool:
        """Checks tool tip"""
        _x, _y = pyautogui.position()
        color = pyautogui.screenshot()
        px_test = color.getpixel((_x, _y))
        return self.__obj_func_lookup.get(obj_name)(_x, _y, px_test, color)

    def check_mage(self) -> bool:
        pyautogui.moveTo(
            327 + random.randint(-50, 50), 327 + random.randint(-5, 5))
        return self.check_obj(ObjName.MAGE)

    def check_rock_small(self) -> bool:
        pyautogui.moveTo(
            541 + random.randint(-100, 100), 519 + random.randint(-20, 20))
        return self.check_obj(ObjName.ROCK_SMALL)

    def check_rock_large(self) -> bool:
        pyautogui.moveTo(
            640 + random.randint(-100, 100), 441 + random.randint(-20, 20))
        return self.check_obj(ObjName.ROCK_LARGE)

    def check_bank(self) -> bool:
        pyautogui.moveTo(
            854 + random.randint(-30, 30), 320 + random.randint(-10, 10))
        return self.check_obj(ObjName.BANK)

    def check_barrel(self) -> bool:
        pyautogui.moveTo(
            634 + random.randint(-50, 50), 307 + random.randint(-20, 20))
        if self.check_obj(ObjName.BARREL):
            return True

        if self.check_obj(ObjName.BARREL_RED):
            self.__mark_of_grace = True
            return True
        return False

    def check_mark_of_grace(self) -> bool:
        pyautogui.moveTo(
            446 + random.randint(-30, 30), 295 + random.randint(-20, 20))
        return self.check_obj(ObjName.MARK_OF_GRACE)

    def check_market_stall(self) -> bool:
        if not self.__mark_of_grace:
            pyautogui.moveTo(
                534 + random.randint(-30, 30), 237 + random.randint(-20, 20))
        else:
            pyautogui.moveTo(
                629 + random.randint(-30, 30), 336 + random.randint(-20, 20))
        return self.check_obj(ObjName.MARKET_STALL)

    def check_banner(self) -> bool:
        pyautogui.moveTo(
            652 + random.randint(-30, 30), 274 + random.randint(-20, 20))
        return self.check_obj(ObjName.BANNER)

    def check_leap_gap(self) -> bool:
        pyautogui.moveTo(
            640 + random.randint(-30, 30), 415 + random.randint(-20, 20))
        return self.check_obj(ObjName.LEAP_GAP)

    def check_tree_one(self) -> bool:
        pyautogui.moveTo(
            594 + random.randint(-30, 30), 344 + random.randint(-20, 20))
        return self.check_obj(ObjName.TREE_ONE)

    def check_tree_two(self) -> bool:
        pyautogui.moveTo(
            591 + random.randint(-30, 30), 294 + random.randint(-20, 20))
        return self.check_obj(ObjName.TREE_TWO)

    def check_rough_wall(self) -> bool:
        pyautogui.moveTo(
            452 + random.randint(-30, 30), 361 + random.randint(-20, 20))
        return self.check_obj(ObjName.ROUGH_WALL)

    def check_monkey_bars(self) -> bool:
        pyautogui.moveTo(
            380 + random.randint(-30, 30), 340 + random.randint(-20, 20))
        return self.check_obj(ObjName.MONKEY_BARS)

    def check_drying_line(self) -> bool:
        pyautogui.moveTo(
            650 + random.randint(-30, 30), 378 + random.randint(-20, 20))
        return self.check_obj(ObjName.DRYING_LINE)

    def check_harvest_trap(self) -> bool:
        """Is this right???"""
        pyautogui.moveTo(
            536 + random.randint(-10, 10), 403 + random.randint(-133, 133))
        return self.check_obj(ObjName.DRYING_LINE)

    def check_tooltip(self, obj_name: str) -> bool:
        """Checks tool tip"""
        _x, _y = pyautogui.position()
        color = pyautogui.screenshot()
        px_test = color.getpixel((_x, _y))
        return self.__obj_func_lookup.get(obj_name)(_x, _y, px_test, color)

    def mage(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if px_test[1] > RGBMage.RED or px_test[0] < RGBMage.GREEN or px_test[2] < RGBMage.BLUE:
            return False
        _x += 56
        _y += 33
        for _ in range(0, 5):
            # checking for yellow, mage tooltip (no blue)
            px_test = color.getpixel((_x, _y))
            if px_test[0] == RGBMage.MAX and \
                    px_test[1] == RGBMage.MAX and \
                    px_test[2] == RGBMage.MIN:
                return True
            _x += 1
        return False

    def rock_small(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if not (px_test[1] > px_test[0] + 30 or px_test[1] > px_test[2] + 30):
            return False
        _x += 31
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.ROCK_SMALL)

    def rock_large(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        _x += 68
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.ROCK_LARGE)

    def bank(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if px_test[0] > 175 or px_test[1] > 175 or px_test[2] > 175:
            return False
        _x += 54
        _y += 31
        return self.check_tooltip_blue(_x, _y, color, ObjName.BANK)

    def barrel(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        # Pollinveach agility defaults
        if not (px_test[1] > 160 and px_test[0] < 150 and px_test[2] < 100):
            return False
        _x += 54
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.BARREL)

    def barrel_red(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if not (px_test[0] > 160 and px_test[1] < 150 and px_test[2] < 100):
            return False
        _x += 54
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.BARREL_RED)

    def mark_of_grace(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
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

    def market_stall(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if not (100 < px_test[0] < 200 and 100 < px_test[1] < 200 and 100 < px_test[2] < 200):
            return False
        _x += 54
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.MARKET_STALL)

    def banner(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if not (px_test[0] < 160 and px_test[2] < 160 and px_test[1] > 190):
            return False
        _x += 54
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.BANNER)

    def leap_gap(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if not (px_test[0] > 100 and px_test[1] > 100 and px_test[2] < 100):
            return False
        _x += 34
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.LEAP_GAP)

    def tree_one(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if not (px_test[0] > 100 and px_test[1] > 100 and px_test[2] < 100):
            return False
        _x += 54
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.TREE_ONE)

    def tree_two(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if not (px_test[1] > px_test[0] and px_test[1] > px_test[2]):
            return False
        _x += 54
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.TREE_TWO)

    def rough_wall(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if not (px_test[0] < 150 and px_test[1] > 180 and px_test[2] < 150):
            return False
        _x += 54
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.ROUGH_WALL)

    def monkey_bars(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if not (px_test[0] < 125 and px_test[1] > 150 and px_test[2] < 125):
            return False
        _x += 54
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.MONKEY_BARS)

    def drying_line(self, _x: int, _y: int, px_test: str, color: Image) -> bool:
        if not (px_test[0] < 140 and px_test[1] > 150 and px_test[2] < 140):
            return False
        _x += 54
        _y += 33
        return self.check_tooltip_blue(_x, _y, color, ObjName.DRYING_LINE)

    def grab_color(self) -> Any:
        """Returns color"""
        screen_shot = pyautogui.screenshot()
        color_test = screen_shot.getpixel(pyautogui.position())
        return color_test

    def is_moving(self, wait_color: int) -> Tuple[bool, Any]:
        """Returns True if character moving"""
        if wait_color == self.grab_color():
            return False, wait_color
        return True, self.grab_color()

    def check_tooltip_blue(self, _x: int, _y: int, color: Image, obj_name: str) -> bool:
        """checking for blue, rock tooltip (no red)"""
        for _ in range(0, 10):
            px_test = color.getpixel((_x, _y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print(f"{obj_name} test succeeded")
                return True
            _x += 1

        print(f"{obj_name} second test failed")
        return False
