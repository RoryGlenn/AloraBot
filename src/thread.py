"""thread.py - """

from PySide6.QtCore import QThread, Signal, Slot, QThreadPool, QTimer

import pyautogui
from mouse_thread import MouseWorker

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

        self.mouse_position_str = ''
        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(1)
        self.thread_stop = False
        print("Multithreading with maximum %d threads" %
              self.threadpool.maxThreadCount())

        # self.timer = QTimer()
        # # sets how often the gui will be updated with the new values
        # # when mouse tracking is enabled
        # self.timer.setInterval(1000)
        # self.timer.timeout.connect(self.recurring_timer)
        # self.timer.start()
        # self.mouse_counter = 0

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

    def set_mouse_position(self, progress_callback) -> None:
        # Get and print the mouse coordinates.
        while True:
            if self.thread_stop:
                break
            
            x, y = pyautogui.position()
            pos_x = "X: " + str(x).rjust(4)
            pos_y = "Y:" + str(y).rjust(4)
            position_str = pos_x + ', ' + pos_y

            if not pyautogui.onScreen(x, y):
                # Pixel color can only be found for the primary monitor, and also not on mac due to the screenshot having the mouse cursor in the way.
                pixelColor = ("NaN", "NaN", "NaN")
            else:
                # NOTE: On Windows & Linux, getpixel() returns a 3-integer tuple, but on macOS it returns a 4-integer tuple.
                pixelColor = pyautogui.pyscreeze.screenshot().getpixel((x, y))

            r = str(pixelColor[0]).rjust(3)
            g = str(pixelColor[1]).rjust(3)
            b = str(pixelColor[2]).rjust(3)

            self.mouse_position_str = position_str + " RBG: (" + \
                r + ', ' + \
                g + ', ' + \
                b + ')'

            print(self.mouse_position_str)
        
        self.thread_stop = False

    def print_output(self, s):
        print(s)

    def progress_fn(self, n):
        print("%d%% done" % n)

    def thread_complete(self):
        print("Mouse Tracking Finished!")

    def recurring_timer(self):
        self.mouse_counter += 1
        # self.l.setText("Counter: %d" % self.mouse_counter)
        print("Counter: %d" % self.mouse_counter)

    def enable_feedback(self) -> None:
        """Initializes mouse worker thread"""

        print("Enabled feedback")

        # Pass the function to execute
        # Any other args, kwargs are passed to the run function
        worker = MouseWorker(self.set_mouse_position)
        # worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        # worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

    def disable_feedback(self) -> None:
        """Stop mouse tracking"""
        print("Disabled feedback")
        self.thread_stop = True
        
