from PyQt5.QtWidgets import *
import sys

from MatrixCoordinates import MatrixCoordinates
from game import Game
from interface.game_interface import GameInterface
from player_color import PlayerColor


class ResponseInterface(GameInterface):
    def __init__(self):
        super(ResponseInterface, self).__init__()
        self.move_number = 0
        self.move_color = PlayerColor.BLACK
        self.game = Game()

        self.set_who_run(self.move_number)
        self.matrix_coordinates = MatrixCoordinates()

    def mouseMoveEvent(self, event):
        pass

    def is_white(self, move_number):
        return move_number % 2 == 0

    def get_player_color(self):
        if self.move_number % 2 == 0:
            return PlayerColor.BLACK
        else:
            return PlayerColor.WHITE

    def mousePressEvent(self, event):
        color = self.get_player_color()
        if self.game.validate_set_stones(event.x(), event.y(), color):
            x_mouse, y_mouse = event.x(), event.y()
            transformed_coord = self.matrix_coordinates.transformed_coord_mouse(x_mouse, y_mouse)
            norm_coord = self.matrix_coordinates.get_normalize_coord(transformed_coord)

            if self.stone_work(transformed_coord, norm_coord):
                self.move_number += 1
                self.draw_who_run()
                print("ХОД ВАЛИДНЫЙ")
            else:
                print("ХОД НЕ ВАЛИДНЫЙ")
            print("-" * 30)

    def stone_work(self, transformed_coord, norm_coord):
        self.set_new_stone(transformed_coord)
        self.game.check_free_dame()
        self.game.update_groups(self.move_color)
        removed_group, VALID_MOVE = self.game.remove_dead_stones(self.move_color)

        if VALID_MOVE:
            self.draw_chip(transformed_coord, norm_coord)
            self.hide_stones(removed_group)
            return True
        else:
            return False

    def set_new_stone(self, transformed_coord):
        normalize_coord = self.matrix_coordinates.get_normalize_coord(transformed_coord)
        print(normalize_coord, "координаты точки")
        self.game.set_new_stone(self.move_color, normalize_coord)

    def draw_chip(self, transformed_coord, norm_coord):
        if self.is_white(self.move_number):
            self.set_chip_b(transformed_coord, norm_coord)
            self.move_color = PlayerColor.WHITE
        else:
            self.set_chip_w(transformed_coord, norm_coord)
            self.move_color = PlayerColor.BLACK

    def draw_who_run(self):
        print(self.move_number)
        self.set_who_run(self.move_number)

    def hide_stones(self, remove_group):
        for group in remove_group:
            for norm_coord in group:
                self.del_chip(norm_coord)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ResponseInterface()
    window.show()
    app.exec_()
