"""
Day 5: Binary Boarding
"""
from unittest import TestCase

coding = {
    'F': '0',
    'B': '1',
    'L': '0',
    'R': '1'
}


def decode_placement(input_str):
    return int(''.join([coding[c] for c in input_str.rstrip('\n')]), 2)


def max_id(file_name):
    with open(file_name, 'r') as input_file:
        return max(decode_placement(x) for x in input_file)


def find_missing(file_name):
    filled_seats = []
    with open(file_name, 'r') as input_file:
        [filled_seats.append(decode_placement(line)) for line in input_file]
    filled_seats.sort()
    for seat in filled_seats:
        if seat+1 not in filled_seats:
            return seat+1

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

