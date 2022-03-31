from PySide6.QtCore import QThread, QTimer, Signal, Slot
from bot_r import Bot_r


class Worker(QThread):
    stopped = Signal(bool)
    send_info_ = Signal(list)

    def __init__(self, handle):
        super().__init__()

        self.bot = Bot_r(handle)
        self.bot.stopped.connect(self.stopped_receiver)
        self.bot.send_info_.connect(self._info_receiver)
        self.stopped_sent = False

    def run(self):
        self.stopped_sent = False
        self.bot.run()

    def disable_bot(self):
        self.bot.disable_bot()

    @Slot()
    def stopped_receiver(self, value):
        if not self.stopped_sent:
            self.stopped_sent = True
            self.stopped.emit(value)
        self.terminate()

    def update_values(self, bot_name, step, mining_seconds):
        self.bot.update_values(bot_name, step, mining_seconds)

    @Slot()
    def _info_receiver(self, value: list):
        self.send_info_.emit(value)
