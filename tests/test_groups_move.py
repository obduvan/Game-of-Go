import os
import sys
import unittest

from engine.groups_move import GroupsMove

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))


class TestGroupsMove(unittest.TestCase):
    def setUp(self):
        self.black_groups = [[1, 2], [1, 4], [1343, 1]]
        self.white_groups = [[2, 2], [3, 4], [1343, 1]]
        self.default_obj = GroupsMove(self.black_groups, self.white_groups)

    def test_same_objects(self):
        other_black_groups = [[1, 2], [1, 4], [1343, 1]]
        other_white_groups = [[2, 2], [3, 4], [1343, 1]]
        self.other_obj = GroupsMove(other_black_groups, other_white_groups)
        self.assertEqual(self.default_obj.is_same_move_groups(self.other_obj), True)

    def test_different_objects(self):
        other_black_groups = [[3123, 2], [1, 321], [1343, 3132], [2, 1]]
        other_white_groups = [[3123, 31], [3, 3123], [1343, 312], [32, 21]]
        self.other_obj = GroupsMove(other_black_groups, other_white_groups)
        self.assertEqual(self.default_obj.is_same_move_groups(self.other_obj), False)

    def test_different_one_of(self):
        other_black_groups = [[11, 2], [1, 4], [1343, 1]]
        other_white_groups = [[2, 2], [3, 4], [1343, 1]]
        self.other_obj = GroupsMove(other_black_groups, other_white_groups)
        self.assertEqual(self.default_obj.is_same_move_groups(self.other_obj), False)
