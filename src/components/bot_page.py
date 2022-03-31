from functools import partial
import keyboard
from thread import Worker

from PySide6.QtWidgets import (
    QFrame, QToolButton, QLabel, QVBoxLayout, QGridLayout,
    QComboBox, QPushButton, QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt, QSize, QMargins, Slot, QRect, QPoint, Signal
from PySide6.QtGui import QPixmap, QColor


from style import stylesheet
import utils
from .popup_alerts import AlertPopup


class BotPage(QFrame):
    def __init__(self, parent, bot_handle):
        super(BotPage, self).__init__()
        self.parent = parent
        self.setStyleSheet(stylesheet.transparent)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.layout().setSpacing(100)
        self.layout().setContentsMargins(QMargins(10, 10, 10, 10))

        self._worker = Worker(self)
        self._worker.stopped.connect(self._worker_stopped_handle)
        self._worker.send_info_.connect(self._insert_log)
        self._bot_name = str()
        self._bot_handle = bot_handle

        # self._key_start = QShortcut(QKeySequence('1'), self)
        # self._key_start.activated.connect(self._keyboard_controller)
        #
        # self._key_stop = QShortcut(QKeySequence('2'), self)
        # self._key_stop.activated.connect(self._keyboard_controller)
        self._key_start = keyboard.add_hotkey(
            'underscore', self._keyboard_controller)
        self._key_stop = keyboard.add_hotkey(
            'equal', self._keyboard_controller)

        self._btns_frame = QFrame()
        self._btns_frame.setLayout(QGridLayout())
        self._btns_frame.layout().setSpacing(10)
        self._btns_frame.layout().setContentsMargins(QMargins(0, 0, 0, 0))
        self.layout().addWidget(self._btns_frame)

        self._skills_title = QLabel('skills'.capitalize())
        self._skills_title.setStyleSheet(stylesheet.logo_text)
        utils.set_font(self._skills_title, size=12)

        self._mining_btn = CustomSkillButton('mining')
        self._runecrafting_btn = CustomSkillButton('runecrafting')
        self._hunter_btn = CustomSkillButton('hunter')
        self._agility_btn = CustomSkillButton('agility')
        self._cooking_btn = CustomSkillButton('cooking')
        self._construction_btn = CustomSkillButton('construction')
        self._smithing_btn = CustomSkillButton('smithing')
        self._woodycutting_btn = CustomSkillButton('woodycutting')

        for btn in [self._mining_btn, self._runecrafting_btn, self._hunter_btn, self._agility_btn,
                    self._cooking_btn, self._construction_btn, self._smithing_btn, self._woodycutting_btn]:
            func = partial(self._update_pos_spawn, btn.objectName())
            btn.clicked.connect(func)
            btn.send_info.connect(self._info_receiver)

        self._btns_frame.layout().addWidget(self._skills_title, 0, 0)
        self._btns_frame.layout().addWidget(self._mining_btn, 1, 0)
        self._btns_frame.layout().addWidget(self._runecrafting_btn, 1, 1)
        self._btns_frame.layout().addWidget(self._hunter_btn, 1, 2)
        self._btns_frame.layout().addWidget(self._agility_btn, 1, 3)
        self._btns_frame.layout().addWidget(self._cooking_btn, 2, 0)
        self._btns_frame.layout().addWidget(self._construction_btn, 2, 1)
        self._btns_frame.layout().addWidget(self._smithing_btn, 2, 2)
        self._btns_frame.layout().addWidget(self._woodycutting_btn, 2, 3)

        self._start_container = QFrame()
        self._start_container.setLayout(QVBoxLayout())
        self._start_container.layout().setSpacing(10)
        self._start_container.layout().setAlignment(Qt.AlignCenter)
        self._start_container.layout().setContentsMargins(QMargins(0, 0, 0, 0))
        self.layout().addWidget(self._start_container)

        self._step_title = QLabel('Current step:'.capitalize())
        self._step_title.setStyleSheet(stylesheet.logo_text)
        utils.set_font(self._step_title, size=10)
        self._start_container.layout().addWidget(self._step_title)

        self._step_combo = QComboBox()
        self._step_combo.setFixedSize(200, 30)
        utils.set_font(self._step_combo, size=10)
        self._step_combo.setStyleSheet(stylesheet.step_combo)
        self._start_container.layout().addWidget(self._step_combo)

        self._start_btn = CustomStartButton()
        self._start_btn.clicked.connect(self._start_btn_handle)
        self._start_container.layout().addWidget(
            self._start_btn, alignment=Qt.AlignCenter)

        self._start_mouse_info = QPushButton('start mouse info'.capitalize())
        self._start_mouse_info.setStyleSheet(stylesheet.mouse_btn)
        utils.set_font(self._start_mouse_info, size=8, italic=True)
        self._start_mouse_info.setCursor(Qt.PointingHandCursor)
        self._start_mouse_info.clicked.connect(self._mouse_info_handle)
        self._start_container.layout().addWidget(self._start_mouse_info)

        self._mouse_info_enabled = False

        self._steps_list = {'Dense Ess': ["Find Wizard", "Fast Travel",
                                          "Climb Rock", "Walk to Runestone", "Mine", "Teleport Home",
                                          "Bank Deposit"], 'Pollivneach': ["Base", "Barrel"],
                            'Donator Zone': ["Set Traps"]}

        self._mining_seconds_popup = AlertPopup(
            self.parent, 'Fill in', 'Seconds spend on mining')
        self._mining_seconds_popup.send_seconds.connect(self._seconds_receiver)
        self._seconds_mining = None

    @Slot()
    def _insert_log(self, values: list):
        msg = values[0]
        type_ = values[1]
        self._bot_handle.insert_log(msg, type_)

    @Slot()
    def _start_btn_handle(self):
        if self._start_btn.started:
            self._worker.update_values(bot_name=self._bot_name, step=self._step_combo.currentText(),
                                       mining_seconds=self._seconds_mining)
            self._worker.start()
            self._bot_handle.update_start(True)
            self._insert_log(['Bot started', 'success'])
        else:
            self._worker.disable_bot()

    def _keyboard_controller(self):
        self._start_btn.mousePressEvent()
        self._start_btn.click()

    @Slot()
    def _update_pos_spawn(self, object_name: str):
        for btn in [self._mining_btn, self._runecrafting_btn, self._hunter_btn, self._agility_btn,
                    self._cooking_btn, self._construction_btn, self._smithing_btn, self._woodycutting_btn]:
            if object_name == btn.objectName():
                sender = btn
                break
        pos_spawn = sender.mapToGlobal(QPoint(0, 0))
        sender.update_popup(pos_spawn)

    @Slot()
    def _seconds_receiver(self, value: int):
        self._seconds_mining = value

    @Slot()
    def _info_receiver(self, data_list):
        self._bot_handle.update_skill_bot(data_list)
        for k, v in self._steps_list.items():
            self._clean_step_combo()
            if k == data_list[1]:
                self._step_combo.addItems(v)
                break
        self._bot_name = data_list[1]
        if data_list[1] == 'Dense Ess':
            self._mining_seconds_popup.show()

    @Slot()
    def _mouse_info_handle(self):
        if self._mouse_info_enabled:
            self._mouse_info_enabled = False
            self._start_mouse_info.setText('start mouse info'.capitalize())
            # stop feedback
            self._worker.disable_feedback()
        else:
            self._mouse_info_enabled = True
            self._start_mouse_info.setText('stop mouse info'.capitalize())
            # start feedback
            self._worker.enable_feedback()

    def _clean_step_combo(self):
        while (self._step_combo.count() != 0):
            self._step_combo.removeItem(0)

    @Slot()
    def _worker_stopped_handle(self):
        self._start_btn.set_start()
        self._bot_handle.update_start(False)
        self._insert_log(['Bot stopped', 'success'])


class CustomSkillButton(QToolButton):
    send_info = Signal(list)

    def __init__(self, title):
        super(CustomSkillButton, self).__init__()
        self.setFixedSize(QSize(70, 70))
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(stylesheet.btn_skill)

        self._title = title
        self.setObjectName(self._title)
        # self.setIcon(QPixmap(f':/images/{title}.png'))
        self.setIcon(QPixmap(f'src/resources/images/{title}.png'))
        self.setIconSize(QSize(40, 40))

        self._popup = None

        self._bot_data = {'mining': ['Dense Ess'],
                          'runecrafting': ["Bloods", "Runecrafting"],
                          'hunter': ["Donator Zone"],
                          'agility': ["Pollivneach", "Seers", "Ardouge"],
                          'cooking': ["Wines", "Cooker"],
                          'construction': ["Construction"],
                          'smithing': ["Smithing"],
                          'woodycutting': ["Woodcutting"]}

    def update_popup(self, pos_spawn):
        self._popup = BotPopUp(
            *self._bot_data[self._title], pos_spawn=pos_spawn)
        self._popup.send_info.connect(self._send_data)
        self._popup.show()

    @Slot()
    def _send_data(self, bot_name):
        self.send_info.emit([self._title, bot_name])


class CustomStartButton(QPushButton):

    def __init__(self):
        super(CustomStartButton, self).__init__()
        self.setFixedSize(QSize(120, 35))
        self.setText('Start')
        self.setStyleSheet(stylesheet.start_btn_default)
        utils.set_font(self, size=13)
        self.setCursor(Qt.PointingHandCursor)

        self.started = False

    def mousePressEvent(self, e=None) -> None:
        if not self.started:
            self.started = True
            self.setText('Stop')
            self.setStyleSheet(stylesheet.stop_btn_default)
        else:
            self.started = False
            self.setText('Stopping')
            self.setStyleSheet(stylesheet.stop_btn_default)

        if e != None:
            return super().mousePressEvent(e)

    def set_start(self):
        self.started = False
        self.setText('Start')
        self.setStyleSheet(stylesheet.start_btn_default)


class BotPopUp(QFrame):
    """Custom popup for the more menu button.
    """

    send_info = Signal(str)

    def __init__(self, *args, **kwargs):
        super(BotPopUp, self).__init__()

        self._bot_list = args

        width = (len(self._bot_list) * 5 + len(self._bot_list) * 35) + 60

        # config
        self.setGeometry(QRect(kwargs['pos_spawn'], QSize(120, width)))
        self.setFixedSize(QSize(120, width))

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setObjectName('main_layout')
        self.main_layout.setContentsMargins(5, 15, 15, 5)
        self.main_layout.setSpacing(0)

        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowStaysOnTopHint | Qt.NoDropShadowWindowHint | Qt.Popup)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.bg_container = QFrame(self)
        self.bg_container.setObjectName('bg_container')
        self.bg_container.setStyleSheet(stylesheet.bot_popup)
        self.main_layout.addWidget(self.bg_container)

        self.bg_layout = QVBoxLayout(self.bg_container)
        self.bg_layout.setObjectName('bg_layout')
        self.bg_layout.setContentsMargins(5, 5, 5, 5)
        self.bg_layout.setSpacing(5)
        self.bg_layout.setAlignment(Qt.AlignTop)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(6)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.bg_container.setGraphicsEffect(self.shadow)

        self._info_label = QLabel('Select bot:')
        self._info_label.setStyleSheet(stylesheet.logo_text)
        utils.set_font(self._info_label, size=10)
        self._info_label.setMinimumSize(QSize(90, 25))
        self.bg_layout.addWidget(self._info_label)

        self._btn_list = list()

        for i in range(len(self._bot_list)):
            aux = QPushButton()
            aux.setObjectName(self._bot_list[i])
            aux.setMinimumSize(QSize(90, 35))
            aux.setCursor(Qt.PointingHandCursor)
            aux.setText(self._bot_list[i])
            aux.setStyleSheet(stylesheet.bot_popup_btn)
            aux.partial_func = partial(self._send_info, self._bot_list[i])
            aux.clicked.connect(aux.partial_func)
            self.bg_layout.addWidget(aux)
            self._btn_list.append(aux)

    def _send_info(self, info):
        self.send_info.emit(info)
        self.close()
