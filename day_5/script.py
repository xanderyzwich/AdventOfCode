"""
Day 5: Binary Boarding
"""
from unittest import TestCase


def decode_placement(input_str):
    row = int(input_str[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(input_str[7:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col


def max_id(file_name):
    with open(file_name, 'r') as input_file:
        return max(decode_placement(x) for x in input_file)


def find_missing(file_name):
    maximum_id = 127 * 8 + 7
    empty_seats = list(range(maximum_id))
    with open(file_name, 'r') as input_file:
        [empty_seats.remove(decode_placement(line)) for line in input_file]
    left, right = 1, len(empty_seats)-2
    while empty_seats[left+1] - empty_seats[left] == 1:
        left += 1
    while empty_seats[right] - empty_seats[right-1] == 1:
        right -= 1
    return empty_seats[left+1]

class TestThing(TestCase):

    def test_one_example(self):
        assert decode_placement('FBFBBFFRLR') == 357
        assert max_id('example.txt') == 820

    def test_one_data(self):
        assert max_id('data.txt') == 885

    def test_two_example(self):
        assert True

    def test_two_data(self):
        assert find_missing('data.txt') == 623

