from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from constants.constantspath import ConstantsPath
from interface.style import Style
from os.path import join


class GameInterface(Style):
    def __init__(self):
        super(GameInterface, self).__init__()
        self.setFixedSize(850, 700)


        self.dict_norm_coord_label = {}
        self.labels()
        self.draw_score_text()
        self.draw_board()
        self.draw_gamers()



    def draw_gamers(self):
        self.label_gamer_b = QLabel("black", self)
        self.label_gamer_b.setStyleSheet(self.stylesheet_gamers)
        self.label_gamer_b.move(50, 200)

        self.label_gamer_w = QLabel("white", self)
        self.label_gamer_w.setStyleSheet(self.stylesheet_gamers)
        self.label_gamer_w.move(700, 200)

    def labels(self):
        """Отрисовка названия"""

        self.name_game = QLabel("Game of Go", self)
        self.name_game.setStyleSheet(self.stylesheet)
        self.name_game.move(285, 40)
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

        self.score_label_w = QLabel("Score white: 0", self)
        self.score_label_w.setStyleSheet(self.stylesheet_score)
        self.score_label_w.move(645, 140)
        self.score_label_b = QLabel("Score black: 0", self)
        self.score_label_b.setStyleSheet(self.stylesheet_score)
        self.score_label_b.move(50, 140)

    def set_chip_b(self, point, norm_coord):
        """Отрисовка черных фишек"""

        chip = QLabel(self)
        pixmap = QPixmap(join(ConstantsPath.dir_graphics, "chip_b.png"))
        chip.setPixmap(pixmap)
        chip.move(point[0] - 24 / 2, point[1] - 18 / 2)
        chip.show()
        self.dict_norm_coord_label.update({norm_coord: chip})


    def set_chip_w(self, point, norm_coord):
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

    def set_who_run(self, num):
        if num % 2 == 0:
            self.label_gamer_b.setStyleSheet(self.stylesheet_gamers_run)
            self.label_gamer_w.setStyleSheet(self.stylesheet_gamers)
        else:
            self.label_gamer_w.setStyleSheet(self.stylesheet_gamers_run)
            self.label_gamer_b.setStyleSheet(self.stylesheet_gamers)
