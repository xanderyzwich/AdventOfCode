"""
https://adventofcode.com/2020/day/1
"""
from unittest import TestCase


def expense_report(input_arr, add_to=2020):
    """
    Find the two numbers that sum to 2020 and return their product
    """
    i, j = 0, len(input_arr) - 1
    print(add_to, input_arr)
    while i <= j:
        left, right = input_arr[i], input_arr[j]
        total = left + right
        if total == add_to:
            print("exiting expense_report from :", left, right, left * right)
            return left * right
        elif total < add_to:
            i += 1
        elif total > add_to:
            j -= 1


def convert(input_file):
    return sorted([int(x) for x in list(input_file)])


def three_fer(input_arr):
    """
    find 3 numbers that total 2020 and return their product
    """
    for i, x in enumerate(input_arr):
        temp_result = expense_report(input_arr[i+1:], add_to=2020-x)
        if temp_result:
            return temp_result * x


def brute_force(input_arr):
    """
    3 numbers
    :param input_arr:
    :return:
    """
    for i in range(len(input_arr)-2):
        for j in range(i+1, len(input_arr)-1):
            for k in range(j+1, len(input_arr)):
                a, b, c = input_arr[i], input_arr[j], input_arr[k]
                if sum([a, b, c]) == 2020:
                    print(a, b, c, a+b+c, a*b*c)
                    return a * b * c


class TestExpenseReport(TestCase):
    example = [1721, 979, 366, 299, 675, 1456]

    def test_one_example(self):
        assert expense_report(self.example) == 514579

    def test_one(self):
        with open("day1.part1.txt", 'r') as in_file:
            assert expense_report(convert(in_file)) == 913824
            # print("Part 1 with data:", expense_report(convert(in_file)))  # 913824

    def test_three_fer_example(self):
        assert three_fer(self.example) == 241861950

    def test_three_fer_two(self):
        with open("day1.part1.txt", 'r') as in_file:
            result = three_fer(convert(in_file))
            # print("Three_fer with data:", result)  # 240889536
            assert result == 240889536


    def test_two_example(self):
        assert 979 * 366 * 675 == 241861950
        assert expense_report(self.example[2:], add_to=2020-979) == (366*675)
        assert brute_force(self.example) == 241861950

    def test_two(self):
        with open("day1.part1.txt", 'r') as in_file:
            assert brute_force(convert(in_file)) == 240889536
            # print("Part 2 with Data:", brute_force(convert(in_file)))  # 240889536
