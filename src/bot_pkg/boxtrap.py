"""boxtrap.py - ..."""

import pyautogui

from .robot import Robot
from time import sleep


def custom_setup(robot):
    robot.click('configbtn', 2)


def find_green(x, y, state, jump, box_traps):
    search_y = y

    for i in range(1, box_traps + 1):
        print("searching from " + str(search_y))
        if pyautogui.pixelMatchesColor(x, search_y, (55, 149, 11), tolerance=25):
            print("found in " + str(i))
            found = {
                "x": x,
                "y": search_y,
                "next_state": i
            }

            return found
        search_y += jump

    return None


def run():
    # pyautogui.mouseInfo()

    box_traps = 5
    box_robot = Robot(__file__)
    box_robot.setup_bot(custom_setup)

    box_robot.click_for("boxtrap", box_traps)
    sleep(3)

    x = 670
    y = 419
    jump = 25
    state = 1

    while True:
        found = None
        while not found:
            found = find_green(x, y, state, jump, box_traps)

        y = y + (jump - (state * jump))
        state = found["next_state"]

        pyautogui.moveTo(found["x"], found["y"] - 3, 0.15, pyautogui.easeInOutQuad)
        pyautogui.click(button="right")
        sleep(1)
        pyautogui.moveTo(found["x"], found["y"] + 37, 0.15, pyautogui.easeInOutQuad)
        pyautogui.click()
        sleep(9)
