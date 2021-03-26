"""
Day 6: Custom Customs
"""
from unittest import TestCase
import re


def process_group_part1(input_str):
    return len(set(input_str.replace('\n', '')))


def process_group_part2(input_str):
    people = re.split('\n', input_str)
    people.remove('')
    all_yes = ''
    for answer in set(input_str.replace('\n', '')):
        if all([answer in person for person in people]):
            all_yes += answer
    return len(all_yes)


def process_file(file_name, check=process_group_part1):
    group, total = '', 0
    with open(file_name, 'r') as input_file:
        for line in input_file:
            if re.match(r'[\w]', line):
                group += line
            else:
                total += check(group)
                # print(total, group)
                group = ''
    return total


class TestThing(TestCase):

    def test_one_example(self):
        assert process_group_part1('abcx\nabcy\nabcz') == 6
        assert process_file('example.txt') == 11

    def test_one_data(self):
        assert process_file('data.txt') == 6596

    def test_two_example(self):
        assert process_file('example.txt', process_group_part2) == 6

    def test_two_data(self):
        assert process_file('data.txt', process_group_part2) == 3219

