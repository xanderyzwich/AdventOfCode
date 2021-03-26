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


def evaluate_advanced(elements):
    working_set = perform('+', elements)
    return int(perform('*', working_set))
                

def perform(operator, elements):
    i, working_set = 1, elements
    # print(f'Perfoming {operator} on {working_set}')
    while operator in working_set:
        # print(working_set)
        if working_set[i] == operator:
            left, right = int(working_set[i - 1]), int(working_set[i + 1])
            result = func[operator](left, right)
            # print(f'{left} {operator} {right} = {result}')
            working_set = [*working_set[:i - 1], str(result), *working_set[i + 2:]]
        else:
            i += 1
    # print(f'Completed {operator} on {working_set}')
    if len(working_set) == 1:
        return working_set[0]
    return working_set


def evaluate_parens(elements, advanced):
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
    priority = evaluate(elements[_open+1:_close-1], advanced)  # omit the outer-most perens
    # print(f'{elements[_open+1:_close-1]} = {priority}')
    updated_elements.append(priority)
    updated_elements.extend(elements[_close:])
    return evaluate(updated_elements, advanced)


def evaluate(elements, advanced):
    base = evaluate_advanced if advanced else evaluate_pure
    # print(elements)
    if '(' in elements:  # Assuming all parens are matched
        return evaluate_parens(elements, advanced)
    else:
        return base(elements)


def solve(expression_str, advanced=False):
    fixed = expression_str.replace('(', '( ').replace(')', ' )')
    elements = fixed.split()
    # print(expression_str, fixed, elements)
    return evaluate(elements, advanced)


def do_homework(file_name, advanced=False):
    _sum = 0
    print(f'Doing {"advanced" if advanced else ""} Homework: {file_name}')
    with open(file_name, 'r') as homework:
        for question in homework:
            _sum += solve(question, advanced)
    print(_sum)
    return _sum


class TestThing(TestCase):
    tests = [
        {'arg': '1 + 2 * 3 + 4 * 5 + 6', 'basic': 71, 'advanced': 231},
        {'arg': '1 + (2 * 3) + (4 * (5 + 6))', 'basic': 51, 'advanced': 51},
        {'arg': '2 * 3 + (4 * 5)', 'basic': 26, 'advanced': 46},
        {'arg': '5 + (8 * 3 + 9 + 3 * 4 * 3)', 'basic': 437, 'advanced': 1445},
        {'arg': '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 'basic': 12240, 'advanced': 669060},
        {'arg': '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 'basic': 13632, 'advanced': 23340}
    ]

    def setUp(self) -> None:
        print(f'\n--- Running test: {self._testMethodName} ---')

    def test_one_example(self):
        for t in self.tests:
            print(f'Testing {t} - ')
            result = solve(t['arg'])
            assert result == t['basic']
            print('--- PASS ---')

    def test_one_data(self):
        do_homework('assignment.txt')

    def test_two_example(self):
        for t in self.tests:
            print(f'Testing {t} - ')
            result = solve(t['arg'], advanced=True)
            # print(f'{t["advanced"]} == {result} : {result == t["advanced"]}')
            assert result == t['advanced']
            print('--- PASS--- ')

    def test_two_data(self):
        assert do_homework('assignment.txt', advanced=True)
