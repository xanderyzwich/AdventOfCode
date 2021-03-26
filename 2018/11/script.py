"""
Day 11: Chronal Charge
https://adventofcode.com/2018/day/11
"""

from datetime import datetime


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


def square_value(x, y, serial_number):
    return dynamic_square_value(x, y, serial_number, square_size)


def dynamic_square_value(x, y, serial_number, size):
    value = 0
    for i in range(size):
        for j in range(size):
            value += make_power_level(x + i, y + j, serial_number)
    return value


def max_square(serial_number, size):
    max_power, x, y = -300, -1, -1
    grid_stop = grid_size + 2 - size # 1 - 298 for checking squares size 3
    for i in range(1, grid_stop):
        for j in range(1, grid_stop):
            cell_power = dynamic_square_value(i, j, serial_number, size)
            if cell_power >= max_power:
                max_power, x, y = cell_power, i, j
    print('Size:', size, 'Power:', max_power, '@', str(x) + ',' + str(y))
    return max_power, x, y


def best_size(serial_number):
    high_max, high_x, high_y, high_size = -300, -1, -1, -1
    for size in range(1, grid_size):
        current_max, x, y = max_square(serial_number, size)
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
    #
    # # Square Demos
    # print('Grid Example 1 - Answer', square_value(33, 45, 18))
    # print('Grid Example 2 - Answer', square_value(21, 61, 42))
    #
    # # Grid Demos - Same input as Square Demos
    # max_square(18, square_size)
    # max_square(42, square_size)
    #
    # # Part1
    input_value = 9798
    start = datetime.now()
    print(max_square(input_value, square_size))
    print('Part1 complete in ', datetime.now()-start)

    # Best Square Demos
    # best_size(18)
    # best_size(42)

    # Part2
    start = datetime.now()
    print(best_size(input_value)[1:])
    print('Part2 complete in ', datetime.now() - start)
    # Size: 13 Power: 121 @ 235, 87
    # Answer = 235,87,13
    # Part2 complete in 0: 02:59.322725

