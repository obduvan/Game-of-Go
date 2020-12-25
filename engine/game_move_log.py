class GameMoveLog:
    def __init__(self):
        self._game_num_groups_dict = {}
        self._num = 0

    def update_game_move_log(self, groups_game):
        self._num += 1
        self._game_num_groups_dict.update({self._num: groups_game})

    def get_some_game_groups(self, num):
        return self._game_num_groups_dict.get(num)

    def get_game_move_log_dict(self):
        return self._game_num_groups_dict
