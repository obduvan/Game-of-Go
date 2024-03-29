import functools


class GroupsMove:
    def __init__(self, black_groups, white_groups):
        self.black_groups = black_groups
        self.white_groups = white_groups

    def is_same_move_groups(self, other_game_move_log):
        other_black_groups = other_game_move_log.black_groups
        other_white_groups = other_game_move_log.white_groups

        return self._check_group(self.black_groups, other_black_groups) and self._check_group(self.white_groups, other_white_groups)

    def _check_group(self, other_groups, groups):
        return functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, other_groups, groups), True)
