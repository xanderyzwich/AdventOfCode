"""
Day 2: Password Philosophy
"""
from unittest import TestCase
import re


def validate_passwords(file_name, validator):
    """
    Read in data from file
    count the number of passwords that are valide per rule specified.
    the format '[min]-[max] [letter]: [pw string]'
    so that [letter] must exist in [pw string] at least [min] times or at most [max] times
    :param file_name: string of file name to be read
    :return: count of valid passwords
    """
    # validator = is_valid_part1 if part1 else is_valid_part2
    with open(file_name, 'r') as file_in:
        return sum([1 for line in file_in if validator(*re.split(r'[-:\s]+', line.replace('\n', '')))])


def is_valid_part1(_min, _max, letter, pw):
    """
    Return true if the pw is valid and contains letter between _min and _max number of times
    """
    count = sum([1 for s in pw if s == letter])
    return int(_min) <= count <= int(_max)


def is_valid_part2(_min, _max, letter, pw):
    """
    Return true if the pw is valid
    and contains letter in a position _min OR _max
    """
    section = (pw[int(x)-1] for x in (_min, _max))
    return 1 == sum([1 for s in section if s == letter])


class TestValidatePW(TestCase):
    def test_part1_example(self):
        assert validate_passwords('example.txt', is_valid_part1) == 2

    def test_part1(self):
        count = validate_passwords('part1.txt', is_valid_part1)
        # print(count)
        assert count == 524

    def test_part2_example(self):
        assert validate_passwords('example.txt', is_valid_part2) == 1

    def test_part2(self):
        count = validate_passwords('part1.txt', is_valid_part2)
        # print(count)
        assert count == 485
