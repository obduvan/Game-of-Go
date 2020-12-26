from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from constants.constants_path import ConstantsPath
from interface.style import Style
from os.path import join


class GameInterface(Style):
    def __init__(self):
        super(GameInterface, self).__init__()
        self.setFixedSize(850, 700)


        self.dict_norm_coord_label = {}
        self.labels()
        self.draw_color_players()
        self.draw_board()
        self.draw_pass_command()
        self.draw_points_black()
        self.draw_points_white()


    def labels(self):
        """Отрисовка названия"""

        self.name_game = QLabel("Game of Go", self)
        self.name_game.setStyleSheet(self.stylesheet)
        self.name_game.move(305, 90)
        self.name_game.resize(500, 60)

    def draw_board(self):
        """Отрисовка игровой доски"""

        self.label_board = QLabel(self)
        pixmap = QPixmap(join(ConstantsPath.dir_graphics, "board.png"))
        self.label_board.setPixmap(pixmap)
        self.label_board.move(220, 220)
        self.label_board.show()

    def draw_color_players(self):
        """Отрисовка количества очков игроков"""

        self.score_label_w = QLabel("White", self)
        self.score_label_w.setStyleSheet(self.stylesheet_score)
        self.score_label_w.move(700, 240)
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

    def draw_forbidden_move(self):
        """Отрисовка не валидного хода"""

        self.forbidden_move_label = QLabel("forbidden move", self)
        self.forbidden_move_label.setStyleSheet(self.stylesheet_forb_move)
        self.forbidden_move_label.move(340, 640)
        self.forbidden_move_label.show()

    def draw_points_black(self):
        self.label_points_black = QLabel("0", self)
        self.label_points_black.setStyleSheet(self.stylesheet_score)
        self.label_points_black.move(90, 290)
        self.label_points_black.setFixedSize(70, 50)
        self.label_points_black.show()

    def draw_points_white(self):
        self.label_points_white = QLabel("0", self)
        self.label_points_white.setStyleSheet(self.stylesheet_score)
        self.label_points_white.move(720, 290)
        self.label_points_white.setFixedSize(70, 50)
        self.label_points_white.show()

    def redraw_points_black(self, points):
        self.label_points_black.setText(str(points))

    def redraw_points_white(self, points):
        self.label_points_white.setText(str(points))

    def close_for_move(self):
        self.forbidden_move_label.hide()

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

    def enabled_buttons(self, black: bool, white: bool):
        self.pass_black.setEnabled(black)
        self.pass_white.setEnabled(white)

