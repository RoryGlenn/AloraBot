import pyautogui

from .robot import Robot
from time import sleep
from path_config import BLOODS_ASSETS


def run(logger):
    log_handle = logger
    loops = 0
    rune_robot = Robot(__file__, BLOODS_ASSETS)
    rune_robot.setup_bot()
    sleep(3)

    # typing thieve as starting point
    rune_robot.type_thieve()
    # clicking compass and fixing camera angle before every run
    rune_robot.click("compass")
    pyautogui.keyDown("up")
    sleep(1)
    # click chest
    rune_robot.click("chest")
    # clicking esc to get out of bank
    rune_robot.press_key("esc")
    # moving mouse to dense ess coord
    loops = 1
    while loops != 27:
        print(loops)
        loops = loops + 1
        pyautogui.moveTo(1027, 665)
        # clicking the dense ess
        pyautogui.click(1027, 665)
        # moving mouse to chisel
        pyautogui.moveTo(1026, 630)
        # clicking chisel
        pyautogui.click(1026, 630)
    if loops == 27:
        rune_robot.click("bank")
        rune_robot.press_key("esc")
        loops = 1
    while loops != 27:
        loops = loops + 1
        pyautogui.moveTo(1027, 665)
        # clicking the dense ess
        pyautogui.click(1027, 665)
        # moving mouse to chisel
        pyautogui.moveTo(1026, 630)
        # clicking chisel
        pyautogui.click(1026, 630)
    if loops == 27:
        rune_robot.click("bank")
        rune_robot.press_key("esc")
        loops = 2
    if loops == 2:
        rune_robot.click("mage")
        pyautogui.moveTo(590, 342)
        pyautogui.click(590, 342)
        sleep(3.3)
        rune_robot.click("altar")
        rune_robot.click("blood")
        rune_robot.check_asset("continue")
        loops = 3
    if loops == 3:
        while loops != 29:
            loops = loops + 1
            pyautogui.moveTo(1027, 665)
            # clicking the dense ess
            pyautogui.click(1027, 665)
            # moving mouse to chisel
            pyautogui.moveTo(1026, 630)
            # clicking chisel
            pyautogui.click(1026, 630)
        if loops == 29:
            rune_robot.click("bloodclose")
            sleep(1.8)
            rune_robot.check_asset("continue")
            loops = 0








