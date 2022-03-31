
import random

import keyboard
import pyautogui
from pynput.mouse import Controller

mouse = Controller()


def grabColor():
    x, y = pyautogui.position()
    ss = pyautogui.screenshot()
    colorTest = ss.getpixel((x, y))
    return colorTest


def moving(waitColor):
    if waitColor == grabColor():
        return False, waitColor
    else:
        waitColor = grabColor()
        return True, waitColor


def checkTooltip(object):
    x, y = pyautogui.position()
    color = pyautogui.screenshot()
    px_test = color.getpixel((x, y))

    # Dense Ess defaults
    if object == "Mage":
        if px_test[1] > 15 or px_test[0] < 15 or px_test[2] < 15:
            print("First test failed")
            return False
        # checking for yellow, mage tooltip (no blue)
        x += 56
        y += 33
        for i in range(0, 5):
            px_test = color.getpixel((x, y))
            if px_test[0] == 255 and px_test[1] == 255 and px_test[2] == 0:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "Small Rock":
        if not (px_test[1] > px_test[0] + 30 or px_test[1] > px_test[2] + 30):
            return False
        # checking for blue, rock tooltip (no red)
        x += 31
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "Large Rock":
        x += 68
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "Bank":
        if px_test[0] > 175 or px_test[1] > 175 or px_test[2] > 175:
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 54
        y += 31
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    # Pollinveach agility defaults
    elif object == "Barrel":
        if not (px_test[1] > 160 and px_test[0] < 150 and px_test[2] < 100):
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 54
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "Red Barrel":
        if not (px_test[0] > 160 and px_test[1] < 150 and px_test[2] < 100):
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 54
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "Mark of Grace":
        if not (px_test[0] > 120 and px_test[1] < 140 and px_test[2] < 100):
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 54
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 255 and px_test[1] == 144 and px_test[2] == 64:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "Market Stall":
        if not (100 < px_test[0] < 200 and 100 < px_test[1] < 200 and 100 < px_test[2] < 200):
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 54
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "Banner":
        if not (px_test[0] < 160 and px_test[2] < 160 and px_test[1] > 190):
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 54
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "Leap Gap":
        if not (px_test[0] > 100 and px_test[1] > 100 and px_test[2] < 100):
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 34
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "TreeOne":
        if not (px_test[0] > 100 and px_test[1] > 100 and px_test[2] < 100):
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 54
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "Rough Wall":
        if not (px_test[0] < 150 and px_test[1] > 180 and px_test[2] < 150):
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 54
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "Monkeybars":
        if not (px_test[0] < 125 and px_test[1] > 150 and px_test[2] < 125):
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 54
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "TreeTwo":
        if not (px_test[1] > px_test[0] and px_test[1] > px_test[2]):
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 54
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False

    elif object == "Drying Line":
        if not (px_test[0] < 140 and px_test[1] > 150 and px_test[2] < 140):
            print("First test failed")
            return False
        # checking for blue, rock tooltip (no red)
        x += 54
        y += 33
        for i in range(0, 10):
            px_test = color.getpixel((x, y))
            if px_test[0] == 0 and px_test[1] == 255 and px_test[2] == 255:
                print("Test succeeded")
                return True
            x += 1
        print("Second test failed")
        return False


def checkDefault(object):
    global markOfGrace
    # Dense Ess defaults
    if object == "Mage":
        pyautogui.moveTo(327 + random.randint(-50, 50),
                         327 + random.randint(-5, 5))
        return checkTooltip("Mage")

    elif object == "Small Rock":
        pyautogui.moveTo(541 + random.randint(-100, 100),
                         519 + random.randint(-20, 20))
        return checkTooltip("Small Rock")

    elif object == "Large Rock":
        pyautogui.moveTo(640 + random.randint(-100, 100),
                         441 + random.randint(-20, 20))
        return checkTooltip("Large Rock")

    elif object == "Bank":
        pyautogui.moveTo(854 + random.randint(-30, 30),
                         320 + random.randint(-10, 10))
        return checkTooltip("Bank")

    # Pollinveach agility defaults
    elif object == "Barrel":
        pyautogui.moveTo(634 + random.randint(-50, 50),
                         307 + random.randint(-20, 20))
        if checkTooltip("Barrel"):
            return True
        else:
            if checkTooltip("Red Barrel"):
                markOfGrace = True
                return True
            else:
                return False

    elif object == "Mark of Grace":
        pyautogui.moveTo(446 + random.randint(-30, 30),
                         295 + random.randint(-20, 20))
        return checkTooltip("Mark of Grace")

    elif object == "Market Stall":
        if not markOfGrace:
            pyautogui.moveTo(534 + random.randint(-30, 30),
                             237 + random.randint(-20, 20))
        else:
            pyautogui.moveTo(629 + random.randint(-30, 30),
                             336 + random.randint(-20, 20))
        return checkTooltip("Market Stall")

    elif object == "Banner":
        pyautogui.moveTo(652 + random.randint(-30, 30),
                         274 + random.randint(-20, 20))
        return checkTooltip("Banner")

    elif object == "Leap Gap":
        pyautogui.moveTo(640 + random.randint(-30, 30),
                         415 + random.randint(-20, 20))
        return checkTooltip("Leap Gap")

    elif object == "TreeOne":
        pyautogui.moveTo(594 + random.randint(-30, 30),
                         344 + random.randint(-20, 20))
        return checkTooltip("TreeOne")

    elif object == "Rough Wall":
        pyautogui.moveTo(452 + random.randint(-30, 30),
                         361 + random.randint(-20, 20))
        return checkTooltip("Rough Wall")

    elif object == "Monkeybars":
        pyautogui.moveTo(380 + random.randint(-30, 30),
                         340 + random.randint(-20, 20))
        return checkTooltip("Monkeybars")

    elif object == "TreeTwo":
        pyautogui.moveTo(591 + random.randint(-30, 30),
                         294 + random.randint(-20, 20))
        return checkTooltip("TreeTwo")

    elif object == "Drying Line":
        pyautogui.moveTo(650 + random.randint(-30, 30),
                         378 + random.randint(-20, 20))
        return checkTooltip("Drying Line")

    elif object == "HarvestTrap":
        pyautogui.moveTo(536 + random.randint(-10, 10),
                         403 + random.randint(-133, 133))
        return checkTooltip("Drying Line")


def downOrient():
    pyautogui.moveTo(911, 44)
    pyautogui.click()
    mouse.scroll(0, -10)
    keyboard.press("down")


def upOrient():
    mouse.scroll(0, -10)
    keyboard.press("up")


def finishOrient():
    keyboard.release("down")
    keyboard.release("up")
