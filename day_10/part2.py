from unittest import TestCase


def parse_file(file_name):
    with open(file_name, 'r') as input_file:
        data = sorted([int(line) for line in input_file])
    return data


def get_diffs(data_set):
    diffs = [data_set[0]]
    for i in range(1, len(data_set)):
        diffs.append(data_set[i] - data_set[i-1])
    return diffs


def run_lengths(diff_set):
    permute_count = 1
    j = 0
    while j < len(diff_set):
        temp_set = []
        if sum([diff_set[j:j+3]]) == 3:
            permute_count *= 6
            j += 3
        elif sum(diff_set[j:j+2]) == 3:
            permute_count *= 2
            j += 2
        elif diff_set[j] == 3:
            j += 1

    return permute_count





class TestThing(TestCase):

    def setUp(self) -> None:
        print(f'In method: {self._testMethodName}')

    def test_two_short_example(self):
        file_diffs = get_diffs(parse_file('short_example.txt'))
        print(file_diffs)
        # assert length == 8

    def test_two_long_example(self):
        file = parse_file('long_example.txt')
        at = AdapterTree(file)
        assert len(at) == 19208

    def test_two_data(self):
        print('Reading File')
        file = parse_file('data.txt')
        print('Building Tree')
        at = AdapterTree(file)
        print(at.root.values)
        print('Calculating length')
        length = len(at)
        print(length)  # not 629856
        assert length