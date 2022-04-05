"""log_frame.py - ..."""

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QScrollArea
from PySide6.QtCore import Qt, QMargins, Slot, QTimer

from style import stylesheet
from .log_entry import LogEntry
import utils


class LogFrame(QFrame):

    def __init__(self) -> None:
        super(LogFrame, self).__init__()
        self.setStyleSheet(stylesheet.log_bg)
        self.setFixedWidth(400)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.layout().setSpacing(10)
        self.layout().setContentsMargins(QMargins(10, 0, 10, 15))

        self._timer = QTimer()
        self._timer.setInterval(1000)
        self._timer.timeout.connect(self._update_time)

        self._title = QLabel('Bot Info')
        self._title.setStyleSheet(stylesheet.logo_text)
        utils.set_font(self._title, size=14)
        self.layout().addWidget(self._title)

        self._info_container = QFrame()
        self._info_container.setLayout(QHBoxLayout())
        self._info_container.layout().setSpacing(5)
        self._info_container.layout().setContentsMargins(QMargins(0, 0, 0, 0))
        self.layout().addWidget(self._info_container)

        self._skill_info = InfoWidget('skill/bot')
        self._time_info = InfoWidget('time elapsed')
        self._time_info.update_info('00:00')
        self._status_info = InfoWidget('status')
        self._status_info.update_info('stopped')

        self._info_container.layout().addWidget(self._skill_info)
        self._info_container.layout().addWidget(self._time_info)
        self._info_container.layout().addWidget(self._status_info)

        self._widget_wrapper = QFrame()
        self._widget_wrapper.setStyleSheet(stylesheet.transparent)
        self._widget_wrapper.setLayout(QVBoxLayout())
        self._widget_wrapper.layout().setAlignment(Qt.AlignTop)
        self._widget_wrapper.layout().setSpacing(5)
        self._widget_wrapper.layout().setContentsMargins(0, 0, 5, 0)

        self._scroll_area = QScrollArea()
        self._scroll_area.setFixedWidth(380)
        # self._scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self._scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._scroll_area.setWidgetResizable(True)

        self._scroll_area.setStyleSheet(stylesheet.scroll_area)
        self._scroll_area.setWidget(self._widget_wrapper)
        self.layout().addWidget(self._scroll_area)

        self._log_list = list()

        self._seconds = 0
        self._minutes = 0
        self._hours = 0

    def insert_log(self, txt: str, type_: str) -> None:
        aux = LogEntry(type_)
        log = txt.capitalize()
        aux.set_text(log)
        self._widget_wrapper.layout().insertWidget(0, aux)
        self._log_list.append(aux)

    def update_skill_bot(self, value: list) -> None:
        self._skill_info.update_info(f'{value[0].capitalize()}\n{value[1]}')

    def update_start(self, started) -> None:
        if started:
            self._status_info.update_info('started')
            self._timer.start()
        else:
            self._status_info.update_info('stopped')
            self._timer.stop()
            self._timer.setInterval(1000)
            self._time_info.update_info('00:00')

    @Slot()
    def _update_time(self) -> None:
        self._seconds += 1
        if self._seconds == 60:
            self._seconds = 0
            self._minutes += 1
            if self._minutes == 60:
                self._minutes = 0
                self._hours += 1

        if self._hours == 0:
            info = ''
        else:
            info = f'{self._hours}:'
        if self._minutes < 10:
            info = info + f'0{self._minutes}:'
        else:
            info = info + f'{self._minutes}:'
        if self._seconds < 10:
            info = info + f'0{self._seconds}'
        else:
            info = info + f'{self._seconds}'
        self._time_info.update_info(info)


class InfoWidget(QFrame):

    def __init__(self, title) -> None:
        super(InfoWidget, self).__init__()
        self.setLayout(QVBoxLayout())
        self.layout().setSpacing(5)
        self.layout().setContentsMargins(10, 10, 10, 10)
        self.setStyleSheet(stylesheet.info_widget)
        self.title = title

        self._title = QLabel()
        self._title.setText(title.upper())
        self._title.setStyleSheet(stylesheet.info_widget_labels)
        utils.set_font(self._title, size=8)
        self.layout().addWidget(self._title)

        self._info = QLabel()
        self._info.setMinimumHeight(30)
        self._info.setText(None)
        self._info.setStyleSheet(stylesheet.info_widget_labels)
        utils.set_font(self._info, size=8)
        self.layout().addWidget(self._info)

        if title == 'skill/bot':
            color = '#F24E1E'
        elif title == 'time elapsed':
            color = '#82D930'
        else:
            color = '#CA50D9'

        self._color_frame = QFrame()
        self._color_frame.setFixedHeight(4)
        self._color_frame.setStyleSheet(f'background: {color}; \
                                        border-radius: 2px')

        self.layout().addWidget(self._color_frame)

    def update_info(self, text: str) -> None:
        # if self.title == 'status':
        #    if text == 'stopped':
        #        self._info.setStyleSheet(f"""background: {colorscheme.transparent};
        #            color: {colorscheme.red_color}""")
        #    else:
        #        self._info.setStyleSheet(f"""background: {colorscheme.transparent};
        #            color: {colorscheme.green_color}""")

        self._info.setText(text)
