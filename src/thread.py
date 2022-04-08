"""thread.py - """

from PySide6.QtCore import QThread, Signal, Slot

import pyautogui

from bot_r import Botr


class Worker(QThread):
    """Worker thread"""
    stopped = Signal(bool)
    send_info_ = Signal(list)

    def __init__(self, handle) -> None:
        super().__init__()

        self.bot = Botr(handle)
        self.bot.stopped.connect(self.stopped_receiver)
        self.bot.send_info_.connect(self._info_receiver)
        self.stopped_sent = False

    def mouseMoveEvent(self, event) -> None:
        self.label.setText('Mouse coords: ( %d : %d )' %
                           (event.x(), event.y()))

    def run(self) -> None:
        """Runs worker thread"""
        self.stopped_sent = False
        self.bot.run()

    def disable_bot(self) -> None:
        """Disables bot"""
        self.bot.disable_bot()

    @Slot()
    def stopped_receiver(self, value) -> None:
        """Stops receiver"""
        if not self.stopped_sent:
            self.stopped_sent = True
            self.stopped.emit(value)
        self.terminate()

    def update_values(self, bot_name, step, mining_seconds) -> None:
        """Updates bot values"""
        self.bot.update_values(bot_name, step, mining_seconds)

    @Slot()
    def _info_receiver(self, value: list) -> None:
        self.send_info_.emit(value)

    def enable_feedback(self) -> None:
        """Start mouse tracking"""

        # print("Press Ctrl-C to quit.")
        
        print("Enabled feedback")
        
        # try:
        #     while True:
        #         # Get and print the mouse coordinates.
        #         x, y = pyautogui.position()
        #         positionStr = "X: " + str(x).rjust(4) + \
        #                       ", Y: " + str(y).rjust(4)

        #         if not pyautogui.onScreen(x, y):
        #             # Pixel color can only be found for the primary monitor, and also not on mac due to the screenshot having the mouse cursor in the way.
        #             pixelColor = ("NaN", "NaN", "NaN")
        #         else:
        #             # NOTE: On Windows & Linux, getpixel() returns a 3-integer tuple, but on macOS it returns a 4-integer tuple.
        #             pixelColor = pyautogui.pyscreeze.screenshot().getpixel((x, y))

        #         positionStr += " RGB: (" + str(pixelColor[0]).rjust(3)
        #         positionStr += ", " + str(pixelColor[1]).rjust(3)
        #         positionStr += ", " + str(pixelColor[2]).rjust(3) + ")"

        #         print(positionStr)
        # except KeyboardInterrupt:
        #     print()

    def disable_feedback(self) -> None:
        """Stop mouse tracking"""
        # self.setMouseTracking(False)
        # self.close()
        
        print("Disabled feedback")
