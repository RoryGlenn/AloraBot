"""smithing.py - ..."""

from time import sleep

import pyautogui

from .robot import Robot
from path_config import SMITHING_ASSETS


def run() -> None:
    robot = Robot(__file__, SMITHING_ASSETS)
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
