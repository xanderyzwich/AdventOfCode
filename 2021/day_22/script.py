"""
Day 22: Reactor Reboot
"""
import logging
import sys
from functools import reduce
from unittest import TestCase


def initialize_reactor(flips, limit=50):
    cubes = {}
    for cube in flips:
        print(cube)
        if not any([abs(n) > limit for n in [*cube.x_range, *cube.y_range, *cube.z_range]]):
            for i in range(cube.x_min, cube.x_max + 1):
                for j in range(cube.y_min, cube.y_max + 1):
                    for k in range(cube.z_min, cube.z_max + 1):
                        cubes[(i, j, k)] = cube.switch_value
    return reduce(lambda a, b: a + b, list(cubes.values()))


def reboot_reactor(flip_data, limit=sys.maxsize):
    powered_on = []
    for new_cube in flip_data:
        logging.debug(f'\nAdding: {new_cube}')
        if not any([abs(n) > limit for n in [*new_cube.x_range, *new_cube.y_range, *new_cube.z_range]]):
            check_size = len(powered_on)
            for _ in range(check_size):
                cube = powered_on.pop(0)
                powered_on.extend(cube.remove_overlap(new_cube))
            if 1 == new_cube.switch_value:
                if 0 == check_size:
                    logging.debug(f'\tTurning on {new_cube.size} cubes')
                powered_on.append(new_cube)
        logging.debug('Currently powered on:')
        for c in powered_on:
            logging.debug(f'\t{c}')
    logging.debug('Final list:')
    for cube in powered_on:
        logging.debug(cube)
    on_count = reduce(lambda x, y: x + y, [c.size for c in powered_on])
    logging.info(f'Reboot_reactor result: {on_count}')
    return on_count


class Cube:
    def __init__(self, switch, x_range, y_range, z_range):
        self.switch_value = switch
        self.x_min, self.x_max = x_range
        self.y_min, self.y_max = y_range
        self.z_min, self.z_max = z_range
        pass

    def overlap(self, other, axis='all'):
        if 'x' == axis:
            return any([
                self.x_min <= other.x_min <= self.x_max,
                self.x_min <= other.x_max <= self.x_max,
                other.x_min <= self.x_min <= other.x_max,
                other.x_min <= self.x_max <= other.x_max,
                        ])
        if 'y' == axis:
            return any([
                self.y_min <= other.y_min <= self.y_max,
                self.y_min <= other.y_max <= self.y_max,
                other.y_min <= self.y_min <= other.y_max,
                other.y_min <= self.y_max <= other.y_max,
                        ])
        if 'z' == axis:
            return any([
                self.z_min <= other.z_min <= self.z_max,
                self.z_min <= other.z_max <= self.z_max,
                other.z_min <= self.z_min <= other.z_max,
                other.z_min <= self.z_max <= other.z_max,
                        ])
        if 'all' == axis:
            return all([self.overlap(other, 'x'), self.overlap(other, 'y'), self.overlap(other, 'z')])

    def remove_overlap(self, other):
        segments = list()
        logging.debug(f'\n\tChecking overlap of \n\tSelf:  {self}\n\tOther: {other}')
        before_size = self.size
        if not self.overlap(other):
            return [self]

        # slice on x
        if self.x_min < self.x_max:
            if self.x_min <= other.x_min <= self.x_max:  # slice off low
                piece = Cube(self.switch_value, (self.x_min, other.x_min-1), self.y_range, self.z_range)
                if piece.x_min <= piece.x_max:
                    logging.debug(f'\tSlicing X low {piece}')
                    segments.append(piece)
                    self.x_min = other.x_min
            if 0 < self.size and (self.x_min <= other.x_max <= self.x_max):  # slice off high
                piece = Cube(self.switch_value, (other.x_max+1, self.x_max), self.y_range, self.z_range)
                if piece.x_min <= piece.x_max:
                    logging.debug(f'\tSlicing X high {piece}')
                    segments.append(piece)
                    self.x_max = other.x_max

        # slice on y
        if self.y_min < self.y_max:
            if 0 < self.size and (self.y_min <= other.y_min <= self.y_max):  # slice off low
                piece = Cube(self.switch_value, self.x_range, (self.y_min, other.y_min-1), self.z_range)
                if piece.y_min <= piece.y_max:
                    logging.debug(f'\tSlicing Y low {piece}')
                    segments.append(piece)
                    self.y_min = other.y_min
            if 0 < self.size and (self.y_min <= other.y_max <= self.y_max):  # slice off high
                piece = Cube(self.switch_value, self.x_range, (other.y_max+1, self.y_max), self.z_range)
                if piece.y_min <= piece.y_max:
                    logging.debug(f'\tSlicing Y high {piece}')
                    segments.append(piece)
                    self.y_max = other.y_max

        # slice on z
        if self.z_min < self.z_max:
            if 0 < self.size and (self.z_min <= other.z_min <= self.z_max):  # slice off low
                piece = Cube(self.switch_value, self.x_range, self.y_range, (self.z_min, other.z_min-1))
                if piece.z_min <= piece.z_max:
                    logging.debug(f'\tSlicing Z low {piece}')
                    segments.append(piece)
                    self.z_min = other.z_min
            if 0 < self.size and (self.z_min <= other.z_max <= self.z_max):  # slice off high
                piece = Cube(self.switch_value, self.x_range, self.y_range, (other.z_max+1, self.z_max))
                if piece.z_min <= piece.z_max:
                    logging.debug(f'\tSlicing Z high {piece}')
                    segments.append(piece)
                    self.z_max = other.z_max

        # At this point self is the overlap with other
        if 0 < len(segments):
            if logging.DEBUG == logging.getLogger().level:
                for segment in segments:
                    logging.debug(f'\tSegment: {segment}')
            segments_size = reduce(lambda x, y: x+y, [c.size for c in segments])

            logging.debug(f'removed overlap size: {self.size}')
            if logging.DEBUG == logging.getLogger().level:
                if 1 == other.switch_value:
                    logging.debug(f'\tTurning on {other.size - self.size}')
                else:
                    logging.debug(f'\tTurned off {before_size - segments_size}')
            return segments
        logging.debug(f'\tNo overlap found')
        return [self]

    @property
    def size(self):
        size = (self.x_max - self.x_min + 1) * (self.y_max - self.y_min + 1) * (self.z_max - self.z_min + 1)
        return size

    @property
    def x_range(self):
        return self.x_min, self.x_max

    @property
    def y_range(self):
        return self.y_min, self.y_max

    @property
    def z_range(self):
        return self.z_min, self.z_max

    def __repr__(self):
        return f'Cube:\t{self.switch_value}\tx:{self.x_range}\ty:{self.y_range}\tz:{self.z_range}\tsize:{self.size}'


