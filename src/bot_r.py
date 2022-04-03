"""bot_r.py - ..."""

from PySide6.QtCore import QTimer, Signal, Slot, QObject

import pyautogui
import keyboard

from bot_pkg import *


class Botr(QObject):
    """Botr"""
    stopped = Signal(bool)
    start_dense = Signal(bool)
    stop_dense = Signal(bool)
    start_pollivneach = Signal(bool)
    stop_pollivneach = Signal(bool)
    send_info_ = Signal(list)

    def __init__(self, parent):
        super(Botr, self).__init__()

        self._timer_feedback = QTimer()
        self._timer_feedback.setInterval(100)
        self._timer_feedback.timeout.connect(self._print_feedback)
        self.parent = parent

        self._timer_dense_ess_bot = QTimer()
        self._timer_dense_ess_bot.timeout.connect(self._dense_ess_start)
        self.start_dense.connect(self._start_dense_timer)
        self.stop_dense.connect(self._stop_dense_timer)
        self._timer_pollivneach_bot = QTimer()
        self.start_pollivneach.connect(self._start_pollivneach_timer)
        self.stop_pollivneach.connect(self._stop_pollivneach_timer)

        # self._mouse = Controller()
        self._bot_active = False
        self._feedback_active = False
        self._game_started = False
        self._current_phase = 'Base'
        self._default_x = 1366
        self._default_y = 768
        self._seconds_mining = 140
        self._bot_name = str()
        self._step = str()

        self._mark_of_grace = False
        self._box_count = 0

        self._setup = False
        self._wait_color = 0
        self._default_attempts = 0
        self._waiting = False
        self._start_emited = False

        self.orient = basic_functions.Orient()

        # why was this variable not defined in init
        # before RMG started working on the project?
        self._key_stop = None

    def run(self):
        """Run"""
        # global botActive, secondsMining, currentPhase, waiting
        # send to logger
        # label_feedback.config(text="The bot has been \
        # activated!\nUse the - key to stop the bot.")
        self._bot_active = True
        self._key_stop = keyboard.add_hotkey('equal', self.disable_bot)

        # bot config
        if self._bot_name == "Dense Ess":
            if self._step == "Find Wizard":
                self._current_phase = "Base"
                self._waiting = False

            elif self._step == "Fast Travel":
                self._current_phase = "Base"
                self._waiting = True

            elif self._step == "Climb Rock":
                self._current_phase = "RockHop"
                self._waiting = False

            elif self._step == "Walk to Runestone":
                self._current_phase = "MinesMap"
                self._waiting = False

            elif self._step == "Mine":
                self._current_phase = "Large Rock"
                self._waiting = False

            elif self._step == "Teleport Home":
                self._current_phase = "Teleport Home"
                self._waiting = False

            elif self._step == "Bank Deposit":
                self._current_phase = "Bank"
                self._waiting = False

            # basic_functions.down_orient()
            self.orient.down_orient()
            self._dense_ess_start()

        elif self._bot_name == "Pollivneach":
            if self._step == 'Base':
                self._current_phase = 'Base'
            elif self._step == 'Barrel':
                self._current_phase = 'Barrel'
                
            # basic_functions.down_orient()
            # basic_functions.up_orient()
            self.orient.down_orient()
            self.orient.up_orient()
            self._pollivneach_start()

        elif self._bot_name == "Donator Zone":
            self._hunting_start()

        elif self._bot_name == "Bloods":
            self._bloods_start()

        elif self._bot_name == "Runecrafting":
            self._runecrafting_start()

        elif self._bot_name == "Seers":
            self._seers_start()

        elif self._bot_name == "Cooker":
            self._cooker_start()

        elif self._bot_name == "Construction":
            self._construction_start()

        elif self._bot_name == "Smithing":
            self._smithing_start()

        elif self._bot_name == "Wines":
            self._wines_start()

        elif self._bot_name == "Ardouge":
            self._ardouge_start()

        elif self._bot_name == "Woodcutter":
            self._woodcutter_start()

    def disable_bot(self):
        """Resets variables"""
        # label_feedback.config(text="The bot has been disabled") send to log
        self._bot_active = False
        self._waiting = False
        self._setup = False
        self._current_phase = "Base"

    def send_info(self, value: list):
        """Sends info"""
        self.send_info_.emit(value)

    def update_values(self,
                      bot_name: str,
                      step: str,
                      mining_seconds: int = 140) -> None:
        """Updates bot values"""
        self._bot_name = bot_name
        self._seconds_mining = mining_seconds
        self._step = step

    @Slot()
    def _start_dense_timer(self) -> None:
        self._timer_dense_ess_bot.start()
        self._start_emited = True

    @Slot()
    def _stop_dense_timer(self) -> None:
        self._timer_dense_ess_bot.stop()
        self._start_emited = False

    @Slot()
    def _start_pollivneach_timer(self) -> None:
        self._start_emited = True
        self._timer_pollivneach_bot.start()

    @Slot()
    def _stop_pollivneach_timer(self) -> None:
        self._timer_pollivneach_bot.stop()
        self._start_emited = False

    def enable_feedback(self) -> None:
        """Enable the print feedback"""
        self._feedback_active = True
        self._timer_feedback.start()

    def disable_feedback(self) -> None:
        """Disable print feedback"""
        self._feedback_active = False

    def _keyboard_controller(self):
        self._bot_active = False

    def _print_feedback(self) -> None:
        """Qtimer call function for mouse feedback """
        if self._feedback_active:
            _x, _y = pyautogui.position()
            # x += 95
            # y += 41
            color = pyautogui.screenshot()
            color = color.getpixel((_x, _y))
            _ss = 'X: ' + str(_x).rjust(4) + ' Y: ' + str(_y).rjust(4)
            _ss += ' RGB: (' + str(color[0]).rjust(3)
            _ss += ', ' + str(color[1]).rjust(3)
            _ss += ', ' + str(color[2]).rjust(3) + ')'

            # label_mouse_info.config(text=ss);
            # probably send to log
        if not self._feedback_active:
            self._timer_feedback.stop()

    def _close_thread(self) -> None:
        self.stopped.emit(True)

    def _dense_ess_start(self) -> None:
        """Dense ess bot handle"""
        reset_timer = denseEssProcess(
            self._current_phase, self._waiting, self._seconds_mining, self)
        self._timer_dense_ess_bot.setInterval(reset_timer)
        if self._bot_active:
            if not self._start_emited:
                self.start_dense.emit(True)
        else:
            self.stop_dense.emit(True)
            self._close_thread()

    def _pollivneach_start(self) -> None:
        """Pollivneach bot handle"""
        reset_timer = pollivneachCourseFile.pollinveachCourse(
            self._current_phase, self)
        self._timer_pollivneach_bot.setInterval(reset_timer)
        self._timer_pollivneach_bot.timeout.connect(self._pollivneach_start)
        if self._bot_active:
            if not self._start_emited:
                self.start_pollivneach.emit(True)
        else:
            self.stop_pollivneach.emit(True)
            self._close_thread()

    def _hunting_start(self) -> None:
        """Hunting bot handle"""
        if self._bot_active:
            RunescapeGame.start(self._setup, self)
            if not self._setup:
                self._setup = True
            self._hunting_start()
        else:
            self._close_thread()

    def _bloods_start(self) -> None:
        """Blood bot handle"""
        if self._bot_active:
            bloods.run(self)
            self._bloods_start()
        else:
            self._close_thread()

    def _runecrafting_start(self) -> None:
        """Runecrafting bot handle"""
        print('trying renecraft bot')
        if self._bot_active:
            runecrafting.run()
            self._runecrafting_start()
        else:
            self._close_thread()

    def _seers_start(self) -> None:
        """Seers bot handle"""
        if self._bot_active:
            seers.run()
            self._seers_start()
        else:
            self._close_thread()

    def _cooker_start(self) -> None:
        """Cooker bot handle"""
        if self._bot_active:
            cooker.run(self._setup)
            if not self._setup:
                self._setup = True
            self._cooker_start()
        else:
            self._close_thread()

    def _construction_start(self) -> None:
        """Construction bot handle"""
        if self._bot_active:
            construction.run()
            self._construction_start()
        else:
            self._close_thread()

    def _smithing_start(self) -> None:
        """Smithing bot handle"""
        if self._bot_active:
            smithing.run()
            self._smithing_start()
        else:
            self._close_thread()

    def _wines_start(self) -> None:
        """Wine bot handle"""
        if self._bot_active:
            wines.run()
            self.wines_start()
        else:
            self._close_thread()

    def _ardouge_start(self) -> None:
        """Ardouge bot handle"""
        if self._bot_active:
            ardouge.run()
            self._ardouge_start()
        else:
            self._close_thread()

    def _woodcutter_start(self) -> None:
        """Woodcutter bot handle"""
        if self._bot_active:
            woodcutter.run()
            self._woodcutter_start()
        else:
            self._close_thread()
