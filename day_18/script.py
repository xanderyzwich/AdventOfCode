"""
Day X: Name
"""
import re
from unittest import TestCase

func = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}


def evaluate_pure(elements):
    i, accumulator = 1, int(elements[0])
    while i < len(elements):
        op, next = elements[i: i+2]
        temp = func[op](accumulator, int(next))
        # print(f'{accumulator} {op} {next} = {temp}')
        accumulator = temp
        i += 2
    return accumulator


def evaluate_parens(elements):
    count, _close = 0, len(elements)
    _open = elements.index('(')
    updated_elements = elements[:_open]  # elements before paren
    for i in range(_open, len(elements)):  # lets find the closing peren
        if elements[i] == '(':
            count += 1
        elif elements[i] == ')':
            count -= 1
            if count == 0:
                _close = i + 1
                break
    priority = evaluate(elements[_open+1:_close-1])  # omit the outer-most perens
    # print(f'{elements[_open+1:_close-1]} = {priority}')
    updated_elements.append(priority)
    updated_elements.extend(elements[_close:])
    return evaluate(updated_elements)


def evaluate(elements):
    # print(elements)
    if '(' in elements:  # Assuming all parens are matched
        return evaluate_parens(elements)
    else:
        return evaluate_pure(elements)


def solve(expression_str):
    fixed = expression_str.replace('(', '( ').replace(')', ' )')
    elements = fixed.split()
    # print(expression_str, fixed, elements)
    return evaluate(elements)


def do_homework(file_name):
    _sum = 0
    print("Doing Homework:", file_name)
    with open(file_name, 'r') as homework:
        for question in homework:
            _sum += solve(question)
    print(_sum)
    return _sum


class TestThing(TestCase):

    def setUp(self) -> None:
        print(f'\n--- Running test: {self._testMethodName} ---')

    def test_one_example(self):
        tests = [
            {'arg': '1 + 2 * 3 + 4 * 5 + 6', 'want': 71},
            {'arg': '1 + (2 * 3) + (4 * (5 + 6))', 'want': 51},
            {'arg': '2 * 3 + (4 * 5)', 'want': 26},
            {'arg': '5 + (8 * 3 + 9 + 3 * 4 * 3)', 'want': 437},
            {'arg': '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 'want': 12240},
            {'arg': '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 'want': 13632}
        ]
        for t in tests:
            print(f'Testing {t}', end=' - ')
            assert solve(t['arg']) == t['want']
            print('PASS')

    def test_one_data(self):
        do_homework('assignment.txt')

    def test_two_example(self):
        assert True

    def test_two_data(self):
        assert True
