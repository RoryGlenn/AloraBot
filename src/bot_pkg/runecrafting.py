"""runecrafting.py - """


from .robot import Robot
from path_config import RUNECRAFTING_ASSETS


def custom_setup(robot) -> None:
    robot.click('configbtn', 2)
    robot.click('itemsbtn')


def run() -> None:
    rune_robot = Robot(__file__, RUNECRAFTING_ASSETS)
    rune_robot.setup_bot(custom_setup)

    rune_robot.type_thieve()

    # We need to first click chest
    rune_robot.click("chest")
    # Now we need to hit ESC key, we don't have an implementation for that, so let's make one:
    rune_robot.press_key("esc")
    # Now we do the pouches part and reopening chest
    rune_robot.run_clicks(["giant", "large", "med", "bank"])
    # We will close the chest with ESC once again
    rune_robot.press_key("esc")
    # Now we can continue with the rest of clicks
    rune_robot.run_clicks(["mage", "deathrune", "altar"])

    # rune_robot.run_clicks(["chest", "giant", "large", "med", "mage", "deathrune", "altar"])
    rune_robot.check_asset("continue")
