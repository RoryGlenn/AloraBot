from .robot import Robot
from path_config import seers_assets


def run():
    seers_robot = Robot(__file__, seers_assets)
    seers_robot.setup_bot()

    seers_robot.run_clicks(["home", "first", "second", "third"])
    seers_robot.check_asset("mark")
    seers_robot.run_clicks(["fourth", "fifth", "sixth"])
