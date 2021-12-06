"""
Day 6: Lanternfish
"""
from unittest import TestCase


def another_day(fish_list):
    new_fish = []
    for i in range(len(fish_list)):
        if 0 == fish_list[i]:
            fish_list[i] = 6
            new_fish.append(8)
        else:
            fish_list[i] = fish_list[i]-1
    fish_list.extend(new_fish)


def population_after_days(fish_school, num):
    for _ in range(num):
        another_day(fish_school)
    return len(fish_school)


def population_by_group(fish_school, days):
    counts = {i: fish_school.count(i) for i in range(9)}
    for _ in range(days):
        counts = {
            0: counts[1],
            1: counts[2],
            2: counts[3],
            3: counts[4],
            4: counts[5],
            5: counts[6],
            6: counts[0]+counts[7],
            7: counts[8],
            8: counts[0],
        }
    print(counts)
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
        fishes = self.example_data
        self.assertion(26 == population_after_days(fishes, 18))
        self.assertion(5934 == population_after_days(fishes, 62))

    def test_one_data(self):
        count = population_after_days(self.input_data, 80)
        self.assertion(353079 == count)

    def test_two_example(self):
        count = population_after_days(self.example_data, 256)
        self.assertion(26984457539 == count)

    def test_two_counts_example(self):
        fishes = self.example_data
        self.assertion(26 == population_by_group(fishes, 18))
        self.assertion(5934 == population_by_group(fishes, 80))
        self.assertion(26984457539 == population_by_group(fishes, 256))

    def test_two_data(self):
        fishes = self.input_data
        count = population_by_group(fishes, 256)
        print(count)
        self.assertion(count)
