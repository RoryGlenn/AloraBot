"""wines.py - ..."""

from time import sleep
from .robot import Robot
from path_config import WINES_ASSETS


def run() -> None:
    robot = Robot(__file__, WINES_ASSETS)
    robot.setup_bot()

    sleep(3)

    robot.click("grape")
    sleep(0.3)
    robot.click("wine")
    sleep(0.7)
    robot.press_key("1")
    sleep(25)
    robot.click("bank")
    sleep(1.5)
    robot.press_key("esc")
