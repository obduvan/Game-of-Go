import os
import sys
import unittest

from engine.count_points import CountPoints

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))


class TestGroupsMove(unittest.TestCase):
    def setUp(self):
        self.default_obj = CountPoints()

    def test_count_white_1(self):
        white_groups = [[(6, 4)], [(3, 7)], [(6, 6)], [(5, 8), (6, 8), (7, 8)]]
        check_point = self.default_obj.get_count_points_white(white_groups)
        self.assertEqual(check_point, 6)

    def test_count_black_1(self):
        black_groups = [[(3, 6)], [(2, 4)], [(5, 3)], [(5, 7), (6, 7), (7, 7), (1, 1)]]
        check_point = self.default_obj.get_count_points_white(black_groups)
        self.assertEqual(check_point, 7)

    def test_count_white_2(self):
        white_groups = [[(1, 1)], [(1, 4)], [(1, 2)], [(5, 5)], [(6, 6), (1, 2)]]
        check_point = self.default_obj.get_count_points_white(white_groups)
        self.assertEqual(check_point, 6)

    def test_count_black_2(self):
        black_groups = [[(3, 6)], [(2, 4)], [(5, 3)], [(5, 7), (6, 7), (7, 7), (1, 1)],
                        [(7, 7), (7, 8), (8, 8), (4, 4), (3, 3), (2, 2)]]
        check_point = self.default_obj.get_count_points_white(black_groups)
        self.assertEqual(check_point, 13)
