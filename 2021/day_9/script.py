"""
Day 9: Smoke Basin
"""
from unittest import TestCase


def get_get_adjacent_indexes(current_row, current_col, full_2d_list):
    adjacents = []
    if 0 < current_row:
        adjacents.append((current_row - 1, current_col))
    if len(full_2d_list) > current_row + 1:
        adjacents.append((current_row + 1, current_col))
    if 0 <= current_col - 1:
        adjacents.append((current_row, current_col - 1))
    if len(full_2d_list[current_row]) > current_col + 1:
        adjacents.append((current_row, current_col + 1))
    return adjacents


def get_adjacent_values(current_row, current_col, full_2d_list, with_indexes=False):
    indexes = get_get_adjacent_indexes(current_row, current_col, full_2d_list)
    values = [full_2d_list[r][c] for r, c in indexes]
    return list(zip(indexes, values)) if with_indexes else values


def find_low_points(data_2d_list, return_indexes=False):
    low_point_heights = []
    low_point_locations = []
    for row in range(len(data_2d_list)):
        for col in range(len(data_2d_list[row])):
            current_value = data_2d_list[row][col]
            adjacent_values = get_adjacent_values(row, col, data_2d_list)
            low_point = all([adj_val > current_value for adj_val in adjacent_values])
            if low_point:
                low_point_heights.append(current_value)
                low_point_locations.append((row, col))
    if return_indexes:
        return low_point_locations
    return low_point_heights


def total_risk_level(data_2d_list):
    return sum([1 + x for x in find_low_points(data_2d_list)])


def size_of_basin(low_row, low_col, data_2d_list):
    basin_points = [(low_row, low_col)]
    found_new_point = True
    while found_new_point:
        # print(f' Current basin size: {len(basin_points)}')
        new_points = []
        found_new_point = False
        for point in basin_points:
            adjacents = get_adjacent_values(*point, data_2d_list, with_indexes=True)
            # print(f'Point: {point} has adjacents: {[(p, v) for p,v in adjacents]}')
            for adj_point, adj_val in adjacents:
                in_basin, in_new = adj_point in basin_points, adj_point in new_points
                is_peak = 9 == adj_val
                if any([in_basin, in_new, is_peak]):
                    continue
                new_points.append(adj_point)
                found_new_point = True
        if 1 < len(new_points):
            # print('Found multiple new points', new_points)
            basin_points.extend(new_points)
        elif 1 == len(new_points):
            # print('Found ONE new point')
            basin_points.append(new_points[0])
    return len(basin_points)


def find_basin_sizes(data_2d_list):
    low_points = find_low_points(data_2d_list, return_indexes=True)
    return [size_of_basin(*point, data_2d_list) for point in low_points]


def product_of_biggest_basins(data_2d_list, count=3):
    basin_sizes = find_basin_sizes(data_2d_list)
    print(basin_sizes)
    basin_sizes.sort(reverse=True)
    product = 1
    for size in basin_sizes[:count]:
        product *= size
    return product


def parse_file(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = [int(n) for n in list(line.strip())]
            data.append(clean)
    return data


class TestThing(TestCase):
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

    def test_one_example(self):
        heights = find_low_points(self.example_data)
        self.assertion([1, 0, 5, 5] == heights)
        self.assertion(15 == total_risk_level(self.example_data))

    def test_one_data(self):
        risk_score = total_risk_level(self.input_data)
        # print(risk_score)
        self.assertion(570 == risk_score)

    def test_two_example(self):
        size = size_of_basin(0, 1, self.example_data)
        self.assertion(3 == size)
        result = product_of_biggest_basins(self.example_data)
        # print(result)
        self.assertion(1134 == result)

    def test_two_data(self):
        size = product_of_biggest_basins(self.input_data)
        print(size)
        self.assertion(899392 == size)