def parse_file(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = line.strip()
            flip_to_position, ranges = clean.split(' ')
            flip_value = 1 if flip_to_position == 'on' else 0
            x_range, y_range, z_range = ranges.split(',')
            x_min, x_max = (int(i) for i in x_range.replace('x=', '').split('..'))
            y_min, y_max = (int(i) for i in y_range.replace('y=', '').split('..'))
            z_min, z_max = (int(i) for i in z_range.replace('z=', '').split('..'))
            data.append(Cube(flip_value, (x_min, x_max), (y_min, y_max), (z_min, z_max)))
    return data


class TestReactorReboot(TestCase):
    small_example_data = parse_file('small_example.txt')
    larger_example_data = parse_file('larger_example.txt')
    part2_example = parse_file('part2_example.txt')
    input_data = parse_file('input.txt')

    @classmethod
    def setUpClass(cls) -> None:
        logging.basicConfig(level=logging.DEBUG)
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
        # count = initialize_reactor(self.small_example_data)  # OOP style
        count = reboot_reactor(self.small_example_data, limit=50)
        self.assertion(39 == count)

        count = initialize_reactor(self.larger_example_data)  # OOP style
        self.assertion(590784 == count)

    def test_one_data(self):
        count = initialize_reactor(self.input_data)
        self.assertion(545118 == count)

    def test_two_example(self):
        # count = initialize_reactor(self.part2_example, limit=50)
        # count = reboot_reactor(self.part2_example, limit=50)
        # self.assertion(474140 == count)
        count = reboot_reactor(self.part2_example)
        expected = 2_758_514_936_282_235
        print(count, '-', expected, '=', count-expected)
        self.assertion(expected == count)

    def test_two_data(self):
        self.assertion(True)
