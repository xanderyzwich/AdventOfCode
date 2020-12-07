"""
Day 7: Handy Haversacks
"""
import json
import pprint
import re
from unittest import TestCase


def parse_rules(file_name):
    rules = {}
    with open(file_name, 'r') as file_in:
        for line in file_in:
            cleaned = line.replace(r'bags', '').replace(r'bag', '').replace(r'\.', '').replace(r'\n', '')
            bag, *contents = re.split(r' contain |, ', cleaned)
            thing = {}
            for bit in contents:
                count, *color = re.split(r'\W', bit)
                color = ' '.join(color)
                if count != 'no':
                    thing[color.rstrip()] = int(count)
            rules[bag.rstrip()] = thing
    # print(json.dumps(rules, sort_keys=True, indent=4))
    return rules


def contained_by(rules, color):
    """How many bags could contain a {color} bag (itself a bag recursively inside)"""
    containers = [color]  # This will be subtracted at the end
    updated = True
    while updated:
        updated = False
        for bag in rules:
            for content in rules[bag]:
                if content in containers and bag not in containers:
                    print(f'Appending: {bag} that contains {content}')
                    containers.append(bag)
                    updated = True
    # print(len(containers) - 1)
    return len(containers) - 1


def must_contain(rules, color):
    contents = rules[color].items()
    if len(contents) == 0:
        return 0

    count = 0
    for k, v in contents:
        count += v * (must_contain(rules, k) + 1)
    # print(f'MUST_CONTAIN returning {color} -> {count}')
    return count


class TestThing(TestCase):

    def test_one_example(self):
        assert contained_by(parse_rules('example-part1.txt'), 'shiny gold') == 4

    def test_one_data(self):
        assert contained_by(parse_rules('data.txt'), 'shiny gold') == 300

    def test_two_example(self):
        assert must_contain(parse_rules('example-part1.txt'), 'shiny gold') == 32
        assert must_contain(parse_rules('example-part2.txt'), 'shiny gold') == 126

    def test_two_data(self):
        assert must_contain(parse_rules('data.txt'), 'shiny gold') == 8030
