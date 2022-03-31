from time import sleep
from .robot import Robot
from pyautogui import click
from path_config import wines_assets


def run():
    robot = Robot(__file__, wines_assets)
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
