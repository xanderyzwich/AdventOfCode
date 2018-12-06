"""
Chronal Coordinates
https://adventofcode.com/2018/day/6
"""

import re
import numpy as np


def read_input():
    locations = {}
    with open('input.txt', 'r') as input_file:
        for label, line in enumerate(list(input_file)):
            x, y = re.split(', ', line[:-1])
            # print(label, ":", x, ',', y)
            locations[label] = x, y
    return locations


def populate_map(locations):
    mymap = np.zeros([500, 500])
    counts = {}
    infinite = []
    for i in range(500):
        for j in range(500):
            closest, distance = 0, 0
            for location in locations.keys():
                x, y = locations.get(location)
                far = manhattan_distance(i, j, int(x), int(y))
                if far < distance:
                    closest, distance = location, far
            mymap[i][j] = closest
            if closest in counts.keys():
                counts[closest] = counts.get(closest) + 1
            else:
                counts[closest] = 1
            if (i in (0, 499) or j in (0, 499)) \
                    and closest not in infinite:
                infinite.append(closest)
            # print('completed', i, j)
    # print(mymap)
    return mymap, counts, infinite


def answer_part1(counts, infinite):
    winner, most = 0, 0
    for key in counts.keys():
        total = counts.get(key)
        print(key, total)
        if total > most and key not in infinite:
            winner, most = key, total
    print(winner, most)


def manhattan_distance(x1, y1, x2, y2):
    xo = x2 - x1 if x2 > x1 else x1 - x2
    yo = y2 - y1 if y2 > y1 else y1 - y2
    # print(xo, yo)
    return xo + yo


if __name__ == '__main__':
    print('Starting')
    locations = read_input()
    print('input read')
    map_data, counts, infinite = populate_map(locations)
    print('map populated')
    answer_part1(counts, infinite)
    print('part1 complete')
