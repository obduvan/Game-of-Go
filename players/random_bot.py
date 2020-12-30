import time

from PyQt5.QtCore import QBasicTimer
from coordinates_generator.matrix_coordinates import MatrixCoordinates
from interface.response_interface import ResponseInterface
import random
from player_color import PlayerColor


class RandomBot(ResponseInterface):
    def __init__(self):
        super(RandomBot, self).__init__()
        self.matrix_coordinates_2 = MatrixCoordinates()
        self.transform_coords = self.matrix_coordinates_2.get_matrix_cord_trans()
        self.set_frequency_render()

    def set_frequency_render(self):
        self.timer = QBasicTimer()
        self.timer.start(300, self)

    def action(self):
        transform_coord_bot = random.choice(self.transform_coords)
        normalize_coord_bot = self.matrix_coordinates_2.get_normalize_coord(transform_coord_bot)
        if not self.is_valid_gambit(transform_coord_bot, normalize_coord_bot, PlayerColor.WHITE):
            try:
                self.action()
            except Exception:
                self.pass_gambit()
        else:
            time.sleep(0.1)
            self.set_new_stone(transform_coord_bot, normalize_coord_bot)

    def timerEvent(self, event):
        if self.get_player_color() == PlayerColor.WHITE:
            self.action()


    def pass_gambit(self):
        print("pass")
        self.get_pass_white()
