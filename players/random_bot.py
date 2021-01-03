import time

from coordinates_generator.matrix_coordinates import MatrixCoordinates
import random
from player_color import PlayerColor


class RandomBot:
    def __init__(self, game):
        self.game = game
        self.matrix_coordinates_2 = MatrixCoordinates()
        self.transform_coords = self.matrix_coordinates_2.get_matrix_cord_trans()
        self.normalize_coords_2 = self.matrix_coordinates_2.get_matrix_cord_norm()
        self.color = PlayerColor.WHITE

    def diff_set(self):
        return list(set(self.normalize_coords_2) - set(self.game.normalize_coord_stones_dict.keys()))

    def action(self):
        transform_coord_bot = random.choice(self.transform_coords)
        normalize_coord_bot = self.matrix_coordinates_2.get_normalize_coord(transform_coord_bot)
        if not self.game.move_is_valid(transform_coord_bot, normalize_coord_bot, self.color):
            try:
                return self.action()
            except Exception:
                return self.pass_gambit()
        else:
            time.sleep(0.1)
            return {"type": "move", "trans_cord": transform_coord_bot, "norm_cord": normalize_coord_bot}

    def pass_gambit(self):
        print("passss")
        return {"type": "pass", "trans_cord": (0, 0), "norm_cord": (0, 0)}
