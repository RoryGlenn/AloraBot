import sys
import time
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import QThread
# from __feature__ import snake_case, true_property

class FireAndForget(QThread):
    def __init__(self, max, sleep, label):
        super().__init__()
        self.label = label
        self.max = max
        self.sleep = sleep

def run(self):
    for x in range(self.max):
        self.label.text = f"Count {x}"
        time.sleep(self.sleep)  # or use self.msleep(ms) as alternative

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        centralwidget = QWidget()
        self.set_central_widget(centralwidget)
        verticalbox = QVBoxLayout(centralwidget)
        label1 = QLabel()
        label2 = QLabel()
        verticalbox.add_widget(label1)
        verticalbox.add_widget(label2)
        self.set_layout(verticalbox)

        self.t = FireAndForget(7, 1, label1)
        self.t2 = FireAndForget(50, .15, label2)
        self.t.start()
        self.t2.start()

app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
app.exec_()