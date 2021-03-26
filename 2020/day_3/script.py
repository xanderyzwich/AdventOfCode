"""
Day 3: Toboggan Trajectory
"""
from unittest import TestCase


class TobogganMap:

    def __init__(self, input_file_name):
        self.map = []
        with open(input_file_name, 'r') as input_file:
            [self.map.append(row.replace('\n', '')) for row in input_file]
        self.width = len(self.map[0])
        self.height = len(self.map)

    def slope_tree_count(self, right=3, down=1):
        _x, _y, count = right, down, 0
        while _y < self.height:
            count += 1 if '#' == self.get(_x, _y) else 0
            _x, _y = _x+right, _y+down
        return count

    def get(self, x, y):
        return self.map[y][x % self.width]

    def __str__(self):
        temp = ''
        for i in self.map:
            for j in i:
                temp += j + '  '
            temp += '\n'
        return temp + '\n'

    @property
    def paths_product(self):
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        my_product = 1
        for right, left in slopes:
            my_product *= self.slope_tree_count(right, left)
        return my_product


class TestTobogganMap(TestCase):

    def test_one_example(self):
        my_map = TobogganMap('example.txt')
        assert my_map.slope_tree_count(3, 1) == 7

    def test_one_data(self):
        my_map = TobogganMap('data.txt')
        assert my_map.slope_tree_count(3, 1) == 232

    def test_two_example(self):
        my_map = TobogganMap('example.txt')
        assert my_map.paths_product == 336

    def test_two_data(self):
        my_map = TobogganMap('data.txt')
        assert my_map.paths_product == 3952291680



