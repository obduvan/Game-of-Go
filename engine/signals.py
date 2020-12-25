from PyQt5.QtCore import QObject, pyqtSignal


class Signals(QObject):
    def __init__(self):
        super(Signals, self).__init__()

    restart_signal = pyqtSignal()
    closed_signal = pyqtSignal()
