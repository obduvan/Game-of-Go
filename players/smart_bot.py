from coordinates_generator.matrix_coordinates import MatrixCoordinates
import random
from constants.player_color import PlayerColor


class SmartBot:
    def __init__(self, game):
        self.matrix_coordinates_2 = MatrixCoordinates()
        self.game = game
        self.transform_coords = self.matrix_coordinates_2.get_matrix_cord_trans()
        self.normalize_coords_2 = self.matrix_coordinates_2.get_matrix_cord_norm()
        self.color = PlayerColor.WHITE

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
        if helped_stone:
            new_moves_list_norm = self.get_list_moves(helped_stone)
            return self.is_valid_new_moves_list(new_moves_list_norm)
        return False

    def queens_gambit(self):
        if self.check_defender():
            # print("defender")
            return True

        if self.check_attack():
            # print("attack")
            return True

        if self.smart_attack():
            # print("smart_attack")
            return True

        if self.check_create():
            # print("create")
            return True

        return False

    def action(self):
        if self.queens_gambit():
            return {"type": "move", "trans_cord": self.transform_coord_bot, "norm_cord": self.norm_cord}
        else:
            return self.standard_move()

    def is_valid_new_moves_list(self, new_moves_list_norm):
        is_valid_new_move = False
        k = len(new_moves_list_norm)

        for norm_cord in new_moves_list_norm:
            trans_cord = self.matrix_coordinates_2.get_transformed_coord_norm(norm_cord)
            if self.game.move_is_valid(trans_cord, norm_cord, self.color):
                is_valid_new_move = True
                self.norm_cord = norm_cord
                self.transform_coord_bot = trans_cord
                break
            k += 1
        return is_valid_new_move

    def is_valid_specific_point(self, norm_cord):
        trans_cord = self.matrix_coordinates_2.get_transformed_coord_norm(norm_cord)
        if self.game.move_is_valid(trans_cord, norm_cord, self.color):
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

        if best_attack_stone:
            new_moves_list_norm = self.get_list_moves(best_attack_stone)
            return self.is_valid_new_moves_list(new_moves_list_norm)
        elif empty_stone:
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
        if creation_stone:
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
            if horizontal_color != vertical_color and horizontal_color and vertical_color:
                return self.is_valid_specific_point(norm_cord)
        return False

    def standard_move(self):
        transform_coord_bot = random.choice(self.transform_coords)
        normalize_coord_bot = self.matrix_coordinates_2.get_normalize_coord(transform_coord_bot)
        if not self.game.move_is_valid(transform_coord_bot, normalize_coord_bot, self.color):
            try:
                return self.standard_move()
            except Exception:
                return self.pass_gambit()
        else:
            # print("стандартный мув")
            return {"type": "move", "trans_cord": transform_coord_bot, "norm_cord": normalize_coord_bot}

    def get_list_moves(self, stone):
        return [(stone.x_norm + 1, stone.y_norm),
                (stone.x_norm - 1, stone.y_norm),
                (stone.x_norm, stone.y_norm + 1),
                (stone.x_norm, stone.y_norm - 1)]

    def pass_gambit(self):
        return {"type": "pass", "trans_cord": (0, 0), "norm_cord": (0, 0)}
