"""
Day 2: Dive!
"""
from unittest import TestCase


def convert_file_to_tuple_list(file_name):
    tuple_list = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = line.strip().split()
            direction = clean[0]
            distance = int(clean[1])
            tuple_list.append((direction, distance))
    return tuple_list


movement_style = {
    1: {
        'up': lambda current, magnitude: (current[0] - magnitude, current[1]),
        'down': lambda current, magnitude: (current[0] + magnitude, current[1]),
        'forward': lambda current, magnitude: (current[0], current[1] + magnitude),
    },
    2: {
        'down': lambda current, magnitude: (current[0], current[1], current[2] + magnitude),
        'up': lambda current, magnitude: (current[0], current[1], current[2] - magnitude),
        'forward': lambda current, magnitude: (current[0] + magnitude * current[2], current[1] + magnitude, current[2]),
    },
}


def execute(file_name, part_number):
    current_position = 0, 0, 0  # depth, horizontal, aim
    movement_strategy = movement_style[part_number]
    data = convert_file_to_tuple_list(file_name)
    for direction, distance in data:
        current_position = movement_strategy[direction](current_position, distance)
    return current_position[0] * current_position[1]


class TestThing(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print(f'\nExecuting {cls.__name__}')

    def setUp(self) -> None:
        self.current_result = False
        print(f'\t Running {self._testMethodName}', end='\n\t\t')

    def assertion(self, test_passes) -> None:
        self.current_result = test_passes
        assert test_passes

    def tearDown(self) -> None:
        test_result = 'PASS' if self.current_result else 'FAIL'
        self.current_result = False
        print('\t\t' + test_result)

    def test_one_example(self):
        result = execute('example.txt', 1)
        self.assertion(result == 150)

    def test_one_data(self):
        result = execute('data.txt', 1)
        self.assertion(1714950 == result)

    def test_two_example(self):
        result = execute('example.txt', 2)
        self.assertion(900 == result)

    def test_two_data(self):
        result = execute('data.txt', 2)
        self.assertion(1281977850 == result)
