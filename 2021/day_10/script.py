"""
Day 10: Syntax Scoring
"""
from math import ceil
from unittest import TestCase


class ParenStack:
    opens = '([{<'
    closes = ')]}>'

    def __init__(self):
        self.stack = list()
        self.forward_pairs = {self.opens[i]: self.closes[i] for i in range(len(self.opens))}
        self.reverse_pairs = {v: k for k, v in self.forward_pairs.items()}

    def push(self, element):
        is_close, is_open = element in self.closes, element in self.opens
        if not any([is_open, is_close]):
            raise ValueError(f'Element "{element}" is not a supported character')
        if is_close:
            not_match = self.reverse_pairs[element] != self.stack[-1]
            if not_match:
                return False
            self.stack.pop()
        else:
            self.stack.append(element)
        return True

    def pop(self):
        return self.stack.pop()

    def autocomplete(self):
        result = ''
        while self.stack:
            result += self.forward_pairs[self.stack.pop()]
        return result

    @classmethod
    def error_score(cls, record):
        scores = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137,
        }
        stack = ParenStack()
        for element in record:
            is_valid = stack.push(element)
            if not is_valid:
                return scores[element]
        return 0

    @classmethod
    def autocomplete_score(cls, record):
        scores = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4,
        }
        stack = ParenStack()
        if 0 != ParenStack.error_score(record):
            return 0
        for element in record:
            stack.push(element)
        completion = stack.autocomplete()
        score = 0
        for x in completion:
            score = 5 * score + scores[x]
        return score


def parse_file(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = list(line.strip())
            data.append(clean)
    return data


def total_error_score(file_data):
    return sum([ParenStack.error_score(r) for r in file_data])


def middle_autocomplete_score(file_data):
    scores = [ParenStack.autocomplete_score(r) for r in file_data]  # get scores
    scores = [s for s in sorted(scores) if s > 0]  # filter out zeroes and sort
    middle_index = ceil(len(scores) / 2) - 1
    return scores[middle_index]


class TestThing(TestCase):
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
        score = total_error_score(self.example_data)
        self.assertion(26397 == score)

    def test_one_data(self):
        score = total_error_score(self.input_data)
        self.assertion(321237 == score)

    def test_two_example(self):
        score = middle_autocomplete_score(self.example_data)
        self.assertion(288957 == score)

    def test_two_data(self):
        score = middle_autocomplete_score(self.input_data)
        self.assertion(2360030859 == score)
