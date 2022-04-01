import pyautogui
from .robot import Robot
from time import sleep
from path_config import ARDOUGE_ASSETS


def run():
    ardy = Robot(__file__, ARDOUGE_ASSETS)
    ardy.setup_bot()

    sleep(2)

    sleep(0.5)
    ardy.click("compass")
    pyautogui.keyDown("up")
    sleep(0.5)
    ardy.click("first")
    sleep(4.9)
    ##pyautogui.moveTo(546, 199)
    ##pyautogui.click(546, 199, 5)
    ardy.click("second")
    sleep(9)
    ardy.click("third")
    sleep(6.8)
    ardy.check_asset("mark")
    sleep(0.8)
    ardy.click("fourth")
    sleep(1.3)
    ardy.click("fifth")
    sleep(2.5)
    ardy.click("sixth")
    sleep(6.5)
    ##pyautogui.moveTo(546, 408)
    ##pyautogui.click(546, 408, 2)
    ardy.click("seven")
    sleep(9.3)
