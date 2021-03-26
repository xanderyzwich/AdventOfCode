"""
Day 9: Encoding Error
"""
from unittest import TestCase


def validate(previous_set, object):
    for i in previous_set:
        other = object - i
        if (other != i) and other in previous_set:
            return True
    return False


def process_set(input_list, preamble_size=25):
    previous_set, i = input_list[:preamble_size], preamble_size
    while len(previous_set) == preamble_size:
        current_element = input_list[i]
        if validate(previous_set, current_element):
            del previous_set[0]
            previous_set.append(current_element)
            i += 1
        else:
            return current_element


def process_file_part1(file_name, preamble_size=25):
    with open(file_name, 'r') as input_file:
        input_data = [int(x) for x in input_file]
        result = process_set(input_data, preamble_size)
        print(result)
        return result


def process_file_part2(file_name, preamble_size=25):
    input_data, invalid_number = [], -1
    with open(file_name, 'r') as input_file:
        input_data = [int(x) for x in input_file]
    invalid_number = process_set(input_data, preamble_size)
    i = 0
    while i < len(input_data) - 1:
        j = i+1
        while j < len(input_data):
            trial_set = input_data[i:j]
            if invalid_number == sum(trial_set):
                trial_sum = min(trial_set) + max(trial_set)
                print(trial_set[0] + trial_set[-1], trial_sum)
                return trial_sum
            j += 1
        i += 1
    print('sumthin dun goofed')




class TestThing(TestCase):

    def test_validate(self):
        example_preamble = list(range(1, 26))
        assert validate(example_preamble, 26)
        assert validate(example_preamble, 24)
        assert not validate(example_preamble, 100)
        assert not validate(example_preamble, 50)

        example_preamble.remove(20)
        example_preamble.append(45)
        assert validate(example_preamble, 26)
        assert not validate(example_preamble, 65)
        assert validate(example_preamble, 64)
        assert validate(example_preamble, 66)

    def test_one_example(self):
        assert process_file_part1('example.txt', 5) == 127

    def test_one_data(self):
        assert process_file_part1('data.txt') == 104054607

    def test_two_example(self):
        assert process_file_part2('example.txt', 5) == 62

    def test_two_data(self):
        assert process_file_part2('data.txt')
