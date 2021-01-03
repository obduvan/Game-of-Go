

from PyQt5.QtWidgets import *

from constants.constants_name import ConstantsName
from interface.style import Style
from interface.time_game import TimeGame
from interface.time_move import TimeMove


class TimeInterface(Style):
    def __init__(self, type_game):
        super(TimeInterface, self).__init__()
        self.setFixedSize(850, 700)
        self.type_game = type_game
        self.buttons()
        self.labels()

    def labels(self):
        """Отрисовка названия"""

        self.name_game = QLabel("Time control", self)
        self.name_game.setStyleSheet(self.stylesheet)
        self.name_game.move(305, 150)
        self.name_game.resize(500, 60)

    def buttons(self):
        self.button_0 = QPushButton('Game without time', self)
        self.button_0.setStyleSheet(self.stylesheet_button)
        self.button_0.clicked.connect(self.set_without_time)
        self.button_0.move(180, 285)
        self.button_0.setFixedSize(500, 50)

        self.button_1 = QPushButton('Set time for the move', self)
        self.button_1.setStyleSheet(self.stylesheet_button)
        self.button_1.clicked.connect(self.set_time_move)
        self.button_1.move(180, 355)
        self.button_1.setFixedSize(500, 50)

        self.button_2 = QPushButton('Set time for the game', self)
        self.button_2.setStyleSheet(self.stylesheet_button)
        self.button_2.clicked.connect(self.set_time_game)

        self.button_2.move(180, 425)
        self.button_2.setFixedSize(500, 50)

        self.button_3 = QPushButton('Back', self)
        self.button_3.setStyleSheet(self.stylesheet_button_back)
        self.button_3.clicked.connect(self.go_back)
        self.button_3.move(180, 515)
        self.button_3.setFixedSize(500, 50)

    def go_back(self):
        self.close()
        from platform import system
        import os
        system = system()
        if system == "Windows":
            start = "python {}".format(ConstantsName.point_program)
        else:
            start = "python3 {}".format(ConstantsName.point_program)
        os.system(start)

    def set_without_time(self):
        self.start_game(self.type_game())

    def set_time_move(self):
        self.start_game(TimeMove(self.type_game))

    def set_time_game(self):
        self.start_game(TimeGame(self.type_game))

    def start_game(self, interface):
        self.window = interface
        self.close()
        self.window.show()


