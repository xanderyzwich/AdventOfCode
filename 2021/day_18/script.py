"""
Day 18: Snailfish
"""
import functools
import re
from copy import deepcopy
from math import floor, ceil
from unittest import TestCase


def add(previous, next):
    return f'[{previous},{next}]'


def reduce(snailfish_number):
    current_number = deepcopy(snailfish_number)
    while should_reduce(current_number):
        while should_explode(current_number):
            current_number = explode(current_number)
        if should_split(current_number):
            current_number = split(current_number)
    return current_number


def explode(snailfish_number):
    current_number = deepcopy(snailfish_number)

    open_count = 0
    # find deepest pair
    for i, char in enumerate(current_number):
        if '[' == char:
            open_count += 1
        if ']' == char:
            if open_count >= 4:
                open_index = current_number[:i].rindex('[')
                pair_left, pair_right = (int(x) for x in current_number[open_index + 1: i].split(','))
                print(pair_left, pair_right)

                left_side, right_side = current_number[:open_index], current_number[i+1:]
                if contains_digit(left_side):
                    # handle left
                    pass
                else:
                    new_left = 0
                    pass
                if contains_digit(right_side):
                    # handle right
                    pass
                print(f'left:"{left_side}", right:"{right_side}"')
    return current_number


def contains_digit(string):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for d in digits:
        if d in string:
            return True
    return False


def should_explode(snailfish_number):
    return 4 <= max_depth(snailfish_number)


def should_split(snailfish_number):
    return any([n >= 10 for n in values(snailfish_number)])


def values(snailfish_number):
    return map(int, re.findall(r'[0-9]+', snailfish_number))


def should_reduce(snailfish_number):
    return any([should_explode(snailfish_number), should_split(snailfish_number)])


def max_depth(snailfish_number):
    unclosed_opens, max_opens = 0, 0
    for char in snailfish_number:
        if '[' == char:
            unclosed_opens += 1
            max_opens = max([unclosed_opens, max_opens])
        if ']' == char:
            unclosed_opens -= 1
    return max_opens


def split(snailfish_number):
    for val in values(snailfish_number):
        if val > 10:
            index, length = snailfish_number.index(val), len(str(val))
            left, right = floor(val / 2), ceil(val / 2)
            split_part = f'[{left},{right}]'
            return snailfish_number[:index] + split_part + snailfish_number[index + length:]


def parse_file(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = line.strip()
            data.append(clean)
    return data


class TestThing(TestCase):
    example_data = parse_file('example.txt')
    input_data = parse_file('input.txt')

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

    def test_split(self):
        self.assertion((5, 5) == split(10))
        self.assertion((5, 6) == split(11))
        self.assertion((6, 6) == split(12))

    def test_add(self):
        self.assertion('[[1,2],[[3,4],5]]' == add('[1,2]', '[[3,4],5]'))
        self.assertion('[[1,1],[2,2]]' == add('[1,1]', '[2,2]'))

    def test_max_depth(self):
        self.assertion(5 == max_depth('[[[[[9,8],1],2],3],4]'))

    def test_shoulds(self):
        explodable = '[[[[[9,8],1],2],3],4]'
        self.assertion(True is should_explode(explodable))
        self.assertion(True is should_reduce(explodable))
        splitable = '[0,10]'
        self.assertion(True is should_split(splitable))
        self.assertion(True is should_reduce(splitable))

    def test_explode(self):
        explodable = '[[[[[9,8],1],2],3],4]'
        explode(explodable)

    def test_one_example(self):
        self.assertion(True)

    def test_one_data(self):
        self.assertion(True)

    def test_two_example(self):
        self.assertion(True)

    def test_two_data(self):
        self.assertion(True)
