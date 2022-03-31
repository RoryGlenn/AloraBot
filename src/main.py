import sys
import ui

from PySide6.QtWidgets import QApplication, QMainWindow


class App(QMainWindow):
    """Gui Interface"""
    def __init__(self):
        super(App, self).__init__()

        self._ui = ui.UiApp()
        self._ui.init_gui(self)

        self.show()
        
        # send to title bar qwindow obj after .show()
        self._ui._title_bar.set_window_handle(self.windowHandle())

    def mousePressEvent(self, event) -> None:
        """Handle the mouse press event in the application"""
        
        # save drag pos to the custom title bar
        self.drag_pos = event.globalPosition().toPoint()

        # remove cursor when search lose focus
        focus_widget = QApplication.focusWidget()

        if hasattr(focus_widget, 'objectName'):
            focus_widget.clearFocus()


def main() -> None:
    """Entry point for application"""
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
