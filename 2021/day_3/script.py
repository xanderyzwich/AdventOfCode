"""
Day X: Name
"""
from unittest import TestCase


def add_lists_by_element(list_a, list_b):
    return [list_a[i]+list_b[i] for i in range(len(list_a))]


def get_power_consumption(string_list):
    line_count = 0

    # count ones in each column
    ones_counts = [0 for _ in range(len(string_list[0]))]
    for row in string_list:
        line_count += 1
        columns = [int(i) for i in list(row)]
        ones_counts = add_lists_by_element(ones_counts, columns)

    gamma_columns = [str(round(col/line_count)) for col in ones_counts]
    gamma = int(''.join(gamma_columns), 2)

    epsilon_columns = ['0' if a =='1' else '1' for a in gamma_columns]
    epsilon = int(''.join(epsilon_columns), 2)
    return gamma*epsilon


def filter_by_bits(data_list, most_common):
    columns = len(data_list[0])
    contenders = data_list
    for i in range(columns):
        ones, zeroes = [], []
        for row in contenders:
            if '1' == row[i]:
                ones.append(row)
            else:
                zeroes.append(row)
        if len(ones) >= len(zeroes):
            contenders = ones if most_common else zeroes
        else:
            contenders = zeroes if most_common else ones
        if 1 == len(contenders):
            return int(contenders[0], 2)


def get_life_support_rating(string_list):
    oxygen_generator_rating = filter_by_bits(string_list, most_common=True)
    co2_scrubber_rating = filter_by_bits(string_list, most_common=False)
    return oxygen_generator_rating * co2_scrubber_rating


def convert_file_to_string_list(file_name):
    string_list = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            string_list.append(line.strip())
    return string_list


class TestThing(TestCase):
    example_data = convert_file_to_string_list('example.txt')
    input_data = convert_file_to_string_list('data.txt')

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
        result = get_power_consumption(self.example_data)
        self.assertion(198 == result)

    def test_one_data(self):
        result = get_power_consumption(self.input_data)
        self.assertion(3374136 == result)

    def test_two_example(self):
        result = get_life_support_rating(self.example_data)
        self.assertion(230 == result)

    def test_two_data(self):
        result = get_life_support_rating(self.input_data)
        self.assertion(4432698 == result)
