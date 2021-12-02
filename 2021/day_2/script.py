"""
Day 2: Dive!
"""
from functools import reduce
from unittest import TestCase
from operator import mul


def convert_file_to_tuple_list(file_name):
    tuple_list = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = line.strip().split()
            direction = clean[0]
            distance = int(clean[1])
            tuple_list.append((direction, distance))
    return tuple_list


def product(info):
    return reduce(mul, info, 1)


def travel(directions):
    current_position = 0, 0
    movement = {
        'up': lambda current, magnitude: (current[0] - magnitude, current[1]),
        'down': lambda current, magnitude: (current[0] + magnitude, current[1]),
        'forward': lambda current, magnitude: (current[0], current[1] + magnitude),
    }
    for direction, distance in directions:
        current_position = movement[direction](current_position, distance)
    return current_position


def part1(file_name):
    data = convert_file_to_tuple_list(file_name)
    destination = travel(data)
    return product(destination)


def travel_with_aim(directions):
    current_position = 0, 0, 0  # depth, horizontal, aim
    movement = {
        'down': lambda current, magnitude: (current[0], current[1], current[2]+magnitude),
        'up': lambda current, magnitude: (current[0], current[1], current[2]-magnitude),
        'forward': lambda current, magnitude: (current[0]+magnitude*current[2], current[1] + magnitude, current[2]),
    }
    for direction, distance in directions:
        current_position = movement[direction](current_position, distance)
    return current_position


def part2(file_name):
    data = convert_file_to_tuple_list(file_name)
    destination = travel_with_aim(data)
    print(destination)
    return product(destination[:2])


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
        result = part1('example.txt')
        self.assertion(result == 150)

    def test_one_data(self):
        result = part1('data.txt')
        self.assertion(1714950 == result)

    def test_two_example(self):
        result = part2('example.txt')
        self.assertion(900 == result)

    def test_two_data(self):
        result = part2('data.txt')
        self.assertion(1281977850 == result)
