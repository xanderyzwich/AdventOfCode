"""
Day 8: Seven Segment Search
"""
from unittest import TestCase


# broken out of parse_data in order to test the short example
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


# part 1
def count_unique_segment_sizes(data):
    count = 0
    for entry in data:
        for d in entry['digits']:
            count += 1 if len(d) in [2, 3, 4, 7] else 0
    return count


# used to order the segments in a given signal
# this prevents issues if segments are disordered between digits and base signals
def sort_string(jumble):
    char_list = list(jumble)
    char_list.sort()
    return ''.join(char_list)


def deduce_cipher(entry_signals):
    segment_counts, unique_cipher = get_counts_and_unique(entry_signals)
    segment_mapping = map_segments(segment_counts, unique_cipher)
    return translate_signals(entry_signals, segment_mapping)


def get_counts_and_unique(entry_signals):
    segment_counts = {alpha: 0 for alpha in ['a', 'b', 'c', 'd', 'e', 'f', 'g']}  # based on signal not proper
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
    return segment_counts, unique_cipher


def translate_signals(entry_signals, segment_mapping):
    cipher = {}
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

    # map signals to numbers
    for signal in entry_signals:
        plaintext_signal = [segment_mapping[k] for k in list(signal)]
        clean_signal = sort_string(plaintext_signal)
        cipher[sort_string(signal)] = proper_segment_cipher[clean_signal]
    return cipher


# build segment translation mapping from signal to proper
def map_segments(segment_counts, unique_cipher):
    segment_mapping = {}
    get_proper_segment_name = {
        4: lambda segment_name, unique: 'e',
        6: lambda segment_name, unique: 'b',
        9: lambda segment_name, unique: 'f',
        8: lambda segment_name, unique: 'c' if segment_name in unique[1] else 'a',
        7: lambda segment_name, unique: 'd' if segment_name in unique[4] else 'g',
    }
    for segment, count in segment_counts.items():
        segment_mapping[segment] = get_proper_segment_name[count](segment, unique_cipher)
    return segment_mapping


def decode_digits(digit_list, cipher):
    result = ''.join([str(cipher[sort_string(digit)]) for digit in digit_list])
    return int(result)


def decode_entry(data_entry):
    cipher = deduce_cipher(data_entry['signals'])
    return decode_digits(data_entry['digits'], cipher)


def sum_entries(entry_list):
    return sum([decode_entry(entry) for entry in entry_list])


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
