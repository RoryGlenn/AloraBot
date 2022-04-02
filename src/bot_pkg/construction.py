"""construction.py - ..."""

from time import sleep

import pyautogui

from .robot import Robot
from path_config import CONSTRUCTION_ASSETS

SLEEP_TIME = 0.5

def run():
    loops = 0  # You initialize loops to 0 right here and don't do the global thing
    robot = Robot(__file__, CONSTRUCTION_ASSETS)
    robot.setup_bot()

    sleep(SLEEP_TIME + 1.5)

    def do_bank_stuff(robot):
        robot.click("planks")
        sleep(SLEEP_TIME)
        robot.click("butler")
        sleep(SLEEP_TIME)
        pyautogui.typewrite("24")
        robot.press_key("enter")
        sleep(SLEEP_TIME + 7)

    loops = loops + 1  # Here I add 1 to loops
    robot.click("build", mouse_btn="right")
    sleep(SLEEP_TIME)
    robot.click("button")
    sleep(SLEEP_TIME)
    robot.press_key("6")
    sleep(SLEEP_TIME)
    robot.click("remove", mouse_btn="right")
    sleep(SLEEP_TIME)
    robot.click("removebtn")
    sleep(SLEEP_TIME)
    robot.press_key("1")
    sleep(SLEEP_TIME)

    if loops == 4:
        do_bank_stuff(robot)
        loops = 0
        if robot.check_asset("pay"):
            do_bank_stuff(robot)
            loops = 0
