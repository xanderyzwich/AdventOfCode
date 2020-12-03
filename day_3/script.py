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
        # print(f'Map created with {self.width} x {self.height} shape')
        # print(self)

    def slope_tree_count(self, x, y, right=3, down=1):
        _x, _y, count = x+right, y+down, 0
        while _y < self.height:
            # print('spot = ', self.get(_x, _y))
            count += 1 if '#' == self.get(_x, _y) else 0
            _x, _y = _x+right, _y+down
        # print(count)
        return count

    def get(self, x, y):
        # print(x, y)
        return self.map[y][x % self.width]

    def __str__(self):
        temp = ''
        for i in self.map:
            for j in i:
                temp += j + '  '
            temp += '\n'
        return temp + '\n'

def tobaggan_path_product(input_file_name):
    my_map = TobogganMap(input_file_name)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    my_product = 1
    for right, left in slopes:
        my_product *= my_map.slope_tree_count(0, 0, right, left)
    # print(my_product)
    return my_product


class TestTobogganMap(TestCase):

    def test_one_example(self):
        my_map = TobogganMap('example.txt')
        assert my_map.slope_tree_count(0, 0) == 7

    def test_one_data(self):
        my_map = TobogganMap('data.txt')
        assert my_map.slope_tree_count(0, 0) == 232

    def test_two_example(self):
        assert tobaggan_path_product('example.txt') == 336

    def test_two_data(self):
        assert tobaggan_path_product('data.txt') == 3952291680



