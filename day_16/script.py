"""
Day 16: Ticket Translation
"""
import re
from unittest import TestCase


class TicketCheck:

    def __init__(self):
        self.rules = []

    def add_rule(self, rule_str):
        *rule, body = re.split(r':', rule_str)
        parts = re.split(r' or ', body)
        for n in parts:
            start, stop = re.split(r'-', n)
            rule.append(int(start))
            rule.append(int(stop))
        self.rules.append(rule)
        return 0

    def check_ticket(self, ticket_line):
        ticket = re.split(r'[,]', ticket_line)
        for v in ticket:
            value = int(v)
            valid = False
            for rule in self.rules:
                first = rule[1] <= value <= rule[2]
                second = rule[3] <= value <= rule[4]
                if first or second:
                    valid = True
                    break
            if not valid:
                return value
        return 0

    def __contains__(self, item):
        for r in self.rules:
            if r[0] == item:
                return True
        return False

    def analyze_ticket(self, ticket_line):
        ticket = re.split(r'[,]', ticket_line)
        possibilites = []
        for v in ticket:
            possible = []
            value = int(v)
            valid = False
            for rule in self.rules:
                first = rule[1] <= value <= rule[2]
                second = rule[3] <= value <= rule[4]
                if first or second:
                    possible.append(rule[0])
            if len(possible) > 0:
                possibilites.append(possible)
        if len(ticket) == len(possibilites):
            return possibilites
        else:
            return []


def process(file_name, part=1):
    tc = TicketCheck()
    error_rate = 0
    field_names = []
    my_ticket = ''
    with open(file_name, 'r') as input_file:
        section = 0
        for l in input_file:
            line = l.rstrip()
            if re.match(r'(your ticket)', line):
                section = 1
            elif re.match(r'(nearby tickets)', line):
                section = 2
            elif re.match(r'[A-Za-z]+', line):
                tc.add_rule(line.rstrip())
            elif re.match(r'[0-9]', line):
                if section == 2 and part == 1:
                    error_rate += tc.check_ticket(line)
                elif section == 2 and part == 2:
                    ticket_possibilities = tc.analyze_ticket(line)
                    if len(ticket_possibilities) == 0:
                        continue
                    elif len(field_names) == 0:
                        field_names = ticket_possibilities
                    else:
                        overlap = find_overlap(field_names, ticket_possibilities)
                        field_names = overlap
                if section == 1:
                    my_ticket = map(int, re.split(r',', line))
    if part == 1:
        print(error_rate)
        return error_rate

    # Cleanup duplicate names
    finished_fields = []
    while len(finished_fields) != len(field_names):
        for i, field in enumerate(field_names):
            if field in finished_fields:
                continue
            if len(field) == 1:
                for j, f in enumerate(field_names):
                    if f == field or type(field_names[j]).__name__ == 'str':
                        continue
                    field_names[j].remove(field[0])
                field_names[i] = field[0]
                finished_fields.append(field[0])
    del finished_fields

    my_clean_ticket = {}
    for x, y in zip(field_names, my_ticket):
        print(f'{x}: {y}')
        my_clean_ticket[x] = y
    del my_ticket

    product = 1
    for k in my_clean_ticket:
        product *= my_clean_ticket[k] if k.startswith('departure') else 1
    print(product)
    return product


def find_overlap(field_names, ticket_possibilities):
    result = []
    for i, possible_fields in enumerate(field_names):
        piece = []
        for possible in possible_fields:
            if possible in ticket_possibilities[i]:
                piece.append(possible)
        result.append(piece)
    return result


class TestThing(TestCase):

    def test_one_example(self):
        assert process('example.txt') == 71

    def test_one_data(self):
        assert process('data.txt')

    def test_two_example(self):
        assert process('example.txt', part=2) == 1

    def test_two_data(self):
        assert process('data.txt', part=2)
