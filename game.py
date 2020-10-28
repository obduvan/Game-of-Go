from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from game_interface import GameInterface
from os.path import join
from settings import Settings


class Game(GameInterface):
    def __init__(self):
        super(Game, self).__init__()
        self.WHO = "black"
        self.num = 0
        self.set_who_run(self.num)

    def validate_gamer_zone(self, x, y):
        h_l = (275, 275)
        d_r = (564, 562)

        if h_l[0] - 5 < x and x < d_r[0] + 5:
            if h_l[1] - 5 < y and y < d_r[1] + 5:
                return True
        return False

    def set_coor_chip(self, x, y):
        res_point = 0, 0
        lengt = 100

        for point in self.matrx_board:
            x_len = abs(point[0] - x)
            y_len = abs(point[1] - y)
            res = y_len + x_len
            if (res) < lengt:
                lengt = res
                res_point = point
        if lengt < 15:
            return res_point
        return (0, 0)

    def mouseMoveEvent(self, event):
        pass

    def mousePressEvent(self, event):
        if self.validate_gamer_zone(event.x(), event.y()):
            res_point = self.set_coor_chip(event.x(), event.y())
            if res_point != (0, 0):

                if self.num % 2 == 0:
                    self.set_chip_b(res_point)
                else:
                    self.set_chip_w(res_point)
                self.num += 1
                self.set_who_run(self.num)

                print(event.x(), event.y())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Game()
    window.show()
    app.exec_()
