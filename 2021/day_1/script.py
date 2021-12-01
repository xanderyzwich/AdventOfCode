"""
Day 1: Sonar Sweep
"""
from unittest import TestCase


def count_depth_increases(stuff):
    count = 0
    for i in range(1, len(stuff)):
        count += 1 if stuff[i-1] < stuff[i] else 0
    print(count)
    return count


def int_list_from_file(name):
    data = []
    with open(name, 'r') as input_file:
        for line in input_file:
            data.append(int(line.strip()))
    return data


def sliding_window_sum(nums, window_size=3):
    window_sums = []
    for i in range(window_size-1, len(nums)):
        current_sum = sum(nums[i-2:i+1])
        window_sums.append(current_sum)
    return window_sums


class TestDay1(TestCase):
    example = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

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
        self.assertion(count_depth_increases(self.example) == 7)

    def test_one_data(self):
        data = int_list_from_file('data.txt')
        result = count_depth_increases(data)
        self.assertion(1266 == result)

    def test_two_example(self):
        sums = sliding_window_sum(self.example)
        self.assertion(sums == [607, 618, 618, 617, 647, 716, 769, 792])
        result = count_depth_increases(sums)
        self.assertion(5 == result)

    def test_two_data(self):
        data = int_list_from_file('data.txt')
        sums = sliding_window_sum(data)
        result = count_depth_increases(sums)
        self.assertion(1217 == result)
