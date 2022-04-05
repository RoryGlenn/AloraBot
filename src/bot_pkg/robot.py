"""robot.py - ..."""

from typing import Any
import pyautogui
import json
from time import sleep
from os import chdir, path
from glob import glob
import pyautogui
from path_config import CONFIG as config_path


class Robot:
    """Robot - """
    def __init__(self, bot_name, path_file) -> None:
        self.bot_path = path_file
        self.bot_name = path.splitext(path.basename(bot_name))[0]

    def move_and_click(self, coords, numClicks, mouse_btn="left") -> None:
        pyautogui.moveTo(coords[0], coords[1], 0.15, pyautogui.easeInOutQuad)
        pyautogui.click(clicks=numClicks, interval=0.05, button=mouse_btn)

    def load_asset_images(self, name) -> list:
        return [img for img in glob(name + '*.png')]

    def load_config(self) -> Any:
        with open(config_path) as config:
            return json.load(config)[self.bot_name]

    def wait(self, asset) -> None:
        sleep_timers = self.load_config()["sleep_timers"]

        if asset in sleep_timers:
            sleep(sleep_timers[asset])

    def click(self, asset, numClicks=1, mouse_btn="left") -> None:
        print("Clicking " + asset + "...")

        images = self.load_asset_images(asset)

        while not images:
            input("Insert an image for " + asset + " and press enter")
            images = self.load_asset_images(asset)

        images_confidence = self.load_config()["confidence"]
        coords = None

        while not coords:
            for image in images:
                if not coords:
                    confidence = images_confidence["default_confidence"]

                    if asset in images_confidence:
                        confidence = images_confidence[asset]

                    coords = pyautogui.locateCenterOnScreen(
                        image, confidence=confidence)

        self.move_and_click(coords, numClicks, mouse_btn)
        self.wait(asset)

    def setup_bot(self, custom_setup=False) -> None:
        print("Starting bot...")
        chdir(self.bot_path)

        if custom_setup:
            custom_setup(self)

    def type(self, text) -> None:
        sleep(0.1)
        pyautogui.typewrite(text)

    def press_key(self, key) -> None:
        pyautogui.press(key)

    def type_thieve(self) -> None:
        sleep(0.1)
        pyautogui.typewrite(';;thieve')
        pyautogui.press('enter')
        sleep(2.5)

    def check_asset(self, asset, times=1) -> None:
        if not asset == 'continue':
            self.check_asset('continue')

        config = self.load_config()["confidence"]
        confidence = config["default_confidence"]

        if asset in config:
            confidence = config[asset]

        coords = pyautogui.locateCenterOnScreen(
            './' + asset + '.png', confidence=confidence)
        if coords:
            print("Clicking " + asset + "...")
            self.move_and_click(coords, times)
            self.wait(asset)
            return True

        return False

    def run_clicks(self, assets) -> None:
        for asset in assets:
            self.click(asset)
