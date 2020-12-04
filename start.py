from constants.constants_name import ConstantsName
from engine.signals import Signals

from PyQt5.QtWidgets import *
import sys
from matrix_coordinates import MatrixCoordinates
from interface.end_game_interface import EndGameInterFace
from engine.game import Game
from interface.game_interface import GameInterface
from player_color import PlayerColor


class ResponseInterface(GameInterface):
    def __init__(self):
        super(ResponseInterface, self).__init__()
        self.move_number = 0
        self.move_color = PlayerColor.BLACK
        self.game = Game()
        self.signal = Signals()

        self.draw_who_run(self.move_number)
        self.matrix_coordinates = MatrixCoordinates()
        self.set_signals()

    def set_signals(self):
        self.signal.restart_signal.connect(self.restart_game)
        self.signal.closed_signal.connect(self.close_game)

    def mouseMoveEvent(self, event):
        pass

    def get_player_color(self):
        if self.move_number % 2 == 0:
            return PlayerColor.BLACK
        else:
            return PlayerColor.WHITE

    def mousePressEvent(self, event):
        color = self.get_player_color()
        if self.game.validate_set_stones(event.x(), event.y()):
            x_mouse, y_mouse = event.x(), event.y()
            transformed_coord = self.matrix_coordinates.transformed_coord_mouse(
                x_mouse, y_mouse
            )
            normalized_coord = self.matrix_coordinates.get_normalize_coord(
                transformed_coord
            )
            print(normalized_coord, " <-- ход")
            if self.move_is_valid(transformed_coord, normalized_coord, color):
                self.what_to_do()

                self.draw_new_stone(transformed_coord, normalized_coord)
                self.move_number += 1
                self.set_who_run()
                print("ХОД ВАЛИДНЫЙ")
            else:
                print("ХОД НЕ ВАЛИДНЫЙ")
            self.game.print_dict()
            print("-" * 30)

    def move_is_valid(self, transformed_coord, normalized_coord, color):
        return self.game.move_is_valid(transformed_coord, normalized_coord, color)

    def what_to_do(self):
        self.game.set_new_move()
        removed_black, removed_white = self.game.get_removed_groups()
        if self.get_player_color() == PlayerColor.BLACK:
            if len(removed_white) != 0:
                self.game.delete_stones_in_dict(removed_white)
                self.hide_stones(removed_white)
        else:
            if len(removed_black) != 0:
                self.game.delete_stones_in_dict(removed_black)
                self.hide_stones(removed_black)

    def draw_new_stone(self, transformed_coord, normalized_coord):
        if self.get_player_color() == PlayerColor.BLACK:
            self.draw_stone_b(transformed_coord, normalized_coord)
            self.move_color = PlayerColor.WHITE
            self.col_pass_black = 0
            self.pass_white.setEnabled(True)
            self.pass_black.setEnabled(False)
        else:
            self.draw_stone_w(transformed_coord, normalized_coord)
            self.move_color = PlayerColor.BLACK
            self.col_pass_white = 0
            self.pass_white.setEnabled(False)
            self.pass_black.setEnabled(True)

    def set_who_run(self):
        self.draw_who_run(self.move_number)

    def hide_stones(self, remove_group):
        for group in remove_group:
            for norm_coord in group:
                self.del_chip(norm_coord)

    def get_pass_black(self):
        self.move_number += 1
        self.set_who_run()
        self.col_pass_black = 1

        self.pass_black.setEnabled(False)
        self.pass_white.setEnabled(True)
        if self.col_pass_white == 1:
            print("конец")
            self.draw_menu()

    def get_pass_white(self):
        self.move_number += 1
        self.set_who_run()

        self.col_pass_white = 1
        self.pass_white.setEnabled(False)
        self.pass_black.setEnabled(True)
        if self.col_pass_black == 1:
            print("конец")
            self.draw_menu()

    def draw_menu(self):
        self.close()
        new_win = EndGameInterFace(self, self.signal)
        new_win.show()

    def close_game(self):
        self.close()

    def closeEvent(self, event):
        self.close_game()

    def restart_game(self):
        self.close_game()
        from platform import system
        import os

        system = system()
        if system == "Windows":
            start = "python {}".format(ConstantsName.point_program)
        else:
            start = "python3 {}".format(ConstantsName.point_program)
        os.system(start)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ResponseInterface()
    window.show()
    app.exec_()
