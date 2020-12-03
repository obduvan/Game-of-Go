class Validate:
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

