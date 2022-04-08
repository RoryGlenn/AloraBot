"""
A complete working example is given below,
showcasing the custom QRunnable worker together with the worker & progress signals.
You should be able to easily adapt this code to any multithreaded application you develop.

"""


from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool

import sys
import time
import traceback
import pyautogui


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        """Initialise the runner function with passed args, kwargs"""

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            # Return the result of the processing
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()  # Done


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(1)
        print("Multithreading with maximum %d threads" %
              self.threadpool.maxThreadCount())

        self.timer = QTimer()
        # sets how often the gui will be updated with the new values
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def progress_fn(self, n):
        print("%d%% done" % n)

    def execute_this_fn(self, progress_callback):
        # for n in range(0, 5):
        #     time.sleep(1)
        #     progress_callback.emit(n*100/4)

        print("Enabled feedback")
        
        for i in range(0, 20):
            # Get and print the mouse coordinates.
            x, y = pyautogui.position()
            pos_x = "X: " + str(x).rjust(4)
            pos_y = "Y:" + str(y).rjust(4)
            position_str = pos_x + ', ' + pos_y

            if not pyautogui.onScreen(x, y):
                # Pixel color can only be found for the primary monitor, and also not on mac due to the screenshot having the mouse cursor in the way.
                pixelColor = ("NaN", "NaN", "NaN")
            else:
                # NOTE: On Windows & Linux, getpixel() returns a 3-integer tuple, but on macOS it returns a 4-integer tuple.
                pixelColor = pyautogui.pyscreeze.screenshot().getpixel((x, y))

            r = str(pixelColor[0]).rjust(3)
            g = str(pixelColor[1]).rjust(3)
            b = str(pixelColor[2]).rjust(3)

            self.position_str = position_str + " RBG: (" + \
                                r + ', ' + \
                                g + ', ' + \
                                b + ')'

            print(self.position_str)
            time.sleep(0.1)
            progress_callback.emit(i/20)
        return "Done."

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def oh_no(self):
        # Pass the function to execute
        # Any other args, kwargs are passed to the run function
        worker = Worker(self.execute_this_fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
