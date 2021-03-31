import sys

from PyQt5.QtCore import QTimer

from constants.constants_name import ConstantsName
from engine.count_points import CountPoints
from engine.signals import Signals

from coordinates_generator.matrix_coordinates import MatrixCoordinates
from interface.end_game_interface import EndGameInterFace
from engine.game import Game
from interface.base_game_interface import BaseGameInterface, QApplication
from player_color import PlayerColor
from players.random_bot import RandomBot
from players.smart_bot import SmartBot


class ResponseInterface(BaseGameInterface):
    def __init__(self, is_move_time=False, is_game_time=False, all_time=None, random_bot=False, smart_bot=False):
        super(ResponseInterface, self).__init__()
        self.col_pass_black = False
        self.col_pass_white = False
        self.is_random_bot = random_bot
        self.is_smart_bot = smart_bot
        self.is_move_time = is_move_time
        self.is_game_time = is_game_time
        self.all_time = all_time
        self.copy_time = all_time
        self.black_points = 0
        self.white_points = 0
        self.start_timing()
        self.normalize_coord_stones_dict = {}
        self.game = Game()

        self.signal = Signals()
        self.count_points = CountPoints()

        self.draw_who_run(self.game.get_move_number_engine())

        self.matrix_coordinates = MatrixCoordinates()
        self.set_signals()
        self.check_bot()

    def check_bot(self):
        if self.is_random_bot or self.is_smart_bot:
            self.set_bots()

    def set_bots(self):
        if self.is_random_bot:
            self.bot = RandomBot(self.game)
        elif self.is_smart_bot:
            self.bot = SmartBot(self.game)

        self.timer_bot = QTimer(self)
        self.timer_bot.setInterval(600)
        self.timer_bot.timeout.connect(self.action_bot)
        self.timer_bot.start()

    def action_bot(self):
        if self.game.get_player_color() == PlayerColor.WHITE:
            response = self.bot.action()
            # print(response)
            type_move = response["type"]
            cord_trans = response["trans_cord"]
            cord_norm = response["norm_cord"]
            if type_move == "pass":
                self.get_pass_white()
            elif type_move == "move":
                self.set_new_stone(cord_trans, cord_norm)

    def start_timing(self):
        if self.is_move_time or self.is_game_time:
            self.start_timer()

    def start_timer(self):
        self.all_time = self.copy_time
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_counter)
        self.timer.start()

    def validate_time(self):
        if self.all_time == -1:
            if self.is_move_time:
                self.time_transition()
            else:
                self.timer.stop()
                self.draw_menu()

    def update_counter(self):
        hours = int(self.all_time / 3600)
        mins = int((self.all_time - hours * 3600) / 60)
        secs = int(self.all_time % 60)
        self.draw_time("%d:%02d:%02d" % (hours, mins, secs))
        self.all_time -= 1
        self.validate_time()

    def set_signals(self):
        self.signal.restart_signal.connect(self.restart_game)
        self.signal.closed_signal.connect(self.close_game)

    def mousePressEvent(self, event):
        if self.game.validate.validate_gamer_zone(event.x(), event.y()):
            x_trans, y_trans = self.matrix_coordinates.transformed_coord_mouse(event.x(), event.y())
            x_norm, y_norm = self.matrix_coordinates.get_normalize_coord((x_trans, y_trans))
            transformed_coord = (x_trans, y_trans)
            normalized_coord = (x_norm, y_norm)
            color = self.game.get_player_color()
            if self.game.move_is_valid(transformed_coord, normalized_coord, color):
                self.set_new_stone(transformed_coord, normalized_coord)

    def set_new_gambit(self):
        self.game.set_new_move()
        hide_point = self.game.get_hide_stones()
        if len(hide_point) != 0:
            self.hide_stones(hide_point)

    def set_new_stone(self, transformed_coord, normalized_coord):
        self.check_timer()

        self.set_new_gambit()
        self.draw_new_stone(transformed_coord, normalized_coord)

        self.game.update_move_number_engine()
        self.draw_who_run(self.game.get_move_number_engine())

        self.set_not_pass_gambit()
        self.draw_points()
        self.game.print_log_game()
        # print("-" * 30)
        # print("ХОД ВАЛИДНЫЙ")

    def set_not_pass_gambit(self):
        if self.game.get_player_color() == PlayerColor.BLACK:
            self.col_pass_black = False
        else:
            self.col_pass_white = False

    def draw_points(self):
        black_groups, white_groups = self.game.get_black_white_groups()
        self.black_points = self.count_points.get_count_points_black(black_groups)
        self.white_points = self.count_points.get_count_points_white(white_groups)
        self.redraw_points_black(self.black_points)
        self.redraw_points_white(self.white_points)

    def draw_new_stone(self, transformed_coord, normalized_coord):
        if self.game.get_player_color() == PlayerColor.BLACK:
            self.draw_stone_b(transformed_coord, normalized_coord)
            self.enabled_buttons(False, True)
        else:
            self.draw_stone_w(transformed_coord, normalized_coord)
            self.enabled_buttons(True, False)

    def hide_stones(self, remove_group):
        for group in remove_group:
            for norm_coord in group:
                self.del_chip(norm_coord)

    def check_timer(self):
        if self.is_move_time:
            self.timer.stop()
            self.start_timer()

    def time_transition(self):
        self.check_timer()
        self.game.update_move_number_engine()

        self.draw_who_run(self.game.get_move_number_engine())

    def get_pass_black(self):
        self.check_timer()
        self.game.update_move_number_engine()
        self.draw_who_run(self.game.get_move_number_engine())

        self.col_pass_black = True
        self.pass_black.setEnabled(False)
        self.pass_white.setEnabled(True)

        if self.col_pass_white:
            # print("конец")
            self.draw_menu()

    def get_pass_white(self):
        self.check_timer()

        self.game.update_move_number_engine()

        self.draw_who_run(self.game.get_move_number_engine())

        self.col_pass_white = True
        self.pass_white.setEnabled(False)
        self.pass_black.setEnabled(True)

        if self.col_pass_black:
            # print("конец")
            self.draw_menu()

    def _close_time(self):
        if self.is_move_time or self.is_game_time:
            if self.timer.isActive():
                self.timer.stop()
        if self.is_smart_bot or self.is_random_bot:
            if self.timer_bot.isActive():
                self.timer_bot.stop()

    def draw_menu(self):
        self._close_time()
        self.close()
        new_win = EndGameInterFace(self, self.signal, self.black_points, self.white_points)
        new_win.show()

    def close_game(self):
        self._close_time()
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
