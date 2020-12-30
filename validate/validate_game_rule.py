

from player_color import PlayerColor


class ValidateGameRule:
    def __init__(
        self, normalize_coord_stones_dict, new_black_groups, new_white_groups, color
    ):
        self.color_stone = color
        self.normalize_coord_stones_dict = normalize_coord_stones_dict
        self.stone = None

        self.new_black_groups = new_black_groups
        self.new_white_groups = new_white_groups

        self.is_new_black_has_died = False
        self.is_new_white_has_died = False

        self.removed_black_group = []
        self.removed_white_group = []

        self.VALID_MOVE = False

    def update_dame_groups(self):
        self.removed_black_group = self.update_DAME_group_color((self.new_black_groups))
        self.removed_white_group = self.update_DAME_group_color((self.new_white_groups))

        self.set_is_new_black_has_died()
        self.set_is_new_white_has_died()

    def set_is_new_black_has_died(self):
        if len(self.removed_black_group) != 0:
            self.is_new_black_has_died = True

    def set_is_new_white_has_died(self):
        if len(self.removed_white_group) != 0:
            self.is_new_white_has_died = True

    def update_DAME_group_color(self, new_color_groups):
        n = 0
        removed_groups = []
        for color_group in new_color_groups:
            for coord in color_group:
                if len(self.normalize_coord_stones_dict[coord].list_dames) == 0:
                    n += 1
            if n == len(color_group):
                new_color_groups.remove(color_group)
                removed_groups.append(color_group)
                print(color_group, " <--- мертва")
            n = 0

        return removed_groups

    def make_decision(self):
        if self.color_stone == PlayerColor.BLACK:
            if self.is_new_black_has_died:
                if self.is_new_white_has_died:
                    self.VALID_MOVE = True
                else:
                    self.VALID_MOVE = False
            else:
                self.VALID_MOVE = True
        else:
            if self.is_new_white_has_died:
                if self.is_new_black_has_died:
                    self.VALID_MOVE = True
                else:
                    self.VALID_MOVE = False
            else:
                self.VALID_MOVE = True
        return self.VALID_MOVE

    def is_ko_situation(self):
        pass
