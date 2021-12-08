"""
Day 8: Seven Segment Search
"""
from unittest import TestCase


def parse_line(input_line):
    signal_pattern_part, four_digit_part = input_line.strip().split(' | ')
    signals = signal_pattern_part.split()
    digits = four_digit_part.split()
    return {'signals': signals, 'digits': digits}


def parse_data(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            data.append(parse_line(line))
    return data


def count_unique_segment_sizes(data):
    count = 0
    for entry in data:
        for d in entry['digits']:
            count += 1 if len(d) in [2, 3, 4, 7] else 0
    # print(count)
    return count


def sort_string(jumble):
    char_list = list(jumble)
    char_list.sort()
    return ''.join(char_list)


segment_sums = {  # summing the number of times each segment appears in proper digits
    'a': 8,
    'b': 6,
    'c': 8,
    'd': 7,
    'e': 4,
    'f': 9,
    'g': 7,
}
segment_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
segments_per_number = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    0: 6
}
proper_segment_cipher = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

def deduce_cipher(entry_signals):
    cipher = {}
    segment_counts = {alpha: 0 for alpha in segment_names}  # based on signal not proper
    segment_mapping = {}  # from signal name to proper name

    unique_cipher = {}
    for signal in entry_signals:
        length = len(signal)

        # Let's get the unique lengths first
        if 2 == length:
            unique_cipher[1] = signal
        elif 4 == length:
            unique_cipher[4] = signal
        elif 3 == length:
            unique_cipher[7] = signal
        elif 9 == length:
            unique_cipher[8] = signal

        # add to the counts for each segment name
        for c in list(signal):
            segment_counts[c] += 1

    for k, v in segment_counts.items():
        if 4 == v:
            segment_mapping[k] = 'e'
        elif 6 == v:
            segment_mapping[k] = 'b'
        elif 9 == v:
            segment_mapping[k] = 'f'
        elif 8 == v:
            segment_mapping[k] = 'c' if k in unique_cipher[1] else 'a'
        elif 7 == v:
            segment_mapping[k] = 'd' if k in unique_cipher[4] else 'g'
        else:
            print('Count Error', k, v)

    for signal in entry_signals:
        plaintext_signal = [segment_mapping[k] for k in list(signal)]
        clean_signal = sort_string(plaintext_signal)
        cipher[sort_string(signal)] = proper_segment_cipher[clean_signal]
    # print(cipher)
    return cipher


def decode(digit_list, cipher):
    result = ''.join([str(cipher[sort_string(digit)]) for digit in digit_list])
    return int(result)


def decode_entry(data_entry):
    cipher = deduce_cipher(data_entry['signals'])
    return decode(data_entry['digits'], cipher)


def sum_entries(entry_list):
    total = 0
    for entry in entry_list:
        total += decode_entry(entry)
    return total


class TestThing(TestCase):
    example_data = parse_data('example.txt')
    input_data = parse_data('data.txt')

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
        count = count_unique_segment_sizes(self.example_data)
        self.assertion(26 == count)

    def test_one_data(self):
        count = count_unique_segment_sizes(self.input_data)
        self.assertion(543 == count)

    def test_two_example(self):
        short_example = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
        short_data = parse_line(short_example)
        short_cipher = deduce_cipher(short_data['signals'])
        self.assertion(short_cipher == {sort_string(k): v for k, v in {
            'acedgfb': 8,
            'cdfbe': 5,
            'gcdfa': 2,
            'fbcad': 3,
            'dab': 7,
            'cefabd': 9,
            'cdfgeb': 6,
            'eafb': 4,
            'cagedb': 0,
            'ab': 1,
        }.items()})
        short_number = decode_entry(short_data)
        self.assertion(5353 == short_number)

        result = sum_entries(self.example_data)
        self.assertion(61229 == result)

    def test_two_data(self):
        result = sum_entries(self.input_data)
        self.assertion(994266 == result)
