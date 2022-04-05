"""woodcutter.py - ..."""

from .robot import Robot


def run() -> None:
    wc = Robot(__file__)
    wc.setup_bot()

    wc.click("one")
    if wc.check_asset("one") == False:
        wc.click("two")
        if wc.check_asset("two") == False:
            wc.click("three")
