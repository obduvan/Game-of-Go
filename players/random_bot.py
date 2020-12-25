from coordinates_generator.matrix_coordinates import MatrixCoordinates
from interface.response_interface import ResponseInterface
import random


class RandomBot(ResponseInterface):
    def __init__(self):
        super(RandomBot, self).__init__()
        self.matrix_coordinates_2 = MatrixCoordinates()
        self.transform_coords = self.matrix_coordinates_2.get_matrix_cord_trans()

    def get_random_ind(self):
        ind = random.randrange(0, 80)
        return ind

    def action(self):
        index_transform_coord = self.get_random_ind()
        transform_coord_bot = self.transform_coords[index_transform_coord]
        normalize_coord_bot = self.matrix_coordinates_2.get_normalize_coord(transform_coord_bot)
        if not self.is_valid_gambit(transform_coord_bot, normalize_coord_bot, "White"):
            self.action()
        else:
            self.set_new_stone(transform_coord_bot, normalize_coord_bot)

    def mouseReleaseEvent(self, event):
        self.action()
