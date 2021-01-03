import time

from PyQt5.QtCore import QBasicTimer
from coordinates_generator.matrix_coordinates import MatrixCoordinates
from interface.response_interface import ResponseInterface
import random
from player_color import PlayerColor


class SmartBot(ResponseInterface):
    def __init__(self, is_move_time=None, is_game_time=None, all_time=None):
        super(SmartBot, self).__init__(is_move_time, is_game_time, all_time)
        self.matrix_coordinates_2 = MatrixCoordinates()
        self.transform_coords = self.matrix_coordinates_2.get_matrix_cord_trans()
        self.normalize_coords_2 = self.matrix_coordinates_2.get_matrix_cord_norm()
        self.set_frequency_render()
        self.color = PlayerColor.WHITE

    def set_frequency_render(self):
        self.timer_smart_bot = QBasicTimer()
        self.timer_smart_bot.start(300, self)

    def check_defender(self):
        kol_enemy = 0
        helped_stone = False
        for groups in self.game.white_groups:
            for norm_coord in groups:
                stone = self.game.normalize_coord_stones_dict[norm_coord]
                stone_enemy = len(stone.enemy_coordinates)
                if stone_enemy > 1 and stone_enemy != 4:
                    if stone_enemy > kol_enemy:
                        kol_enemy = stone_enemy
                        helped_stone = stone
        if helped_stone != False:
            new_moves_list_norm = self.get_list_moves(helped_stone)
            return self.is_valid_new_moves_list(new_moves_list_norm)
        return False

    def action(self):
        if self.check_defender():
            self.set_new_stone(self.transform_coord_bot, self.norm_cord)
            print("defender")
            return
        if self.check_attack():
            self.set_new_stone(self.transform_coord_bot, self.norm_cord)
            print("attack")
            return
        if self.smart_attack():
            self.set_new_stone(self.transform_coord_bot, self.norm_cord)
            print("smart_attack")
            return
        if self.check_create():
            self.set_new_stone(self.transform_coord_bot, self.norm_cord)
            print("create")
            return

        self.standard_move()

    def is_valid_new_moves_list(self, new_moves_list_norm):
        is_valid_new_move = False
        k = len(new_moves_list_norm)

        for norm_cord in new_moves_list_norm:
            trans_cord = self.matrix_coordinates.get_transformed_coord_norm(norm_cord)
            if self.is_valid_gambit(trans_cord, norm_cord, self.color):
                is_valid_new_move = True
                self.norm_cord = norm_cord
                self.transform_coord_bot = trans_cord
                break
            k += 1
        return is_valid_new_move

    def is_valid_specific_point(self, norm_cord):
        trans_cord = self.matrix_coordinates.get_transformed_coord_norm(norm_cord)
        if self.is_valid_gambit(trans_cord, norm_cord, self.color):
            self.norm_cord = norm_cord
            self.transform_coord_bot = trans_cord
            return True
        return False

    def check_attack(self):
        empty_stone = False
        best_attack_stone = False
        kol_enemy = 0
        for groups in self.game.black_groups:
            for norm_coord in groups:
                stone = self.game.normalize_coord_stones_dict[norm_coord]
                neighbors = len(stone.neighbor_coordinates)
                enemies = len(stone.enemy_coordinates)
                if neighbors == 0:
                    empty_stone = stone
                if enemies > 0 and enemies > kol_enemy and neighbors == 0:
                    kol_enemy = enemies
                    best_attack_stone = stone

        if best_attack_stone != False:
            new_moves_list_norm = self.get_list_moves(best_attack_stone)
            return self.is_valid_new_moves_list(new_moves_list_norm)
        elif empty_stone != False:
            new_moves_list_norm = self.get_list_moves(empty_stone)
            return self.is_valid_new_moves_list(new_moves_list_norm)
        return False

    def check_create(self):
        creation_stone = False
        for groups in self.game.white_groups:
            for norm_coord in groups:
                stone = self.game.normalize_coord_stones_dict[norm_coord]
                stone_enemy = len(stone.enemy_coordinates)
                if stone_enemy == 0:
                    creation_stone = stone
                    break
        if creation_stone != False:
            new_moves_list_norm = self.get_list_moves(creation_stone)
            return self.is_valid_new_moves_list(new_moves_list_norm)
        return False

    def what_is_color(self, cord_1):
        color_1 = False
        if cord_1 in self.game.normalize_coord_stones_dict:
            stone_1 = self.game.normalize_coord_stones_dict[cord_1]
            color_1 = stone_1.color
        return color_1

    def smart_attack(self):
        list_norm_cord = self.matrix_coordinates_2.get_matrix_cord_norm()
        for norm_cord in list_norm_cord:
            x, y = norm_cord[0], norm_cord[1]
            variant_horizontal = [(x - 1, y), (x + 1, y)]
            variant_vertical = [(x, y + 1), (x, y - 1)]
            horizontal_color = False
            vertical_color = False
            for norm_cord_hor in variant_horizontal:
                horizontal_color = self.what_is_color(norm_cord_hor)
                break
            for norm_cord_ver in variant_vertical:
                vertical_color = self.what_is_color(norm_cord_ver)
                break
            if horizontal_color != vertical_color and horizontal_color != False and vertical_color != False:
                return self.is_valid_specific_point(norm_cord)
        return False

    def standard_move(self):
        transform_coord_bot = random.choice(self.transform_coords)
        normalize_coord_bot = self.matrix_coordinates_2.get_normalize_coord(transform_coord_bot)
        if not self.is_valid_gambit(transform_coord_bot, normalize_coord_bot, self.color):
            self.standard_move()
        else:
            print("стандартный мув")
            self.set_new_stone(transform_coord_bot, normalize_coord_bot)

    def get_list_moves(self, stone):
        return [(stone.x_norm + 1, stone.y_norm),
                (stone.x_norm - 1, stone.y_norm),
                (stone.x_norm, stone.y_norm + 1),
                (stone.x_norm, stone.y_norm - 1)]

    def timerEvent(self, event):
        try:
            if self.get_player_color() == PlayerColor.WHITE:
                self.action()
        except Exception as e:
            print(e)
            self.pass_gambit()

    def pass_gambit(self):
        # print("pass")
        time.sleep(0.2)
        self.get_pass_white()
