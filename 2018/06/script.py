"""
Chronal Coordinates
https://adventofcode.com/2018/day/6
"""

import re
import numpy as np
import datetime as dt


def read_input():
    locations = []
    with open('input.txt', 'r') as input_file:
        for label, line in enumerate(list(input_file)):
            x, y = re.split(', ', line)
            # print(label, ":", x, ',', y)
            locations.append([label, x, y])
    return locations


def manhattan_distance(point1, point2):
    """
    Find the distance between (x1, y1) and (x2, y2)
    """
    x1, y1, x2, y2 = map(int, [*point1, *point2])
    xo = x2 - x1 if x2 > x1 else x1 - x2
    yo = y2 - y1 if y2 > y1 else y1 - y2
    # print(xo, yo)
    return xo + yo


def minmax(locations_list):
    """
    Use to find the minimum and maximum values of x and y
    :param locations_list:
    :print: ranges of X and Y values
    """
    minx, miny, maxx, maxy = 5000, 5000, -5000, -5000
    for location, x, y in locations_list:
        location, x, y = map(int, [location, x, y])
        if x < minx:
            minx = x
        if y < miny:
            miny = y
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
    print('\t', 'X goes from', minx, 'to', maxx)
    print('\t', 'Y goes from', miny, 'to', maxy)


def part1_preprocess(locations):
    mymap = np.zeros([500, 500])
    counts = {}
    infinite = []
    for i in range(500):
        for j in range(500):
            distances = []
            closest, distance = 0, 0
            for name, x, y in locations:
                distances.append([name, manhattan_distance([i, j], [x, y])])
            distance_only = list(zip(*distances))[1]
            least = min(distance_only)
            if distance_only.count(least) == 1:
                winner = distances[distance_only.index(least)][0]
                mymap[i][j] = winner
                if i in (0, 499) or j in (0, 499):
                    infinite.append(winner)
                else:
                    if winner in counts.keys():
                        counts[winner] += 1
                    else:
                        counts[winner] = 1

    return mymap, counts, infinite


def part1_answer(counts, infinite):
    winner, most = 0, 0
    for key in counts.keys():
        total = counts.get(key)
        # print(key, total)
        if total > most and key not in infinite:
            winner, most = key, total
    print(winner, most)


def part2(locations):
    area = 0
    for i in range(500):
        for j in range(500):
            manhattan_sum = 0
            for name, x, y in locations:
                # x, y = str(int(x) + 350), str(int(y) + 350)
                manhattan_sum += manhattan_distance([i, j], [x, y])
            if manhattan_sum < 10000:
                area += 1
    print("Part2: Safe area is ", area)  # 42939


if __name__ == '__main__':

    print('Starting... ', end='')
    start = dt.datetime.now()
    locations = read_input()
    print('input read')

    # X goes from 44 to 313
    # Y goes from 25 to 342
    print('Used area of the map')
    minmax(locations)  # for planning and research

    """
    Do work for Part 1
    """
    map_data, counts, infinite = part1_preprocess(locations)
    print('map populated')
    part1_answer(counts, infinite)
    print('part1 complete at ', dt.datetime.now() - start)

    """
    Do work for Part 2
    """
    part2(locations)
    print('part2 complete at ', dt.datetime.now() - start)
