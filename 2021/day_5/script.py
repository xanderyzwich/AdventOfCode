"""
Day 5: Hydrothermal Venture
"""
from unittest import TestCase


def parse_vents_from_file(file_name):
    vents = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            first, second = line.strip().split(' -> ')
            x1, y1 = first.split(',')
            x2, y2 = second.split(',')
            vents.append(tuple(int(n) for n in (x1, y1, x2, y2)))
    return vents


def map_vents(vents_list, part=1):
    vent_map = {}
    max_x, max_y = 0, 0
    print(vents_list)
    for x1, y1, x2, y2 in vents_list:
        small_x, large_x = min(x1, x2), max(x1, x2)
        small_y, large_y = min(y1, y2), max(y1, y2)
        max_x, max_y = max(large_x, max_x), max(large_y, max_y)

        horizontal = y1 == y2
        vertical = x1 == x2
        if horizontal:
            for x in range(small_x, large_x+1):
                point = x, y1
                if point in vent_map:
                    vent_map[point] += 1
                else:
                    vent_map[point] = 1
        elif vertical:
            for y in range(small_y, large_y+1):
                point = x1, y
                if point in vent_map:
                    vent_map[point] += 1
                else:
                    vent_map[point] = 1
        elif part == 2:
            start_left = x1 == small_x
            horizontal_direction = 1 if start_left else -1
            start_top = y1 == small_y
            vertical_direction = 1 if start_top else -1
            # print(f'Starting Diagonal from {x1, y1} to {x2, y2}')
            for y, x in zip(range(y1, y2+vertical_direction, vertical_direction), range(x1, x2+horizontal_direction, horizontal_direction)):  # iterate top to bottom
                point = x, y
                # print(point)
                if point in vent_map:
                    vent_map[point] += 1
                else:
                    vent_map[point] = 1

    return vent_map, max_x, max_y


def print_map(vent_map, max_x, max_y):
    visual = '\n'
    for row in range(max_y+1):
        for col in range(max_x+1):
            visual += str(vent_map[(col, row)]) if (col, row) in vent_map else '.'
        visual += '\n'
    print(visual)


def count_danger_points(vent_map, threshold=2):
    count = 0
    for point, value in vent_map.items():
        if value >= threshold:
            count += 1
    return count


class TestVentMapping(TestCase):
    example_data = parse_vents_from_file('example.txt')
    input_data = parse_vents_from_file('data.txt')

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
        map_data = map_vents(self.example_data)
        # print_map(*map_data)
        mapped_vents, *_ = map_data
        danger_count = count_danger_points(mapped_vents)
        self.assertion(5 == danger_count)

    def test_one_data(self):
        map_data, *_ = map_vents(self.input_data)
        danger_count = count_danger_points(map_data)
        self.assertion(6856 == danger_count)

    def test_two_example(self):
        map_data = map_vents(self.example_data, part=2)
        print_map(*map_data)
        mapped_vents, *_ = map_data
        danger_count = count_danger_points(mapped_vents)
        self.assertion(12 == danger_count)

    def test_two_data(self):
        map_data = map_vents(self.input_data, part=2)
        mapped_vents, *_ = map_data
        danger_count = count_danger_points(mapped_vents)
        self.assertion(20666 == danger_count)
