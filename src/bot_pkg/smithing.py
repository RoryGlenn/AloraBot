from time import sleep

import pyautogui

from .robot import Robot
from path_config import smithing_assets


def run():
    robot = Robot(__file__, smithing_assets)
    robot.setup_bot()

    sleep(3)

    robot.click("anvil")
    sleep(3.3)
    robot.click("plate")
    sleep(14)
    robot.click("bank")
    sleep(5.5)
    robot.press_key("esc")
    sleep(0.3)
    robot.click("compass")
    pyautogui.keyDown("up")
