"""
Day 12: Passage Pathing
"""
from unittest import TestCase


def find_paths_no_small_revisit(route_map, visited=[], start='start'):

    is_small = start == start.lower()
    have_visited = start in visited
    if have_visited and is_small:
        return []

    now_visited = [*visited, start]
    if 'end' == start:
        return [now_visited]

    next_destinations = route_map[start]
    results = []
    for place in next_destinations:
        routes = find_paths_no_small_revisit(route_map, now_visited, place)
        results.extend(routes)
    return results


def find_paths_single_small_revisit(route_map, visited=[], start='start', small_doubled=False):
    have_visited = start in visited
    is_start = 'start' == start
    if have_visited and is_start:
        return []

    is_small = start == start.lower()
    small_and_visited = have_visited and is_small
    if small_and_visited and small_doubled:
        return []
    now_small_doubled = small_doubled or small_and_visited

    now_visited = [*visited, start]
    if 'end' == start:
        return [now_visited]

    next_destinations = route_map[start]
    results = []
    for place in next_destinations:
        routes = find_paths_single_small_revisit(route_map,
                                                 visited=now_visited,
                                                 start=place,
                                                 small_doubled=now_small_doubled)
        results.extend(routes)
    return results


def parse_file(file_name):
    data = {}
    with open(file_name, 'r') as input_file:
        for line in input_file:
            source, destination = line.strip().split('-')
            if source in data:
                data[source].append(destination)
            else:
                data[source] = [destination]
            if destination in data:
                data[destination].append(source)
            else:
                data[destination] = [source]
    # print(f'Data for {file_name}')
    # for key, value in data.items():
    #     print(f'\t{key}: {value}')
    return data


class TestThing(TestCase):
    example_one = parse_file('example1.txt')
    example_two = parse_file('example2.txt')
    example_three = parse_file('example3.txt')
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
        routes = find_paths_no_small_revisit(self.example_one)
        self.assertion(10 == len(routes))

        routes = find_paths_no_small_revisit(self.example_two)
        self.assertion(19 == len(routes))

        routes = find_paths_no_small_revisit(self.example_three)
        self.assertion(226 == len(routes))

    def test_one_data(self):
        routes = find_paths_no_small_revisit(self.input_data)
        # print(len(routes))
        self.assertion(3576 == len(routes))

    def test_two_example(self):
        count = len(find_paths_single_small_revisit(self.example_one))
        self.assertion(36 == count)
        count = len(find_paths_single_small_revisit(self.example_two))
        self.assertion(103 == count)
        count = len(find_paths_single_small_revisit(self.example_three))
        self.assertion(3509 == count)

    def test_two_data(self):
        count = len(find_paths_single_small_revisit(self.input_data))
        self.assertion(84271 == count)
