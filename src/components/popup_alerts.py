from PySide6.QtWidgets import QFrame, QStyle, QLabel, QVBoxLayout, QGraphicsDropShadowEffect, QPushButton, QLineEdit
from PySide6.QtCore import QSize, Qt, Slot, Signal, QRegularExpression
from PySide6.QtGui import QGuiApplication, QColor, QRegularExpressionValidator
from PySide6.QtSvgWidgets import QSvgWidget

import utils
from style import stylesheet


class AlertPopup(QFrame):

    send_seconds = Signal(int)

    def __init__(self, parent, title, info):
        super(AlertPopup, self).__init__(parent=parent)

        self.setObjectName('alert_dialog')
        self.setFixedSize(QSize(305, 284))
        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.Popup | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setLayout(QVBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(10, 10, 10, 10)

        self._bg_container = QFrame(self)
        self._bg_container.setStyleSheet(stylesheet.app_bg)
        self._bg_container.setLayout(QVBoxLayout())
        self._bg_container.layout().setSpacing(0)
        self._bg_container.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self._bg_container)
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(6)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self._bg_container.setGraphicsEffect(self.shadow)
        self._bg_container.setLayout(QVBoxLayout())
        self._bg_container.layout().setSpacing(20)
        self._bg_container.layout().setAlignment(Qt.AlignCenter)
        self._bg_container.layout().setContentsMargins(0, 0, 0, 0)

        self._content_container = QFrame()
        self._content_container.setLayout(QVBoxLayout())
        self._content_container.layout().setSpacing(10)
        self._content_container.layout().setContentsMargins(0, 0, 0, 0)
        self._bg_container.layout().addWidget(self._content_container)

        self._icon = QSvgWidget('src/resources/images/warning.svg')
        self._icon.setFixedSize(QSize(72, 72))
        self._content_container.layout().addWidget(
            self._icon, alignment=Qt.AlignHCenter)

        self._title = QLabel(title.capitalize())
        utils.set_font(self._title, size=12)
        self._title.setAlignment(Qt.AlignCenter)
        self._title.setStyleSheet(stylesheet.logo_text)
        self._content_container.layout().addWidget(self._title)

        self._info = QLabel(info.capitalize())
        utils.set_font(self._info, size=10)
        self._info.setAlignment(Qt.AlignCenter)
        self._info.setStyleSheet(stylesheet.logo_text)
        self._content_container.layout().addWidget(self._info)

        self._entry = QLineEdit()
        self._entry.setFixedSize(QSize(180, 32))
        self._entry.setStyleSheet(stylesheet.entry_seconds_spend)
        self._entry.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        utils.set_font(self._entry, size=10)
        self._content_container.layout().addWidget(
            self._entry, alignment=Qt.AlignHCenter)

        self._confirm_btn = QPushButton()
        self._confirm_btn.setText('confirm'.capitalize())
        self._confirm_btn.setFixedSize(QSize(62, 32))
        self._confirm_btn.setStyleSheet(stylesheet.default_btn)
        utils.set_font(self._confirm_btn, size=10)
        self._confirm_btn.setCursor(Qt.PointingHandCursor)
        self._btn_shadow = QGraphicsDropShadowEffect()
        self._btn_shadow.setBlurRadius(6)
        self._btn_shadow.setXOffset(0)
        self._btn_shadow.setYOffset(0)
        self._btn_shadow.setColor(QColor(0, 0, 0, 60))
        self._confirm_btn.setGraphicsEffect(self._btn_shadow)
        self._bg_container.layout().addWidget(
            self._confirm_btn, alignment=Qt.AlignHCenter)
        self._confirm_btn.clicked.connect(self._close)

    def showEvent(self, arg__1) -> None:
        parent = self.parent()

        if parent:
            rect = parent.geometry()
            self.move(rect.center() - self.rect().center())
        else:
            self.setGeometry(QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                self.size(),
                QGuiApplication.primaryScreen().availableGeometry(),
            ))

    @Slot()
    def _close(self):
        self.send_seconds.emit(int(self._entry.text()))
        self._entry.setText('')
        self.close()
