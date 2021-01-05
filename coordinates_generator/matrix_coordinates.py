class MatrixCoordinates:
    def __init__(self):
        self._matrix_cord_trans = []
        self._normalize_coord = {}
        self._matrix_cord_norm = []

        self._set_matrix_board()
        self._set_normalize_coord()

    def _set_matrix_board(self):
        x, y = 275, 275
        for i in range(9):
            for k in range(9):
                self._matrix_cord_trans.append((x, y))
                x += 35
            y += 35
            x = 275

    def _set_normalize_coord(self):
        n = 0
        xx, yy = 1, 9
        for i in range(9):
            for k in range(9):
                self._normalize_coord.update({self._matrix_cord_trans[n]: (xx, yy)})
                self._matrix_cord_norm.append((xx, yy))
                n += 1
                xx += 1
            xx = 1
            yy -= 1

    def transformed_coord_mouse(self, x_mouse, y_mouse):
        transformed_coord = 0, 0
        length = 100

        for point in self._matrix_cord_trans:
            x_len = abs(point[0] - x_mouse)
            y_len = abs(point[1] - y_mouse)
            res = y_len + x_len
            if res < length:
                length = res
                transformed_coord = point

        return transformed_coord

    def get_matrix_cord_norm(self):
        return self._matrix_cord_norm

    def get_matrix_cord_trans(self):
        return self._matrix_cord_trans

    def get_normalize_coord(self, coord_trans):
        return self._normalize_coord[coord_trans]

    def get_transformed_coord_norm(self, coord_norm):
        for i in self._normalize_coord:
            if coord_norm == self._normalize_coord[i]:
                return i
        return 10**3, 10**3

    def get_dict(self):
        return self._normalize_coord
