from MatrixCoordinates import MatrixCoordinates


class Validate:
    def __init__(self):
        self.matrix_coordinates = MatrixCoordinates()

    def validate_gamer_zone(self, x_mouse, y_mouse):
        """Проверка попадания курсора в игровую зону"""

        h_l = (275, 275)
        d_r = (564, 564)

        if h_l[0] - 5 < x_mouse and x_mouse < d_r[0] + 5:
            if h_l[1] - 5 < y_mouse and y_mouse < d_r[1] + 5:
                return True
        return False

    def validate_free_place(self, coordinates_stones_dict, x_norm, y_norm):
        """Проверка на свободное место на карте"""

        return (x_norm, y_norm) not in coordinates_stones_dict

    def validate_set_stones(self, x_mouse, y_mouse, normalize_coord_stones_dict):
        if self.validate_gamer_zone(x_mouse, y_mouse):
            x_trans, y_trans = self.matrix_coordinates.transformed_coord_mouse(x_mouse, y_mouse)
            x_norm, y_norm = self.matrix_coordinates.get_normalize_coord((x_trans, y_trans))
            return self.validate_free_place(normalize_coord_stones_dict, x_norm, y_norm)

        return False

