"""
Trying to make a faster solution
Day 11: Chronal Charge
https://adventofcode.com/2018/day/11

further performance can be gained with this
https://en.wikipedia.org/wiki/Summed-area_table
"""

from datetime import datetime

import numpy as np

grid_size = 300
square_size = 3


def make_rack_id(x):
    return x + 10


def make_power_level(x, y, serial_number):
    rack_id = make_rack_id(x)
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_string = str(power_level)
    if len(power_string) >= 3:
        power_level = int(power_string[-3])
    else:
        power_level = 0
    power_level -= 5
    # print(power_string, power_level)
    return power_level


def make_power_grid(serial_number):
    power_grid = np.zeros((grid_size + 1, grid_size+ 1))
    for i in range(1, grid_size + 1):
        for j in range(1, grid_size +1):
            power_grid[i][j] = make_power_level(i, j, serial_number)
    return power_grid


def square_value(x, y, serial_number):
    power_grid = make_power_grid(serial_number)
    return dynamic_square_value(x, y, power_grid, square_size)


def dynamic_square_value(x, y, power_grid, size):
    minx = x
    maxx = x + size
    miny = y
    maxy = y + size
    value = power_grid[minx:maxx, miny:maxy].sum()
    # print('Grid being checked', minx, maxx, miny, maxy)
    return value


def max_square(power_grid, size):
    max_power, x, y = -300, -1, -1
    grid_stop = grid_size + 2 - size  # 1 - 298 for checking squares size 3
    for i in range(1, grid_stop):
        for j in range(1, grid_stop):
            cell_power = dynamic_square_value(i, j, power_grid, size)
            if cell_power >= max_power:
                max_power, x, y = cell_power, i, j
    # print('Size:', size, 'Power:', max_power, '@', str(x) + ',' + str(y))
    return max_power, x, y


def best_size(serial_number):
    high_max, high_x, high_y, high_size = -300, -1, -1, -1
    power_grid = make_power_grid(serial_number)
    for size in range(2, grid_size):
        current_max, x, y = max_square(power_grid, size)
        if current_max > high_max:
            high_max, high_x, high_y, high_size = current_max, x, y, size
        elif current_max < high_max * 0.75:
            break
    print('Power:', high_max, '@', str(high_x) + ',' + str(high_y) + ',' + str(high_size))
    return high_max, high_x, high_y, high_size



if __name__ == '__main__':
    # # Examples
    # print('Example 0 - Answer', make_power_level(3, 5, 8))
    # print('Example 1 - Answer', make_power_level(122, 79, 57))
    # print('Example 2 - Answer', make_power_level(217, 196, 39))
    # print('Example 3 - Answer', make_power_level(101, 153, 71))

    # # Square Demos
    # print('Grid Example 1 - Answer', dynamic_square_value(33, 45, make_power_grid(18), square_size))
    # print('Grid Example 2 - Answer', dynamic_square_value(21, 61, make_power_grid(42), square_size))

    # # # Grid Demos - Same input as Square Demos
    # max_square(make_power_grid(18), square_size)
    # max_square(make_power_grid(42), square_size)

    # # Part1
    input_value = 9798
    start = datetime.now()
    print(max_square(make_power_grid(input_value), square_size)[1:])
    print('Part1 complete in ', datetime.now()-start)
    # Part1 complete in 0: 00:00.686413


    # Best Square Demos
    # best_size(18)
    # best_size(42)

    # Part2
    # Answer from other script = 235,87,13
    start = datetime.now()
    print(best_size(input_value)[1:])
    print('Part2 complete in ', datetime.now() - start)
    # Part2 complete in 0: 00:14.777728

