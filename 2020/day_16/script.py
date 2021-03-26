"""
Day 16: Ticket Translation
"""
import re
from unittest import TestCase


class TicketCheck:

    def __init__(self):
        self.rules = []

    def add_rule(self, rule_str):
        """
        Parse and append rule from text string
        :param rule_str: text string of a given rule
        :return: None
        """
        *rule, body = re.split(r':', rule_str)
        parts = re.split(r' or ', body)
        for n in parts:
            start, stop = re.split(r'-', n)
            rule.append(int(start))
            rule.append(int(stop))
        self.rules.append(rule)
        return 0

    def check_ticket(self, ticket_line):
        """
        Check that each value falls within a rule's range
        :param ticket_line: text info for a ticket
        :return: invalid value or zero if ticket is valid
        """
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

    def analyze_ticket(self, ticket_line):
        """
        :param ticket_line: text data for a given ticket
        :return: list of rule names fitting each position
        """
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
    """
    This does the heavy lifting
    :param file_name: name of file containing puzzle input
    :param part: puzzle part beign solved in [1, 2]
    :return: puzzle solution
    """
    tc = TicketCheck()
    error_rate = 0
    field_names = []
    my_ticket = ''
    with open(file_name, 'r') as input_file:
        section = 0
        for l in input_file:
            line = l.rstrip()
            if section == 0:
                if re.match(r'(your ticket)', line):  # process your ticket
                    section = 1
                elif re.match(r'[A-Za-z]+', line):  # is rule
                    tc.add_rule(line.rstrip())
            elif section == 1:
                if re.match(r'(nearby tickets)', line):  # begin processing nearby tickets
                    section = 2
                elif re.match(r'[0-9]', line):
                    my_ticket = map(int, re.split(r',', line))
            elif section == 2 and re.match(r'[0-9]', line):  # process ticket
                if part == 1:
                    error_rate += tc.check_ticket(line)
                elif part == 2:
                    field_names = update_fields(field_names, tc.analyze_ticket(line))
    if part == 1:
        print(error_rate)
        return error_rate

    field_names = deduplicate_fields(field_names)
    my_ticket = translate_ticket(field_names, my_ticket)

    product = 1
    for k in my_ticket:
        product *= my_ticket[k] if k.startswith('departure') else 1
    print(product)
    return product


def update_fields(field_names, ticket_possibilities):
    """
    Return possible names overlapping between lists passed
    if field_names is empty return ticket_possibilities
    :param field_names: 2d list of possible names for each field
    :param ticket_possibilities: 2d list of possible names for each field based on one ticket
    :return: list of names possible for each field present in both input lists
    """
    if not ticket_possibilities:
        return field_names
    if field_names:
        return find_overlap(field_names, ticket_possibilities)
    return ticket_possibilities


def deduplicate_fields(field_names):
    """
    The possible names of the fields contain many duplicates
    :param field_names: 2d list of possible names for each field
    :return: 1d list of names for each field
    """
    cleaned_fields = field_names
    finished_fields = []
    while len(finished_fields) != len(cleaned_fields):  # Continue as long as fields need to be cleaned
        for i, field in enumerate(cleaned_fields):
            if len(field) == 1 and field not in finished_fields:
                for j, f in enumerate(cleaned_fields):
                    not_self = f != field
                    not_string = type(f).__name__ != 'str'
                    not_single = len(cleaned_fields[j]) != 1
                    need_to_remove = not_self and not_string and not_single
                    if need_to_remove:
                        cleaned_fields[j].remove(field[0])
                cleaned_fields[i] = field[0]
                finished_fields.append(field[0])
    return cleaned_fields


def translate_ticket(field_names, my_ticket):
    """
    Apply names to fields in the given ticket
    :param field_names: deduplicated list of fields
    :param my_ticket: values for each field
    :return: dict of [field name]: [value]
    """
    from rich.console import Console
    from rich.table import Table
    console = Console()
    table = Table(show_header=True, header_style="green")
    table.add_column("field")
    table.add_column("value")

    my_clean_ticket = {}
    for x, y in zip(field_names, my_ticket):
        table.add_row(x, str(y))
        # print(f'{x}: {y}')
        my_clean_ticket[x] = y
    console.print(table)
    return my_clean_ticket


def find_overlap(field_names, ticket_possibilities):
    """
    For each position in the list return values existing in both inputs
    :param field_names: 2d list of possibilities for each position
    :param ticket_possibilities: 2d list of possibilities for each position based on single ticket info
    :return: 2d list of overlapping values in each position
    """
    result = []
    for i, possible_fields in enumerate(field_names):
        piece = []
        for possible in possible_fields:
            if possible in ticket_possibilities[i]:
                piece.append(possible)
        result.append(piece)
    return result


class TestThing(TestCase):

    def setUp(self) -> None:
        print(f'\n--- Running test: {self._testMethodName} ---')

    def test_one_example(self):
        assert process('example.txt') == 71

    def test_one_data(self):
        assert process('data.txt')

    def test_two_example(self):
        assert process('example.txt', part=2) == 1

    def test_two_data(self):
        assert process('data.txt', part=2)
