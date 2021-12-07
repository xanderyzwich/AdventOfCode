"""
Day X: Name
"""
import sys
from unittest import TestCase


def horizontal_of_least_fuel(horizontals_list):
    middle = int(len(horizontals_list)/2)
    return horizontals_list[middle]  # median


def fuel_to_horizontal(given_horizontal, horizontals_list):
    return sum([abs(given_horizontal-h) for h in horizontals_list])


def non_linear_fuel_cost(given_horizontal, horizontals_list):
    fuel_cost = 0
    for h in horizontals_list:
        n = abs(given_horizontal-h)
        fuel_cost += (n**2+n)/2  # triangular distribution
    return fuel_cost


def non_linear_guess_horizontal(horizontals_list):
    min_fuel = sys.maxsize  # big number
    for i in range(max(horizontals_list)):
        check_guess = non_linear_fuel_cost(i, horizontals_list)
        if check_guess < min_fuel:
            min_fuel = check_guess
        else:
            return min_fuel


def parse_file(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            data = [int(l) for l in line.strip().split(',')]
    data.sort()
    return data


class TestThing(TestCase):
    example_data = parse_file('example.txt')
    input_data = parse_file('data.txt')

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
        ideal_horizontal = horizontal_of_least_fuel(self.example_data)
        self.assertion(2 == ideal_horizontal)
        fuel_cost = fuel_to_horizontal(ideal_horizontal, self.example_data)
        self.assertion(37 == fuel_cost)

    def test_one_data(self):
        horizontal = horizontal_of_least_fuel(self.input_data)
        fuel_cost = fuel_to_horizontal(horizontal, self.input_data)
        self.assertion(352331 == fuel_cost)

    def test_two_example(self):
        fuel_cost = non_linear_guess_horizontal(self.example_data)
        self.assertion(168 == fuel_cost)

    def test_two_data(self):
        fuel_cost = non_linear_guess_horizontal(self.input_data)
        self.assertion(99266250 == fuel_cost)
