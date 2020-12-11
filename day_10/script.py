"""
Day 10: Adapter Array
"""
from datetime import datetime
from unittest import TestCase


def count_jolts(file_name):
    counts, current_jolts = {1: 0, 2: 0, 3: 0}, 0
    data = parse_file(file_name)
    for i in range(len(data)):
        diff = data[i] - current_jolts
        counts[diff] += 1
        # print(f'{data[i]} - {current_jolts} = {diff}  TOTALS: {counts}')
        current_jolts = data[i]
    counts[3] += 1
    return counts


def parse_file(file_name):
    with open(file_name, 'r') as input_file:
        data = sorted([int(line) for line in input_file])
    return data


def part_one(counts_dict):
    return counts_dict[1] * counts_dict[3]


class AdapterTreeNode:

    def __init__(self, value):
        self.value = value
        self.children = {}
        self.values = [value]

    def add_child(self, child):
        was_added = False
        for v in [child.value - 1, child.value - 2, child.value - 3]:
            if not self.contains(v):
                continue
            if self.value == v:
                # print("It's me")
                self.children[child.value] = child
            else:
                [kid.add_child(child) for kid in self.children.values() if kid.contains(v)]
            was_added = True
            self.values.append(child.value)
        return was_added

    def contains(self, value):
        return value in self.values


    @property
    def kids(self):
        return self.children.keys()

    def valid_leaf_count(self, limit):
        if self.value == limit:
            return 1
        return sum(child.valid_leaf_count(limit) for child in self.children.values())

    def __str__(self, level=0):
        temp = '\t'*level + str(self.value)
        if len(self.children.values()) == 0:
            return temp
        temp += ': { ' + str(list(self.children.keys())) + '\n'
        for c in self.children.values():
            temp += c.__str__(level+1)
        temp += '\n' + '\t'*level + '}\n'
        return temp


class AdapterTree:

    def __init__(self, data_array):
        self.data_array = data_array
        self.root = AdapterTreeNode(0)
        count, start = 1, datetime.now()
        for val in self.data_array:
            print(f'Adding {count}th value : {val}')
            before = datetime.now()
            self.root.add_child(AdapterTreeNode(val))
            print(f'    {val} added {datetime.now() - before}')
            count += 1

    def __len__(self):
        return self.root.valid_leaf_count(self.data_array[-1])

    def __str__(self):
        return f'{self.data_array}\n{self.root.__str__()}'


class TestThing(TestCase):

    def setUp(self) -> None:
        print(f'In method: {self._testMethodName}')

    def test_one_short_example(self):
        count = count_jolts('short_example.txt')
        assert count == {1: 7, 2: 0, 3: 5}
        assert part_one(count) == 35

    def test_one_long_example(self):
        count = count_jolts('long_example.txt')
        assert count == {1: 22, 2: 0, 3: 10}
        assert part_one(count) == 220

    def test_one_data(self):
        count = count_jolts('data.txt')
        assert count == {1: 64, 2: 0, 3: 32}
        assert part_one(count) == 2048

    def test_two_short_example(self):
        at = AdapterTree(parse_file('short_example.txt'))
        print(at)
        length = len(at)
        assert length == 8

    def test_two_long_example(self):
        at = AdapterTree(parse_file('long_example.txt'))
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
