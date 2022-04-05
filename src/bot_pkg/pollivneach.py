"""pollivneach.py - ..."""

from time import sleep

from .robot import Robot
import pyautogui
from path_config import POLLIVNEACH_ASSETS


def run() -> None:
    polli_bot = Robot(__file__, POLLIVNEACH_ASSETS)
    polli_bot.setup_bot()

    polli_bot.click("home")
    polli_bot.click("compass")
    pyautogui.keyDown("up")
    sleep(1)
    
    polli_bot.run_clicks(["palm", "basket"])
    polli_bot.check_asset("coin")
    polli_bot.run_clicks(
        ["market", "banner", "gap", "tree",
         "wall", "ladder", "secondtree", "line"])
