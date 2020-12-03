from MatrixCoordinates import MatrixCoordinates
from player_color import PlayerColor
from previous_game_snapshot import PreviousGameSnapshot
from stone.stone import Stone
from validate.validate import Validate


class Game:
    def __init__(self):
        self.matrix_coordinates = MatrixCoordinates()
        self.matrix_board_interface = self.matrix_coordinates.get_matrix_cord_trans()
        self.previous_game_snapshot = PreviousGameSnapshot()
        self._coordinates_stones_dict = {}
        self.validate = Validate()

        self.previous_black_groups = []
        self.previous_white_groups = []

        self.black_groups = []
        self.white_groups = []
        self.last_stone = None

    def set_new_stone(self, color, normalize_coord):
        stone = Stone(normalize_coord[0], normalize_coord[1], color)

        stone.check_dame(self._coordinates_stones_dict)
        stone.check_neighbor_stone_and_coordinates(self._coordinates_stones_dict)
        self.last_stone = stone
        self._coordinates_stones_dict.update({normalize_coord: stone})

    def check_free_dame(self):
        for i in self._coordinates_stones_dict:
            self._coordinates_stones_dict[i].check_dame(self._coordinates_stones_dict)
            self._coordinates_stones_dict[i].check_neighbor_stone_and_coordinates(self._coordinates_stones_dict)

    def validate_set_stones(self, x_mouse, y_mouse, color):
        if self.validate.validate_gamer_zone(x_mouse, y_mouse):
            x_trans, y_trans = self.matrix_coordinates.transformed_coord_mouse(x_mouse, y_mouse)
            x_norm, y_norm = self.matrix_coordinates.get_normalize_coord((x_trans, y_trans))
            return self.validate.validate_free_place(self._coordinates_stones_dict, x_norm, y_norm)

        return False

    def white_or_black_stone(self, stone):
        return stone.color == PlayerColor.WHITE

    def update_groups(self, main_color):
        print(main_color)
        if main_color == PlayerColor.WHITE:
            self.white_groups = self._update_gr(self.white_groups)
        else:
            self.black_groups = self._update_gr(self.black_groups)

        print("black group  ", self.black_groups)
        print("white_group  ", self.white_groups)

    def _update_gr(self, groups):
        new_group = []
        for neighbor_coord in self.last_stone.neighbor_coordinates:
            for group in groups:
                if neighbor_coord in group:
                    new_group += group
                    groups.remove(group)

        new_group.append((self.last_stone.x_norm, self.last_stone.y_norm))
        groups.append(new_group)
        return groups

    def clear_dict_norm_coord(self, removed_group):
        for group in removed_group:
            for norm_coord in group:
                self._coordinates_stones_dict.pop(norm_coord)

    def is_suicide_move(self, color_main, color_sec):
        return len(color_main) != 0 and len(color_sec)

    def remove_dead_stones(self, main_color):
        VALID_MOVE = True
        prev_black_groups = self.black_groups
        prev_white_groups = self.white_groups
        new_black_groups, removed_groups_black = self.remove_group(self.black_groups)
        new_white_groups, removed_groups_white = self.remove_group(self.white_groups)
        removed_groups = removed_groups_white + removed_groups_black
        NO_VALID_CORD = (self.last_stone.x_norm, self.last_stone.y_norm)

        if main_color == PlayerColor.WHITE:
            if self.is_suicide_move(removed_groups_white, removed_groups_black):
                VALID_MOVE = False
                # self.white_groups = self._restore_group(removed_groups_white, self.white_groups, NO_VALID_CORD)
                # self.white_groups = self.previous_white_groups

                # self._coordinates_stones_dict.pop(NO_VALID_CORD)
        else:
            if self.is_suicide_move(removed_groups_black, removed_groups_white):
                VALID_MOVE = False
                # self.black_groups = self._restore_group(removed_groups_black, self.black_groups, NO_VALID_CORD)
                # self.black_groups = self.previous_black_groups
                # self._coordinates_stones_dict.pop(NO_VALID_CORD)

        # if VALID_MOVE:
        #     self.clear_dict_norm_coord(removed_groups)
        #     self.set_prev_game()
        #     self.previous_white_groups = prev_white_groups
        #     self.previous_black_groups = prev_black_groups
        # else:
        #     self.white_groups = self.previous_game_snapshot.white_groups
        #     self.black_groups = self.previous_game_snapshot.black_groups

        print("-"*30)
        for i in self._coordinates_stones_dict:
            print(i)
        return removed_groups, VALID_MOVE

    def set_prev_game(self):
        self.previous_game_snapshot.coordinates_stones_dict = self._coordinates_stones_dict
        self.previous_game_snapshot.white_groups = self.w

    def _restore_group(self, reset_color_groups, color_groups, NO_VALID_CORD):
        print(reset_color_groups, "Восстановили")

        for color_group in reset_color_groups:
            color_groups.append(color_group)
        return color_groups

    def remove_group(self, color_groups):
        n = 0
        removed_groups = []
        for color_group in color_groups:
            for coord in color_group:
                if len(self._coordinates_stones_dict[coord].list_dames) == 0:
                    n += 1
            if n == len(color_group):
                color_groups.remove(color_group)
                removed_groups.append(color_group)
                print(color_group, "   мертва")
            n = 0

        return color_groups, removed_groups
