from PyQt5.QtWidgets import *

from interface.response_interface import ResponseInterface
from interface.style import Style
from validate.validate_input_time import ValidateInputTime


class TimeGame(Style):
    def __init__(self, random_bot=False, smart_bot=False):
        super(TimeGame, self).__init__()
        self.setFixedSize(850, 700)
        self.random_bot = random_bot
        self.smart_bot = smart_bot
        self.buttons()
        self.labels()

    def labels(self):
        self.name_game = QLabel('Set time for the game', self)
        self.name_game.setStyleSheet(self.stylesheet)
        self.name_game.move(220, 150)
        self.name_game.resize(500, 60)

        self.hour_label = QLabel('Hour:', self)
        self.hour_label.setStyleSheet(self.stylesheet_time_label)
        self.hour_label.move(260, 335)

        self.hour_line = QLineEdit("0", self)
        self.hour_line.move(350, 335)
        self.hour_line.setStyleSheet(self.stylesheet_line)
        self.hour_line.resize(50, 32)
        self.hour_line.setMaxLength(4)

        self.min_label = QLabel('Min:', self)

        self.min_label.setStyleSheet(self.stylesheet_time_label)
        self.min_label.move(460, 335)

        self.min_line = QLineEdit("0", self)
        self.min_line.setMaxLength(4)
        self.min_line.setStyleSheet(self.stylesheet_line)

        self.min_line.move(530, 335)
        self.min_line.resize(50, 32)

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
        self.window = TimeInterface(self.random_bot, self.smart_bot)
        self.close()
        self.window.show()

    def start_game(self):
        time_hour = self.hour_line.text()
        time_min = self.min_line.text()
        if ValidateInputTime.validate_time(time_hour, time_min):
            all_time = int(time_hour) * 3600 + int(time_min) * 60
            self.start_interface(all_time)

    def start_interface(self, all_time):

        self.window = ResponseInterface(False, True, all_time, self.random_bot, self.smart_bot)
        self.close()
        self.window.show()
