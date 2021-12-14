"""
Day X: Name
"""
from copy import deepcopy
from unittest import TestCase


class OctopusField:

    def __init__(self, energy_levels):
        self.energy_levels = deepcopy(energy_levels)
        self.step = 0
        self.flash_count = 0

    def take_step(self):
        flash_queue = []

        # Increment Energy levels
        for r in range(len(self.energy_levels)):
            row = self.energy_levels[r]
            for c in range(len(row)):
                self.energy_levels[r][c] += 1
                has_energy = 9 < self.energy_levels[r][c]
                if has_energy:
                    flash_queue.append((r, c))

        # Flash if you can, but just once
        has_flashed = []
        while 0 < len(flash_queue):
            r, c = flash_queue.pop(0)
            has_flashed.append((r, c))
            more_to_flash = self.flash_others(r, c)
            for mtf in more_to_flash:
                if mtf not in flash_queue and mtf not in has_flashed:
                    flash_queue.append(mtf)
        for r, c in has_flashed:
            self.energy_levels[r][c] = 0
        self.step += 1
        self.flash_count += len(has_flashed)
        return len(has_flashed)

    def flash_others(self, row, col):
        can_flash_next = []
        for r, c in self.__get_adjacents__(row, col):
            self.energy_levels[r][c] += 1
            if 9 < self.energy_levels[r][c]:
                can_flash_next.append((r, c))
        return can_flash_next

    def __get_adjacents__(self, row, col):
        result = [(r, c) for (r, c) in [
            (row-1, col), (row-1, col-1), (row-1, col+1),
            (row, col-1), (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        ] if 0 <= r < len(self.energy_levels) and 0 <= c < len(self.energy_levels[r])]
        return result


def flash_count_after(data, steps):
    octopus_field = OctopusField(data)
    for _ in range(steps):
        octopus_field.take_step()
    return octopus_field.flash_count

def first_all_flash(data):
    octopus_field = OctopusField(data)
    i = 0
    full_size = len(octopus_field.energy_levels) * len(octopus_field.energy_levels[0])
    while full_size > octopus_field.take_step():
        i += 1
    return i+1


def parse_file(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = [int(n) for n in list(line.strip())]
            data.append(clean)
    return data


class TestOctopusField(TestCase):
    example_data = parse_file('example.txt')
    input_data = parse_file('input.txt')

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

    def test_get_adjacents(self):
        octo_field = OctopusField(self.example_data)
        self.assertion(3 == len(octo_field.__get_adjacents__(0, 0)))
        self.assertion(5 == len(octo_field.__get_adjacents__(0, 5)))
        self.assertion(3 == len(octo_field.__get_adjacents__(0, 9)))
        self.assertion(5 == len(octo_field.__get_adjacents__(1, 0)))
        self.assertion(8 == len(octo_field.__get_adjacents__(1, 5)))
        self.assertion(5 == len(octo_field.__get_adjacents__(1, 9)))
        self.assertion(3 == len(octo_field.__get_adjacents__(9, 0)))
        self.assertion(5 == len(octo_field.__get_adjacents__(9, 5)))
        self.assertion(3 == len(octo_field.__get_adjacents__(9, 9)))

    def test_one_example(self):
        result = flash_count_after(self.example_data, 2)
        # print(result)
        self.assertion(35 == result)

        result = flash_count_after(self.example_data, 10)
        self.assertion(204 == result)

        result = flash_count_after(self.example_data, 100)
        self.assertion(1656 == result)

    def test_one_data(self):
        result = flash_count_after(self.input_data, 100)
        self.assertion(1719 == result)

    def test_two_example(self):
        step = first_all_flash(self.example_data)
        self.assertion(195 == step)

    def test_two_data(self):
        step = first_all_flash(self.input_data)
        self.assertion(232 == step)
