from .robot import Robot
from time import sleep
from path_config import woodcutter_assets


def run():
    wc = Robot(__file__)
    wc.setup_bot()

    wc.click("one")
    if wc.check_asset("one") == False:
        wc.click("two")
        if wc.check_asset("two") == False:
            wc.click("three")
