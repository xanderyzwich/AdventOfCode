"""
Day 14: Extended Polymerization
"""
import copy
from unittest import TestCase


def convert_data(template):
    # Split into letter pairs
    pairs = []
    for i in range(len(template)-1):
        curren_pair = template[i:i + 2]
        pairs.append(curren_pair)

    # each unique pair
    unique_pairs = set(pairs)
    return {up: pairs.count(up) for up in unique_pairs}


def convert_rules(rules):
    pair_rules = {}
    for pair, result in rules.items():
        pair_rules[pair] = [pair[0]+result, result+pair[1]]
    return pair_rules


def parse_file(file_name):
    polymer_template, rules = '', {}
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = line.strip()
            if 0 < len(clean):
                if ' -> ' in line:
                    pair, result = clean.split(' -> ')
                    rules[pair] = result
                else:
                    polymer_template = clean
    return convert_data(polymer_template), convert_rules(rules), polymer_template[0]


def apply_rules(count_data, rules, steps=1):
    current_data = copy.deepcopy(count_data)
    for _ in range(steps):
        temp_data = {}
        for key, count in current_data.items():
            rule_pairs = rules[key]
            for rp in rule_pairs:
                if rp in temp_data:
                    temp_data[rp] += count
                else:
                    temp_data[rp] = count
        current_data = temp_data
    return current_data


def get_result(count_data, first_letter):
    letter_counts = {first_letter: 1}
    for k, v in count_data.items():
        if k[1] not in letter_counts:
            letter_counts[k[1]] = v
        else:
            letter_counts[k[1]] += v
    frequencies = list(letter_counts.values())
    frequencies.sort(reverse=True)
    return frequencies[0]-frequencies[-1]


def part1(data, rules, first_letter):
    final_data = apply_rules(data, rules, steps=10)
    return get_result(final_data, first_letter)


def part2(data, rules, first_letter):
    final_data = apply_rules(data, rules, steps=40)
    return get_result(final_data, first_letter)


class TestPolymerization(TestCase):
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

    def test_one_example(self):
        result = part1(*self.example_data)
        self.assertion(1588 == result)

    def test_one_data(self):
        result = part1(*self.input_data)
        self.assertion(2797 == result)

    def test_two_example(self):
        result = part2(*self.example_data)
        self.assertion(2188189693529 == result)

    def test_two_data(self):
        result = part2(*self.input_data)
        self.assertion(2926813379532 == result)
