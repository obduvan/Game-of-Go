from PyQt5.QtWidgets import *

from interface.style import Style
from validate.validate_input_time import ValidateInputTime


class TimeMove(Style):
    def __init__(self, type_game):
        super(TimeMove, self).__init__()
        self.setFixedSize(850, 700)
        self.type_game = type_game
        self.buttons()
        self.labels()

    def labels(self):
        self.name_game = QLabel('Set time for the move', self)
        self.name_game.setStyleSheet(self.stylesheet)
        self.name_game.move(220, 150)
        self.name_game.resize(500, 60)

        self.min_label = QLabel('Min:', self)
        self.min_label.setStyleSheet(self.stylesheet_time_label)
        self.min_label.move(270, 335)

        self.min_line = QLineEdit("0", self)
        self.min_line.move(340, 335)
        self.min_line.setMaxLength(4)
        self.min_line.setStyleSheet(self.stylesheet_line)
        self.min_line.resize(50, 32)

        self.sec_label = QLabel('Sec:', self)

        self.sec_label.setStyleSheet(self.stylesheet_time_label)
        self.sec_label.move(452, 335)

        self.sec_line = QLineEdit("0", self)
        self.sec_line.move(530, 335)
        self.sec_line.setMaxLength(4)
        self.sec_line.setStyleSheet(self.stylesheet_line)
        self.sec_line.resize(50, 32)

    def buttons(self):
        self.button_0 = QPushButton('Ok', self)
        self.button_0.setStyleSheet(self.stylesheet_button)
        self.button_0.clicked.connect(self.start_game)
        self.button_0.move(180, 435)
        self.button_0.setFixedSize(500, 50)

        self.button_1 = QPushButton('Back', self)
        self.button_1.setStyleSheet(self.stylesheet_button_back)
        self.button_1.clicked.connect(self.go_back)
        self.button_1.move(180, 505)
        self.button_1.setFixedSize(500, 50)

    def go_back(self):
        from interface.time_interface import TimeInterface
        self.start_interface(TimeInterface(self.type_game))

    def start_game(self):
        time_min = self.min_line.text()
        time_sec = self.sec_line.text()
        if ValidateInputTime.validate_time(time_sec, time_min):
            all_time = int(time_sec) + int(time_min) * 60
            self.start_interface(self.type_game(True, False, all_time))

    def start_interface(self, interface):
        self.window = interface
        self.close()
        self.window.show()
