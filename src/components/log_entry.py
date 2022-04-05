"""log_entry.py - ..."""

from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

from utils import set_font
from style import stylesheet


class LogEntry(QFrame):

    def __init__(self, type_='success') -> None:
        super(LogEntry, self).__init__()
        self.setFixedHeight(35)
        self.setLayout(QHBoxLayout())
        self.layout().setSpacing(5)
        self.layout().setContentsMargins(5, 0, 5, 0)
        self.setStyleSheet(stylesheet.log_widget)

        self._color_container = QFrame()
        self._color_container.setFixedWidth(4)
        self._color_container.setStyleSheet(stylesheet.reset_style)
        self._color_container.setLayout(QVBoxLayout())
        self._color_container.layout().setSpacing(3)
        self._color_container.layout().setContentsMargins(0, 4, 0, 4)
        self.layout().addWidget(self._color_container)

        self._color = QFrame()
        self._color.setFixedHeight(15)
        self._color_container.layout().addWidget(self._color)
        if type_ == 'success':
            self._color.setStyleSheet(stylesheet.log_success)
        else:
            self._color.setStyleSheet(stylesheet.log_error)

        self._aux_color = QFrame()
        self._aux_color.setStyleSheet(stylesheet.log_aux)
        self._color_container.layout().addWidget(self._aux_color)

        self._info_container = QFrame()
        self._info_container.setStyleSheet(stylesheet.reset_style)
        self._info_container.setLayout(QHBoxLayout())
        self._info_container.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self._info_container)
        self._info_label = QLabel()
        set_font(self._info_label, size=10)
        self._info_label.setStyleSheet('color: #FFFFFF')
        self._info_container.layout().addWidget(
            self._info_label, alignment=Qt.AlignLeft)

    def set_text(self, text: str) -> None:
        self._info_label.setText(text.capitalize())
