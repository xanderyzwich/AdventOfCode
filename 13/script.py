"""
Day 13: Mine Cart Madness
https://adventofcode.com/2018/day/13
"""

up, down, left, right = '^', 'v', '<', '>'
directions = up + left + down + right
cars = {}


def read_input(file_name):
    map = []
    with open(file_name, 'r') as input_file:
        map_list = list(input_file)
    max_length = 0
    for row in map_list:  # find longest row length
        row_length = len(row.replace('\n', ''))
        if row_length > max_length:
            max_length = row_length
    for row in map_list:  # put rows into map
        row_list = list(row.replace('\n', ''))
        row = row.strip()
        if len(row) < max_length:
            while len(row) < max_length:
                row += ' '
        # print(len(row_list))
        map.append(row_list)
    return map


def process_map(map):
    above, current, below = None, None, None
    for i in range(len(map)):
        above, current, below = current, below, map[i]
        if not current:
            continue
        for char in directions:  # for each of up, down, left, and right
            if char in current:  # check if it occurs in the current line
                above, current, below = process_row([above, current, below])


def process_row(row_set, i):
    above, current, below = row_set
    for j in range(len(current)):
        old_car = current[j]
        if old_car in directions:
            x, y = where_to(row_set, j)
            next_rail = row_set[x][y]
            car = new_car(next_rail, old_car)
            if next_rail == '+':
                # TODO : check if car is in cars
                car = decide(i, j, old_car)
            row_set[x][y] = car
            # TODO : put rail back after move
    return [above, current, below]


def where_to(row_set, i):  # Get destination x,y
    char = row_set[1][i]
    if char == up:
        destination = [0, i]
    elif char == left:
        destination = [1, i - 1]
    elif char == right:
        destination = [1, i + 1]
    elif char == down:
        destination = [2, i]
    else:
        destination = [-1, -1]  # ERROR
    return destination


def new_car(destination_rail, current_car):  # Which way should the car point after the move
    if destination_rail in '|-':
        return current_car
    elif destination_rail == '/':
        if current_car in up + down:
            return turn(current_car, right)
        else:
            return turn(current_car, left)
    elif destination_rail == '\\':
        if current_car in left + right:
            return turn(current_car, right)
        else:
            return turn(current_car, left)
    else:
        return 'O'


def turn(car, direction):  # turn the car right/left/straight
    if direction == 'straight':
        return car
    else:
        index = directions.index(car)
        if direction == 'left':
            return directions[index + 1 % len(directions)]
        if direction == 'right':
            return directions[index - 1 % len(directions)]
    return 'O'


if __name__ == '__main__':
    map = read_input('simple.txt')
    # map = read_input('example.txt')
    # map = read_input('input.txt')
