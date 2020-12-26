import sys

from constants.constants_name import ConstantsName
from engine.count_points import CountPoints
from engine.signals import Signals

from coordinates_generator.matrix_coordinates import MatrixCoordinates
from interface.end_game_interface import EndGameInterFace
from engine.game import Game
from interface.game_interface import GameInterface, QApplication
from player_color import PlayerColor


class ResponseInterface(GameInterface):
    def __init__(self):
        super(ResponseInterface, self).__init__()
        self.col_pass_black = False
        self.col_pass_white = False
        self.move_number = 0
        self.black_points = 0
        self.white_points = 0
        self.normalize_coord_stones_dict = {}
        self.game = Game()

        self.signal = Signals()
        self.count_points = CountPoints()

        self.draw_who_run(self.move_number)
        self.matrix_coordinates = MatrixCoordinates()
        self.set_signals()

    def set_signals(self):
        self.signal.restart_signal.connect(self.restart_game)
        self.signal.closed_signal.connect(self.close_game)

    def get_player_color(self):
        if self.move_number % 2 == 0:
            return PlayerColor.BLACK
        else:
            return PlayerColor.WHITE

    def mousePressEvent(self, event):
        if self.game.validate.validate_gamer_zone(event.x(), event.y()):
            x_trans, y_trans = self.matrix_coordinates.transformed_coord_mouse(event.x(), event.y())
            x_norm, y_norm = self.matrix_coordinates.get_normalize_coord((x_trans, y_trans))
            transformed_coord = (x_trans, y_trans)
            normalized_coord = (x_norm, y_norm)
            color = self.get_player_color()
            if self.is_valid_gambit(transformed_coord, normalized_coord, color):
                self.set_new_stone(transformed_coord, normalized_coord)

    def set_new_gambit(self):
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

    def set_new_stone(self, transformed_coord, normalized_coord):
        self.draw_points()
        self.set_new_gambit()
        self.draw_new_stone(transformed_coord, normalized_coord)
        self.move_number += 1
        self.draw_who_run(self.move_number)

        self.set_not_pass_gambit()
        self.game.print_log_game()
        print("-" * 30)
        print("ХОД ВАЛИДНЫЙ")

    def set_not_pass_gambit(self):
        if self.get_player_color() == PlayerColor.BLACK:
            self.col_pass_black = False
        else:
            self.col_pass_white = False

    def is_valid_gambit(self, transformed_coord, normalized_coord, color):
        if self.game.validate_set_stones(normalized_coord[0], normalized_coord[1]):
            print(normalized_coord, " <-- ход")
            if self.move_is_valid(transformed_coord, normalized_coord, color):
                return True
            print("ХОД НЕ ВАЛИДНЫЙ")
            return False
        return False

    def draw_points(self):
        black_groups, white_groups = self.game.get_black_white_groups()
        self.black_points = self.count_points.count_points_black(black_groups)
        self.white_points = self.count_points.count_points_white(white_groups)
        self.redraw_points_black(self.black_points)
        self.redraw_points_white(self.white_points)

    def move_is_valid(self, transformed_coord, normalized_coord, color):
        return self.game.move_is_valid(transformed_coord, normalized_coord, color)

    def draw_new_stone(self, transformed_coord, normalized_coord):
        if self.get_player_color() == PlayerColor.BLACK:
            self.draw_stone_b(transformed_coord, normalized_coord)
            self.enabled_buttons(False, True)
        else:
            self.draw_stone_w(transformed_coord, normalized_coord)
            self.enabled_buttons(True, False)

    def hide_stones(self, remove_group):
        for group in remove_group:
            for norm_coord in group:
                self.del_chip(norm_coord)

    def get_pass_black(self):
        self.move_number += 1
        self.draw_who_run(self.move_number)

        self.col_pass_black = True
        self.pass_black.setEnabled(False)
        self.pass_white.setEnabled(True)

        if self.col_pass_white == True:
            print("конец")
            self.draw_menu()

    def get_pass_white(self):
        self.move_number += 1
        self.draw_who_run(self.move_number)

        self.col_pass_white = True
        self.pass_white.setEnabled(False)
        self.pass_black.setEnabled(True)

        if self.col_pass_black == True:
            print("конец")
            self.draw_menu()

    def draw_menu(self):
        self.close()
        new_win = EndGameInterFace(self, self.signal, self.black_points, self.white_points)
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