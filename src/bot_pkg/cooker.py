from time import sleep
from .robot import Robot
from pyautogui import click
from path_config import COOKER_ASSETS

robot = None

def run(setup):
    global robot
    
    if not setup:
        robot = Robot(__file__, COOKER_ASSETS)
        robot.setup_bot()

        sleep(3)

        robot.check_asset("option")
        sleep(0.5)
        click(958, 489, clicks=2)


    robot.click("fire")
    robot.press_key("1")
    sleep(67)
    robot.click("bank")
    robot.press_key("esc")

    # How to right click
    # robot.click("asset", mouse_btn="right")
