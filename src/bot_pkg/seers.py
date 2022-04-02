"""seers.py - ..."""

from .robot import Robot
from path_config import SEERS_ASSETS


def run():
    seers_robot = Robot(__file__, SEERS_ASSETS)
    seers_robot.setup_bot()

    seers_robot.run_clicks(["home", "first", "second", "third"])
    seers_robot.check_asset("mark")
    seers_robot.run_clicks(["fourth", "fifth", "sixth"])
