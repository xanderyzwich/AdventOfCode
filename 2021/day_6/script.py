"""
Day 6: Lanternfish
"""
from unittest import TestCase


def population_by_group(fish_school, days):
    counts = {i: fish_school.count(i) for i in range(9)}
    for _ in range(days):
        counts = {i: counts[(i+1) % 9] for i in counts}
        counts[6] += counts[8]
    return sum(counts.values())


def parse_file(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            data = [int(l) for l in line.strip().split(',')]
    return data


class TestThing(TestCase):
    example_data = [3, 4, 3, 1, 2]
    example_growth = [5, 5, 6, 7, 9, 10, 10, 10, 10, 11, 12, 15, 17, 19, 20, 20, 21, 22, 26]
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
        self.assertion(26 == population_by_group(self.example_data, 18))
        self.assertion(5934 == population_by_group(self.example_data, 80))

    def test_one_data(self):
        self.assertion(353079 == population_by_group(self.input_data, 80))

    def test_two_example(self):
        self.assertion(26984457539 == population_by_group(self.example_data, 256))

    def test_two_counts_example(self):
        self.assertion(26 == population_by_group(self.example_data, 18))
        self.assertion(5934 == population_by_group(self.example_data, 80))
        self.assertion(26984457539 == population_by_group(self.example_data, 256))

    def test_two_data(self):
        self.assertion(1605400130036 == population_by_group(self.input_data, 256))
