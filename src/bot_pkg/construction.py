from time import sleep

import pyautogui

from .robot import Robot
from path_config import CONSTRUCTION_ASSETS

def run():
    loops = 0  # You initialize loops to 0 right here and don't do the global thing
    robot = Robot(__file__, CONSTRUCTION_ASSETS)
    robot.setup_bot()

    sleep(2)

    def do_bank_stuff(robot):
        #sleep(0.4)
        robot.click("planks")
        sleep(0.5)
        robot.click("butler")
        sleep(0.6)
        pyautogui.typewrite("24")
        robot.press_key("enter")
        sleep(7.5)

    loops = loops + 1  # Here I add 1 to loops
    robot.click("build", mouse_btn="right")
    sleep(0.2)
    robot.click("button")
    sleep(0.55)
    robot.press_key("6")
    sleep(0.45)
    robot.click("remove", mouse_btn="right")
    sleep(0.2)
    robot.click("removebtn")
    sleep(0.55)
    robot.press_key("1")
    sleep(0.1)

    if loops == 4:
        do_bank_stuff(robot)
        loops = 0
        if robot.check_asset("pay"):
            do_bank_stuff(robot)
            loops = 0
