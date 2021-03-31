import os
import sys
import unittest

from engine.game import Game
from player_color import PlayerColor

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))


class TestSetChip(unittest.TestCase):
    def setUp(self):
        self.color_white = PlayerColor.WHITE
        self.color_black = PlayerColor.BLACK

    def move(self, trans_cord, norm_cord, game, color):
        if game.move_is_valid(trans_cord, norm_cord, color):
            game.set_new_move()
            hide_point = game.get_hide_stones()

    def test_black_chips(self):
        """Тестируем постановку черных фишек, и определения черных групп"""

        game = Game()
        self.move((555, 310), (9, 8), game, self.color_black)
        self.move((520, 310), (8, 8), game, self.color_black)
        self.move((485, 310), (7, 8), game, self.color_black)
        self.move((450, 310), (6, 8), game, self.color_black)
        self.move((275, 555), (1, 1), game, self.color_black)
        self.move((310, 555), (2, 1), game, self.color_black)
        self.move((345, 555), (3, 1), game, self.color_black)

        expected_black_groups = [[(9, 8), (8, 8), (7, 8), (6, 8)], [(1, 1), (2, 1), (3, 1)]]
        actual_black_groups = game.get_black_groups()

        self.assertEqual(actual_black_groups, expected_black_groups)

    def test_white_chips(self):
        """Тестируем постановку белых фишек, и определения белых групп"""

        game = Game()
        self.move((450, 450), (6, 4), game, self.color_white)
        self.move((485, 450), (7, 4), game, self.color_white)
        self.move((520, 450), (8, 4), game, self.color_white)
        self.move((275, 275), (1, 9), game, self.color_white)
        self.move((555, 555), (9, 1), game, self.color_white)

        expected_white_groups = [[(6, 4), (7, 4), (8, 4)], [(1, 9)], [(9, 1)]]
        actual_white_groups = game.get_white_groups()

        self.assertEqual(actual_white_groups, expected_white_groups)

    def test_white_black_chips(self):
        """Тестируем постановку фишек обоих цветов, и определения обоих групп"""

        game = Game()
        self.move((345, 380), (3, 6), game, self.color_white)
        self.move((310, 380), (2, 6), game, self.color_white)
        self.move((275, 380), (1, 6), game, self.color_white)
        self.move((380, 555), (4, 1), game, self.color_white)
        self.move((415, 555), (5, 1), game, self.color_white)

        self.move((380, 310), (4, 8), game, self.color_black)
        self.move((380, 310), (4, 8), game, self.color_black)
        self.move((310, 310), (2, 8), game, self.color_black)
        self.move((275, 310), (1, 8), game, self.color_black)

        expected_black_groups = [[(4, 8)], [(2, 8), (1, 8)]]
        actual_white_groups = game.get_white_groups()
        actual_black_groups = game.get_black_groups()
        expected_white_groups = [[(3, 6), (2, 6), (1, 6)], [(4, 1), (5, 1)]]
        self.assertEqual(actual_black_groups, expected_black_groups)
        self.assertEqual(actual_white_groups, expected_white_groups)
