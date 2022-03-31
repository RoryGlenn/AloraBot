from time import sleep

from .robot import Robot
import pyautogui
from path_config import pollivneach_assets


def run():
    polli_bot = Robot(__file__, pollivneach_assets)
    polli_bot.setup_bot()

    polli_bot.click("home")
    #sleep(0.3)
    polli_bot.click("compass")
    pyautogui.keyDown("up")
    sleep(1)
    polli_bot.run_clicks(["palm", "basket"])
    polli_bot.check_asset("coin")
    #sleep(3.5)
    polli_bot.run_clicks(["market", "banner", "gap", "tree", "wall", "ladder", "secondtree", "line"])
