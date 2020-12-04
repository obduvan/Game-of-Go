from matrix_coordinates import MatrixCoordinates
from validate.validate import Validate


class Stone:
    def __init__(self, x_norm, y_norm, color, normalize_coord_stones_dict):
        self.normalize_coord_stones_dict = normalize_coord_stones_dict
        self.x_norm = x_norm
        self.y_norm = y_norm
        self.color = color
        self.validate = Validate()
        self.matrix_coordinates = MatrixCoordinates()

        self.list_dames = []
        self.neighbor_stones = []
        self.neighbor_coordinates = []

    def coordinates_generator(self):
        for new_x_norm, new_y_norm in [
            (self.x_norm, self.y_norm + 1),
            (self.x_norm, self.y_norm - 1),
            (self.x_norm + 1, self.y_norm),
            (self.x_norm - 1, self.y_norm),
        ]:
            yield new_x_norm, new_y_norm

    def update_list_dames(self):
        self.list_dames = []
        for new_x_norm, new_y_norm in self.coordinates_generator():
            (
                new_x_trans,
                new_y_trans,
            ) = self.matrix_coordinates.get_transformed_coord_norm(
                (new_x_norm, new_y_norm)
            )
            if self.validate.validate_gamer_zone(new_x_trans, new_y_trans):
                if self.validate.validate_free_place(
                    self.normalize_coord_stones_dict, new_x_norm, new_y_norm
                ):
                    self.list_dames.append((new_x_norm, new_y_norm))

    def check_neighbor_stone_and_coordinates(self):
        self.neighbor_stones = []
        self.neighbor_coordinates = []
        for new_x_norm, new_y_norm in self.coordinates_generator():
            (
                new_x_trans,
                new_y_trans,
            ) = self.matrix_coordinates.get_transformed_coord_norm(
                (new_x_norm, new_y_norm)
            )
            if self.validate.validate_gamer_zone(new_x_trans, new_y_trans):
                if not self.validate.validate_free_place(
                    self.normalize_coord_stones_dict, new_x_norm, new_y_norm
                ):
                    if (
                        self.normalize_coord_stones_dict[(new_x_norm, new_y_norm)].color
                        == self.color
                    ):
                        self.neighbor_stones.append(
                            self.normalize_coord_stones_dict[(new_x_norm, new_y_norm)]
                        )
                        self.neighbor_coordinates.append((new_x_norm, new_y_norm))

    def i_am_dead(self):
        if len(self.list_dames) == 0:
            print(self.x_norm, self.y_norm, "died")
