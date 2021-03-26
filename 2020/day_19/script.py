"""
Day X: Name
"""
import re
from unittest import TestCase


class RegexEngine:

    def __init__(self, rule_str_arr):
        self.rules = {}
        self.add_rules(rule_str_arr)

    def build_regex(self, input_str):
        # print(f'Building Regex: {input_str}')
        if re.match(r'[0-9]+: [a-zA-Z]+', input_str):
            to_match = re.findall(r'([a-zA-Z]+)', input_str)[0]
            return f'{to_match}'

    def add_rules(self, rule_str_arr):
        # print(f'Adding rules {rule_str_arr}')
        complex_rules = {}
        for string in rule_str_arr:
            # print('adding rule', string)
            id, val = re.split(r':', string)
            if re.match(r'^[0-9]+: [a-zA-Z]+', string):
                temp_regex = f'({self.build_regex(string)})'
                self.rules[int(id)] = temp_regex
                # print(id, temp_regex)
            else:
                complex_rules[int(id)] = val
        print(self)
        print('complex rules:', complex_rules)
        self.build_nested_regex(complex_rules)

    def build_nested_regex(self, complex_rules):
        complicated = complex_rules
        while len(complicated) != 0:
            # print(complicated)
            keys_to_remove = []
            for k, v in complicated.items():
                nested_regex = ''
                depends_on = list(map(int, set(re.findall('[0-9]+', v))))
                print('I need:', depends_on)
                if all([x in self.rules for x in depends_on if x != ' ']):
                    print(f'I can make {k, v}')
                    csv = v.replace(' ', ',')
                    for d in depends_on:
                        csv = csv.replace(str(d), f'({self.rules[d]})')
                    nested_regex = csv.replace(',', '')
                else:
                    print(f'couldn\'t build {k}: {v}')
                    continue
                # print(f'Adding {k}: "{nested_regex}"')
                self.rules[k] = f'({nested_regex})'
                keys_to_remove.append(k)
            for k in keys_to_remove:
                del complicated[k]
        # print('Nested Regex Built')
        # print(self)

    def matches(self, message, rule_number):
        return True if re.match(r'^' + self.rules[rule_number] + '$', message) else False

    def count_zero_matches(self, message_arr):
        return sum([1 for m in message_arr if self.matches(m, 0)])

    def __str__(self):
        temp = 'Regular Expression Engine\n'
        for k, v in self.rules.items():
            temp += f'{k}: "{v}"\n'
        return temp



def read(file_name):
    rules, messages = [], []
    with open(file_name, 'r') as input_file:
        for l in input_file:
            line = l.rstrip()
            if re.match(r'^[0-9]+(: ).*.$', l):  # is a rule
                # rule = line.replace(r': ', ':').replace(' | ', '|').replace(r' ', '.').replace('"', '')
                rule = line.replace('"', '')
                rules.append(rule)
            elif re.match(r'^[a-zA-Z]+$', l):
                messages.append(line)
    print(rules, messages)
    return rules, messages


def part1(file_name):
    rules, messages = read(file_name)
    regex_engine = RegexEngine(rules)
    print(regex_engine.rules[0])
    result = regex_engine.count_zero_matches(messages)
    print(f'Part1 for {file_name} result: {result}')
    return result


class TestThing(TestCase):

    def setUp(self) -> None:
        print(f'\n--- Running test: {self._testMethodName} ---')

    def test_one_dev(self):
        rules, messages = read('example.txt')
        regex_engine = RegexEngine(rules)
        print(regex_engine)
        # for m in messages:
        #     print(m, regex_engine.matches(m, 0))
        assert regex_engine.count_zero_matches(messages) == 2


    def test_one_example(self):
        assert part1('example.txt') == 2

    def test_one_data(self):
        assert part1('data.txt') > 155

    def test_two_example(self):
        assert True

    def test_two_data(self):
        assert True
