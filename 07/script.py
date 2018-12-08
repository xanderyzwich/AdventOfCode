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


def get_task(requirement_list):
    columns = zip(*requirement_list)
    possible = []
    before, after = columns
    for point in before:
        if point not in after:
            possible.append(point)
    return sorted(possible)[0]


def perform_task(processed, requirement_list, task):
    processed += task
    for item in sorted(requirement_list):
        if item[0] == task:
            if len(requirement_list) == 1:
                processed += item[1]
            requirement_list.remove(item)
    return processed, requirement_list


def part1(requirements):
    processed = ''
    while len(requirements) > 0:
        to_do = get_task(requirements)
        processed, requirements = perform_task(processed, requirements, to_do)
        print(processed)


if __name__ == '__main__':
    print('Starting... ')
    start = dt.datetime.now()
    requirements = read_file()
    part1(requirements)
    print('Part1 finished in', dt.datetime.now() - start)

