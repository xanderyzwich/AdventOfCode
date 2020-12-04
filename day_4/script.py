"""
--- Day 4: Passport Processing ---
"""
from unittest import TestCase
import re

required_fields = {
    'byr': (lambda v: 4 == len(str(v)) and (1920 <= int(v) <= 2002)),  # birth year
    'iyr': (lambda v: 4 == len(str(v)) and (2010 <= int(v) <= 2020)),  # 'issue year',
    'eyr': (lambda v: 4 == len(str(v)) and (2020 <= int(v) <= 2030)),  # 'expiration year',
    'hgt': (lambda v: (150 <= int(v[:-2]) <= 193) if 'cm' == v[-2:] else (59 <= int(v[:-2]) <= 76) if 'in' == v[-2:] else False),  # 'height',
    'hcl': (lambda v: v[0] == '#' and re.match(r'#[A-Fa-f0-9]{6}', v)),  # 'hair color',
    'ecl': (lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),  # 'eye color',
    # 'cid': (lambda v: True),  # 'country id',
    'pid': (lambda v: 9 == len(v))  # 'passport id'
}


def validate(passport):
    """
    :param passport: data to be validated
    :return: True if valid, False otherwise
    """
    for key in required_fields.keys():
        if key not in passport.keys(): # and key != 'cid':
            # print(f'Missing value "{key}" in passport: {passport}')
            return False
    return True


def validate_better(passport):
    for key in required_fields.keys():
        if key not in passport.keys() or not validate_rule(key, passport[key]):
            # print(f'INVALID or MISSING value "{key}" in passport: {passport}')
            return False
    return True


def validate_rule(key, value):
    return required_fields[key](value)


def convert(input_str):
    passport = {}
    for token in re.split(r'\s', input_str):
        # print('  ', token)
        if ':' in token:
            k, v = re.split(':', token)
            passport[k] = v
    return passport


def process(file_name, is_valid=validate):
    """
    Read in the file and validate each passport
    :param is_valid: validation function to be used
    :param file_name:
    :return:
    """
    with open(file_name, 'r') as input_file:
        one_line, valid_count = '', 0
        for line in input_file:
            if ':' in line:
                one_line += line.replace('\n', ' ')
            else:
                passport = convert(one_line)
                valid_count += 1 if is_valid(passport) else 0
                one_line = ''
        return valid_count


class TestThing(TestCase):

    def test_one_example(self):
        assert process('example.txt') == 2

    def test_one_data(self):
        assert process('data.txt') == 264

    def test_two_example_entries(self):
        assert validate_rule('byr', 2002)
        assert not validate_rule('byr', 2003)

        assert validate_rule('hgt', '60in')
        assert validate_rule('hgt', '190cm')
        assert not validate_rule('hgt', '190in')
        assert not validate_rule('hgt', '190')

        assert validate_rule('hcl', '#123abc')
        assert not validate_rule('hcl', '#123abz')
        assert not validate_rule('hcl', '123abc')

        assert validate_rule('ecl', 'brn')
        assert not validate_rule('ecl', 'wat')

        assert validate_rule('pid', '000000001')
        assert not validate_rule('pid', '0123456789')

    def test_two_example_invalid(self):
        assert process('pt2_invalid.txt', validate_better) == 0

    def test_two_example_valid(self):
        assert process('pt2_valid.txt', validate_better) == 4

    def test_two_data(self):
        assert process('data.txt', validate_better) == 224
