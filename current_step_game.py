from player_color import PlayerColor
from stone.stone import Stone


class CurrentStepGame:
    def __init__(self, transformed_coord, normalize_coord, normalize_coord_stones_dict, black_groups, white_groups, color):
        self.transformed_coord = transformed_coord
        self.normalize_coord = normalize_coord

        self.color_stone = color
        self.normalize_coord_stones_dict = normalize_coord_stones_dict
        self.black_groups = black_groups
        self.white_groups = white_groups

        self.stone = None

        self.new_black_groups = []
        self.new_white_groups = []

        self.work()

    def work(self):
        self._init_stone()
        self._add_stone_to_dict()
        self._update_groups()
        self.update_other_dames()


    def _init_stone(self):
        self.stone = Stone(self.normalize_coord[0], self.normalize_coord[1], self.color_stone, self.normalize_coord_stones_dict)
        self.stone.update_list_dames()
        self.stone.check_neighbor_stone_and_coordinates()

    def _add_stone_to_dict(self):
        self.normalize_coord_stones_dict.update({self.normalize_coord: self.stone})

    def _update_groups(self):
        if self.color_stone == PlayerColor.BLACK:
            self.new_black_groups = self.update_group_color(self.black_groups)
            self.new_white_groups = self.white_groups
        else:
            self.new_white_groups = self.update_group_color(self.white_groups)
            self.new_black_groups = self.black_groups

        print(self.new_black_groups, " black new")
        print(self.new_white_groups, " white new")

    def update_other_dames(self):
        for norm_coord in self.normalize_coord_stones_dict:
            self.normalize_coord_stones_dict[norm_coord].update_list_dames()
            self.normalize_coord_stones_dict[norm_coord].check_neighbor_stone_and_coordinates()

    def update_group_color(self, color_all_groups):
        new_group = []
        for neighbor_coord in self.stone.neighbor_coordinates:
            for group in color_all_groups:
                if neighbor_coord in group:
                    new_group += group
                    color_all_groups.remove(group)

        new_group.append((self.stone.x_norm, self.stone.y_norm))
        color_all_groups.append(new_group)
        return color_all_groups
