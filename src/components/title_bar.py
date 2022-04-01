
from PySide6.QtWidgets import QFrame, QHBoxLayout, QToolButton
from PySide6.QtCore import Qt, QSize, QMargins, Slot
from PySide6.QtGui import QWindow
import utils
from style import stylesheet


class TitleBar(QFrame):

    def __init__(self, parent):
        super(TitleBar, self).__init__()
        self.setFixedHeight(30)
        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.layout().setSpacing(2)
        self.layout().setContentsMargins(QMargins(0, 0, 0, 0))
        self.setStyleSheet(stylesheet.title_bar)

        self.main_app = parent
        self.window_handle = None
        self.support_system_move = False

        self._container = QFrame()
        self._container.setStyleSheet(stylesheet.title_bar_detail)
        self._container.setFixedWidth(400)
        self._container.setLayout(QHBoxLayout())
        self._container.layout().setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._container.layout().setSpacing(2)
        self._container.layout().setContentsMargins(QMargins(0, 10, 10, 0))
        self.layout().addWidget(self._container)

        self._minimize_btn = CustomButtom(icon=utils.load_svg(
            'src/resources/images/minimize.svg', size=QSize(10, 1)), type_='minimize')
        self._minimize_btn.clicked.connect(self._minimize)
        self._exit_btn = CustomButtom(icon=utils.load_svg(
            'src/resources/images/exit.svg', size=QSize(10, 10)))
        self._exit_btn.clicked.connect(self._exit)

        for btn in [self._minimize_btn, self._exit_btn]:
            self._container.layout().addWidget(btn)

    def set_window_handle(self, window: QWindow) -> None:
        """Set the window obj for the startsystemmove
        """
        self.window_handle = window

    def mouseMoveEvent(self, event) -> None:
        """Handle the window move event if not 
        support the startsystemmove
        """
        if not self.support_system_move:
            app = utils.find_parent(obj=self, target='main_app')
            if app != None:
                if not app.isMaximized():
                    if event.buttons() == Qt.LeftButton:
                        app.move(app.pos() + event.globalPos() - app.drag_pos)
                        app.drag_pos = event.globalPos()
                        event.accept()
        return super().mousePressEvent(event)

    def mousePressEvent(self, event) -> None:
        """Move window function using mouse press event
        """
        if self.window_handle != None:
            self.support_system_move = True if self.window_handle.startSystemMove() else False
        return super().mousePressEvent(event)

    @Slot()
    def _minimize(self):
        self.main_app.showMinimized()

    @Slot()
    def _exit(self):
        self.main_app.close()


class CustomButtom(QToolButton):

    def __init__(self, icon, type_=None):
        super(CustomButtom, self).__init__()

        icon_size = QSize(14, 14) if type_ == None else QSize(14, 2)
        self.setFixedSize(QSize(20, 20))
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.setCursor(Qt.PointingHandCursor)
        self.setIcon(icon)
        self.setIconSize(icon_size)
