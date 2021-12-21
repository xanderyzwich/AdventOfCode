"""
Day 17: Trick Shot
"""
from unittest import TestCase


class Probe:

    def __init__(self, x_max, x_min, y_max, y_min):
        self.x_max = x_max
        self.x_min = x_min
        self.y_max = y_max
        self.y_min = y_min

    def hits_target(self, x_velocity, y_velocity):
        x, y, step = 0, 0, 0
        velocity_x, velocity_y = x_velocity, y_velocity
        highest_points = []
        while x < self.x_max and y >= self.y_min:
            x += velocity_x
            y += velocity_y
            velocity_y -= 1
            if velocity_x > 0:
                velocity_x -= 1
            elif velocity_x < 0:
                velocity_x += 1
            highest_points.append(y)
            on_target_x = self.x_min <= x <= self.x_max
            on_target_y = self.y_min <= y <= self.y_max
            if on_target_x and on_target_y:
                return max(highest_points)
        return False

    def highest_trajectory(self):
        heights = []
        for x_val in range(1, self.x_max + 1):
            for y_val in range(self.y_min, 100):
                height = self.hits_target(x_val, y_val)
                if height is not False:
                    heights.append(height)
        return max(heights)

    def possible_trajectory_count(self):
        trajectories = []
        for x_val in range(1, self.x_max + 1):
            for y_val in range(self.y_min, 100):
                height = self.hits_target(x_val, y_val)
                if height is not False:
                    trajectories.append((x_val, y_val))
        return len(trajectories)


def thing(stuff):
    pass


def parse_file(file_name):
    data = {}
    with open(file_name, 'r') as input_file:
        for line in input_file:
            x_range, y_range = line.strip().replace('target area: ', '').split(', ')
            x_min, x_max = (int(x) for x in x_range.replace('x=', '').split('..'))
            y_min, y_max = (int(y) for y in y_range.replace('y=', '').split('..'))
            data = {
                'x_min': x_min,
                'x_max': x_max,
                'y_min': y_min,
                'y_max': y_max,
            }
    return data


class TestProbe(TestCase):
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

    def test_hits_target(self):
        probe = Probe(**self.example_data)
        height = probe.hits_target(6, 9)
        self.assertion(45 == height)

    def test_one_example(self):
        probe = Probe(**self.example_data)
        apex = probe.highest_trajectory()
        self.assertion(45 == apex)

    def test_one_data(self):
        probe = Probe(**self.input_data)
        apex = probe.highest_trajectory()
        self.assertion(2701 == apex)

    def test_two_example(self):
        probe = Probe(**self.example_data)
        count = probe.possible_trajectory_count()
        self.assertion(112 == count)

    def test_two_data(self):
        probe = Probe(**self.input_data)
        count = probe.possible_trajectory_count()
        self.assertion(1070 == count)
