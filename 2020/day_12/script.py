"""
Day 12: Rain Risk
"""
from unittest import TestCase


class Ship:

    bearings = ['N', 'E', 'S', 'W']

    def __init__(self):
        self.north = 0
        self.east = 0
        self._bearing = 1  # East

    def act(self, action, value):
        actions = {
            'R': lambda v: self.rotate(v),
            'L': lambda v: self.rotate(-v),
            'F': lambda v: self.act(self.facing, v),
            'S': lambda v: self.act('N', -v),
            'W': lambda v: self.act('E', -v)
        }
        if action == 'N':
            self.north += value
        elif action == 'E':
            self.east += value
        else:
            return actions[action](value)

    def rotate(self, degrees_right):
        clicks = degrees_right // 90
        self._bearing = (self._bearing + clicks) % 4

    @property
    def facing(self):
        return self.bearings[self._bearing]

    @property
    def odometer(self):
        return abs(self.north) + abs(self.east)


class WaypointShip(Ship):

    def __init__(self):
        self.waypoint_east = 10
        self.waypoint_north = 1
        self.east = 0
        self.north = 0

    def act(self, action, value):
        if action == 'N':
            self.waypoint_north += value
        elif action == 'S':
            self.waypoint_north -= value
        elif action == 'E':
            self.waypoint_east += value
        elif action == 'W':
            self.waypoint_east -= value
        elif action == 'F':
            self.north += self.waypoint_north * value
            self.east += self.waypoint_east * value
        else:
            self.rotate_waypoint(action, value)

    def rotate_waypoint(self, action, value):
        clicks = (value // 90) % 4
        if action == 'L' and clicks%2 == 1:
            clicks = (clicks + 2) % 4
        if clicks == 0:
            pass
        if clicks == 1:
            north = self.waypoint_north
            east = self.waypoint_east
            self.waypoint_east = north
            self.waypoint_north = -east

        elif clicks == 2:
            self.waypoint_east *= -1
            self.waypoint_north *= -1
        elif clicks == 3:
            north = self.waypoint_north
            east = self.waypoint_east
            self.waypoint_east = -north
            self.waypoint_north = east

    def __str__(self):
        temp = f'Ship:  ({self.east}, {self.north}) && Waypoint: ({self.waypoint_east}, {self.waypoint_north})'
        return temp



def part1(file_name):
    ship = Ship()
    with open(file_name, 'r') as input_file:
        for line in input_file:
            action = line[0]
            value = int(line[1:])
            ship.act(action, value)
    print(ship.odometer)
    return ship.odometer


def part2(file_name):
    ship = WaypointShip()
    # print(ship)
    with open(file_name, 'r') as input_file:
        for line in input_file:
            action = line[0]
            value = int(line[1:])
            ship.act(action, value)
            # print(ship)
    print(ship.odometer)
    return ship.odometer


class TestThing(TestCase):

    def test_ship(self):
        ship = Ship()
        ship.act('R', 90)
        assert ship.facing == 'S'
        ship.rotate(180)
        assert ship.facing == 'N'

    def test_one_example(self):
        assert part1('example.txt') == 25

    def test_one_data(self):
        assert part1('data.txt') == 923

    def test_waypoint_ship(self):
        ship = WaypointShip()
        print(ship)
        ship.act('R', 180)
        print(ship)
        assert ship.waypoint_east == -10
        assert ship.waypoint_north == -1

    def test_two_example(self):
        assert part2('example.txt') == 286

    def test_two_data(self):
        assert part2('data.txt') == 24769
