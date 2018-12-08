"""
Day 7: The Sum of Its Parts
https://adventofcode.com/2018/day/7
"""

import datetime as dt

def read_file(file = 'input.txt'):
    requirements = []
    with open(file,'r') as input_file:
        for line in input_file:
            pieces = line.split()
            requirements.append([pieces[1], pieces[7]])
    return requirements


def do_next(requirement_list, processed):
    columns = zip(*requirement_list)
    possible = []
    before, after = columns
    for point in before:
        if point not in after:
            possible.append(point)
    to_do = sorted(possible)[0]
    processed += to_do
    for item in sorted(requirement_list):
        if item[0] == to_do:
            if len(requirement_list) == 1:
                processed += item[1]
            requirement_list.remove(item)
    print('Doing', to_do, end=': ')
    return requirement_list, processed


def part1(requirements):
    processed = ''
    while len(requirements) > 0:
        requirements, processed = do_next(requirements, processed)
        print(processed, requirements)


if __name__ == '__main__':
    print('Starting... ')
    start = dt.datetime.now()
    requirements = read_file()
    part1(requirements)
    print('Part1 finished in', dt.datetime.now() - start)

