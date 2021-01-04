import os
import sys
import unittest

from engine.game import Game
from player_color import PlayerColor
from players.smart_bot import SmartBot

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))


class TestSmartBot(unittest.TestCase):
    def setUp(self):
        self.color = PlayerColor.BLACK
        self.color_bot = PlayerColor.WHITE

    def move(self, trans_cord, norm_cord, game, color):
        if game.move_is_valid(trans_cord, norm_cord, color):
            game.set_new_move()
            hide_point = game.get_hide_stones()

    def test_attack(self):
        """Тест атаки бота.
        Заполняем доску четырмя фишками, отдаленных друг от друга.
        Такие фишки легко закрыть с помощью 16 ходов: 4 дыхания на каждую фишку"""

        game = Game()
        self.move((275, 275), (9, 9), game, self.color)
        self.move((555, 555), (9, 1), game, self.color)
        self.move((555, 380), (9, 6), game, self.color)
        self.move((380, 450), (4, 4), game, self.color)

        bot = SmartBot(game)
        for i in range(16):
            response = bot.action()
            game.set_new_move()
        expected_black_groups = []
        actual_black_groups = game.get_black_groups()
        self.assertEqual(actual_black_groups, expected_black_groups)

    def test_defender(self):
        """Тест защиты бота.
        Окружаем белую фишку тремя черными.
        Бот должен увеличить дыхания для данной фишки"""

        game = Game()
        self.move((380, 450), (4, 4), game, self.color_bot)

        self.move((345, 450), (3, 4), game, self.color)
        self.move((415, 450), (5, 4), game, self.color)
        self.move((380, 485), (4, 3), game, self.color)

        bot = SmartBot(game)
        response = bot.action()
        game.set_new_move()
        expected_white_groups = [[(4, 4), (4, 5)]]
        actual_white_groups = game.get_white_groups()
        self.assertEqual(actual_white_groups, expected_white_groups)

    def test_cold_war(self):
        """Тест: "не ввязываемся в борьбу".
        Черные фишки имеют много дыханий и стоят монолитно вдалеке от белых.
        Фишки бота (белые) имеют намного меньше дыхания. В данном случае они будут строить оборону
        на расстоянии (2-3клетки) от черных"""

        game = Game()
        self.move((380, 450), (4, 4), game, self.color)
        self.move((345, 450), (3, 4), game, self.color)
        self.move((380, 415), (4, 5), game, self.color)
        self.move((380, 485), (4, 3), game, self.color)
        self.move((380, 380), (4, 6), game, self.color)

        self.move((345, 310), (3, 8), game, self.color_bot)
        self.move((310, 310), (2, 8), game, self.color_bot)

        bot = SmartBot(game)
        for i in range(2):
            response = bot.action()
            game.set_new_move()
        expected_white_groups = [[(3, 8), (2, 8), (4, 8), (3, 9)]]
        actual_white_groups = game.get_white_groups()
        self.assertEqual(actual_white_groups, expected_white_groups)

    def test_smart_attack(self):
        """Тест умной атаки.
        Белые и Черные фишки имеют достаточно дыханий и стоят рядом (>=3).
        Это самая частая ситуация в ГО. В данной ситуации нужно атаковать-защищать"""

        game = Game()
        self.move((275, 275), (1, 9), game, self.color)
        self.move((275, 310), (1, 8), game, self.color)
        self.move((275, 345), (1, 7), game, self.color)
        self.move((275, 380), (1, 6), game, self.color)

        self.move((310, 310), (2, 8), game, self.color_bot)

        bot = SmartBot(game)
        response = bot.action()
        game.set_new_move()

        expected_white_groups = [[(2, 8), (2, 7)]]
        actual_white_groups = game.get_white_groups()
        self.assertEqual(actual_white_groups, expected_white_groups)


