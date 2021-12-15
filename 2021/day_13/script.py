"""
Day 13: Transparent Origami
"""
import copy
import re
import sys
from unittest import TestCase


def perform_fold(dots, direction, location):
    new_dots = []
    end = 2*location
    fold_on_y = 'y' == direction
    fold_x, fold_y = (sys.maxsize, location) if fold_on_y else (location, sys.maxsize)
    for x, y in dots:
        # dots will not be on the fold
        new_x = x if x < fold_x else end-x
        new_y = y if y < fold_y else end-y
        new_point = new_x, new_y
        if new_point not in new_dots:
            new_dots.append(new_point)
    return new_dots


def paint_dots(dots):
    max_x, max_y = 0, 0
    for x, y in dots:
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y

    paper = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in dots:
        paper[y][x] = '#'

    print()
    for line in paper:
        print(*line)


def dots_after_one_fold(dots, folds):
    new_dots = perform_fold(dots, *folds[0])
    return len(new_dots)


def paint_after_folding(dots, folds):
    new_dots = copy.deepcopy(dots)
    for fold in folds:
        new_dots = perform_fold(new_dots, *fold)
    paint_dots(new_dots)


def parse_file(file_name):
    dots, folds = [], []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = line.strip()
            if ',' in clean:
                x, y = (int(n) for n in clean.split(','))
                dots.append((x, y))
            elif 'fold along ' in clean:
                direction, location = clean.replace('fold along ', '').split('=')
                location = int(location)
                folds.append((direction, location))
    return dots, folds


class TestOrigami(TestCase):
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
        count = dots_after_one_fold(*self.example_data)
        self.assertion(17 == count)

    def test_one_data(self):
        count = dots_after_one_fold(*self.input_data)
        self.assertion(704 == count)

    def test_two_example(self):
        paint_after_folding(*self.example_data)
        self.assertion(True)

    def test_two_data(self):
        paint_after_folding(*self.input_data)
        self.assertion(True)
