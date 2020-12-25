import copy
from engine.game_move_log import GameMoveLog
from engine.current_step_game import CurrentStepGame
from engine.groups_move import GroupsMove
from validate.validate import Validate
from validate.validate_game_rule import ValidateGameRule


class Game:
    def __init__(self):
        self.validate = Validate()
        self.game_move_log = GameMoveLog()

        self.normalize_coord_stones_dict = {}

        self.black_groups = []
        self.white_groups = []

        self.removed_black_group = []
        self.removed_white_group = []

    def move_is_valid(self, transformed_coord, normalize_coord, color):
        self.current_step_game = CurrentStepGame(transformed_coord, normalize_coord,
                                                 copy.deepcopy(self.normalize_coord_stones_dict), self.black_groups,
                                                 self.white_groups, color,)

        normalize_coord_stones_dict = self.current_step_game.normalize_coord_stones_dict

        new_black_groups = self.current_step_game.new_black_groups
        new_white_groups = self.current_step_game.new_white_groups

        self.validate_game_rule = ValidateGameRule(
            normalize_coord_stones_dict, new_black_groups, new_white_groups, color)

        self.validate_game_rule.update_dame_groups()
        answer = self.validate_game_rule.make_decision()

        return answer

    def set_new_move(self):
        self.black_groups = self.current_step_game.new_black_groups
        self.white_groups = self.current_step_game.new_white_groups

        self.normalize_coord_stones_dict = (
            self.current_step_game.normalize_coord_stones_dict)

        self.game_move_log.update_game_move_log(
            GroupsMove(self.black_groups, self.white_groups))

    def delete_stones_in_dict(self, removed_groups):
        for group in removed_groups:
            for norm_cord in group:
                self.normalize_coord_stones_dict.pop(norm_cord)

    def print_log_game(self):
        print("Все точки на карте:")

        for cord in self.normalize_coord_stones_dict:
            print(cord)

        print(self.black_groups, " <--- black groups")
        print(self.white_groups, " <--- white_groups")

    def get_black_white_groups(self):
        return self.black_groups, self.white_groups

    def get_removed_groups(self):
        return self.validate_game_rule.removed_black_group, self.validate_game_rule.removed_white_group

    def validate_set_stones(self, x_mouse, y_mouse):
        return self.validate.validate_set_stones(x_mouse, y_mouse, self.normalize_coord_stones_dict)
