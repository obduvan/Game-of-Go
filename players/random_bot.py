import time

from PyQt5.QtCore import QBasicTimer
from coordinates_generator.matrix_coordinates import MatrixCoordinates
from interface.response_interface import ResponseInterface
import random
from player_color import PlayerColor


class RandomBot(ResponseInterface):
    def __init__(self, is_move_time=None, is_game_time=None, all_time=None):
        super(RandomBot, self).__init__(is_move_time, is_game_time, all_time)
        self.matrix_coordinates_2 = MatrixCoordinates()
        self.transform_coords = self.matrix_coordinates_2.get_matrix_cord_trans()
        self.normalize_coords_2 = self.matrix_coordinates_2.get_matrix_cord_norm()
        self.set_frequency_render()
        self.color = PlayerColor.WHITE

    def set_frequency_render(self):
        self.timer_random_bot = QBasicTimer()
        self.timer_random_bot.start(300, self)

    def diff_set(self):
        return list(set(self.normalize_coords_2) - set(self.game.normalize_coord_stones_dict.keys()))

    def action(self):
        transform_coord_bot = random.choice(self.transform_coords)
        normalize_coord_bot = self.matrix_coordinates_2.get_normalize_coord(transform_coord_bot)
        if not self.is_valid_gambit(transform_coord_bot, normalize_coord_bot, self.color):
            try:
                self.action()
            except Exception:
                self.pass_gambit()
        else:
            time.sleep(0.1)
            self.set_new_stone(transform_coord_bot, normalize_coord_bot)

    def timerEvent(self, event):
        if self.game.get_player_color() == self.color:
            self.action()

    def pass_gambit(self):
        # print("pass")
        self.get_pass_white()
