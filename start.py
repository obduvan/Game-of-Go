import sys

from PyQt5.QtWidgets import *

from interface.response_interface import ResponseInterface
from interface.style import Style
from interface.time_interface import TimeInterface
from players.random_bot import RandomBot
from players.smart_bot import SmartBot


class StartInterface(Style):
    def __init__(self):
        super(StartInterface, self).__init__()
        self.setFixedSize(850, 700)
        self.buttons()
        self.labels()

    def labels(self):
        """Отрисовка названия"""

        self.name_game = QLabel("Game of Go", self)
        self.name_game.setStyleSheet(self.stylesheet)
        self.name_game.move(305, 150)
        self.name_game.resize(500, 60)

    def buttons(self):
        self.button_0 = QPushButton('Play on the same computer', self)
        self.button_0.setStyleSheet(self.stylesheet_button)
        self.button_0.clicked.connect(self.start_with_man)
        self.button_0.move(180, 285)
        self.button_0.setFixedSize(500, 50)

        self.button_1 = QPushButton('Play with a stupid bot', self)
        self.button_1.setStyleSheet(self.stylesheet_button)
        self.button_1.clicked.connect(self.start_easy_bot)
        self.button_1.move(180, 355)
        self.button_1.setFixedSize(500, 50)

        self.button_2 = QPushButton('Play with a smarter bot ', self)
        self.button_2.setStyleSheet(self.stylesheet_button)
        self.button_2.clicked.connect(self.start_clever_bot)

        self.button_2.move(180, 425)
        self.button_2.setFixedSize(500, 50)

    def start_with_man(self):
        self.window = TimeInterface(ResponseInterface)
        self.start_game()

    def start_easy_bot(self):
        self.window = TimeInterface(RandomBot)
        self.start_game()

    def start_clever_bot(self):
        self.window = TimeInterface(SmartBot)
        self.start_game()


    def start_game(self):
        self.close()
        self.window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartInterface()
    window.show()
    app.exec_()

