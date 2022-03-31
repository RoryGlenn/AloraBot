from PySide6.QtWidgets import QFrame, QHBoxLayout, QStackedWidget, QVBoxLayout
from PySide6.QtCore import QSize, Qt, QMargins
from PySide6.QtGui import QIcon

from style import stylesheet
import components


class UiApp(object):

	def init_gui(self, app):

		app.setWindowTitle('Runescape Bot')
		app.setWindowIcon(QIcon(':/images/logo.ico'))
		app.setObjectName('main_app')
		app.setMinimumSize(QSize(1000, 585))
		app.setWindowFlags(Qt.FramelessWindowHint)
		app.setAttribute(Qt.WA_TranslucentBackground)

		self._app_container = QFrame()
		self._app_container.setStyleSheet(stylesheet.app_bg)
		self._app_container.setLayout(QVBoxLayout())
		self._app_container.layout().setSpacing(0)
		self._app_container.layout().setContentsMargins(QMargins(0, 0, 0, 0))
		app.setCentralWidget(self._app_container)

		self._title_bar = components.TitleBar(app)

		self._content_container = QFrame()
		self._content_container.setLayout(QHBoxLayout())
		self._content_container.layout().setSpacing(0)
		self._content_container.layout().setContentsMargins(QMargins(0, 0, 0, 0))

		self._app_container.layout().addWidget(self._title_bar)
		self._app_container.layout().addWidget(self._content_container)

		self._pages_container = QStackedWidget()
		self._log_frame = components.LogFrame()
		self._content_container.layout().addWidget(self._pages_container)
		self._content_container.layout().addWidget(self._log_frame)

		self._bot_page = components.BotPage(app, self._log_frame)
		self._pages_container.addWidget(self._bot_page)
		self._pages_container.setCurrentWidget(self._bot_page)
