from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from constants.constants_path import ConstantsPath
from interface.style import Style
from os.path import join


class GameInterface(Style):
    def __init__(self):
        super(GameInterface, self).__init__()
        self.setFixedSize(850, 700)
        self.col_pass_black = 0
        self.col_pass_white = 0

        self.dict_norm_coord_label = {}
        self.labels()
        self.draw_score_text()
        self.draw_board()
        self.draw_pass_command()

    def labels(self):
        """Отрисовка названия"""

        self.name_game = QLabel("Game of Go", self)
        self.name_game.setStyleSheet(self.stylesheet)
        self.name_game.move(285, 90)
        self.name_game.resize(500, 60)

    def draw_board(self):
        """Отрисовка игровой доски"""

        self.label_board = QLabel(self)
        pixmap = QPixmap(join(ConstantsPath.dir_graphics, "board.png"))
        self.label_board.setPixmap(pixmap)
        self.label_board.move(220, 220)
        self.label_board.show()

    def draw_score_text(self):
        """Отрисовка количества очков игроков"""

        self.score_label_w = QLabel("White", self)
        self.score_label_w.setStyleSheet(self.stylesheet_score)
        self.score_label_w.move(710, 240)
        self.score_label_b = QLabel("Black", self)
        self.score_label_b.setStyleSheet(self.stylesheet_score)
        self.score_label_b.move(70, 240)

    def draw_stone_b(self, point, norm_coord):
        """Отрисовка черных фишек"""

        chip = QLabel(self)
        pixmap = QPixmap(join(ConstantsPath.dir_graphics, "chip_b.png"))
        chip.setPixmap(pixmap)
        chip.move(point[0] - 24 / 2, point[1] - 18 / 2)
        chip.show()
        self.dict_norm_coord_label.update({norm_coord: chip})

    def draw_pass_command(self):
        """Отрисовка команды pass"""

        self.pass_black = QPushButton("Pass", self)
        self.pass_black.setStyleSheet(self.stylesheet_button)
        self.pass_black.clicked.connect(self.get_pass_black)
        self.pass_black.setFixedSize(90, 40)
        self.pass_black.move(50, 550)
        self.pass_black.show()

        self.pass_white = QPushButton("Pass", self)
        self.pass_white.setStyleSheet(self.stylesheet_button)
        self.pass_white.clicked.connect(self.get_pass_white)
        self.pass_white.setFixedSize(90, 40)
        self.pass_white.move(690, 550)
        self.pass_white.show()
        self.pass_white.setEnabled(False)

    def draw_stone_w(self, point, norm_coord):
        """Отрисовка белых фишек"""

        chip = QLabel(self)
        pixmap = QPixmap(join(ConstantsPath.dir_graphics, "chip_w.png"))
        chip.setPixmap(pixmap)
        chip.move(point[0] - 24 / 2, point[1] - 18 / 2)
        chip.show()
        self.dict_norm_coord_label.update({norm_coord: chip})

    def del_chip(self, norm_coord):
        self.dict_norm_coord_label[norm_coord].hide()

    def redrawing_score(self, label, score):
        """Отрисовка изменения счета"""

        label.setText("{} {}".format(label, score))

    def draw_who_run(self, num):
        if num % 2 == 0:
            self.score_label_b.setStyleSheet(self.stylesheet_gamers_run)
            self.score_label_w.setStyleSheet(self.stylesheet_gamers)
        else:
            self.score_label_w.setStyleSheet(self.stylesheet_gamers_run)
            self.score_label_b.setStyleSheet(self.stylesheet_gamers)
