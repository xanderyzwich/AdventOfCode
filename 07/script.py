"""
Day 7: The Sum of Its Parts
https://adventofcode.com/2018/day/7
"""

import datetime as dt

idle = '.'
workers = 5
base_seconds = 60

def read_file(file = 'input.txt'):
    requirements = []
    with open(file,'r') as input_file:
        for line in input_file:
            pieces = line.split()
            requirements.append([pieces[1], pieces[7]])
    return requirements


def remove_dups(group):
    dedup = []
    for item in group:
        if item not in dedup:
            dedup.append(item)
    return sorted(dedup)

def get_tasks(requirement_list):
    columns = zip(*requirement_list)
    possible = []
    before, after = columns
    for point in before:
        if point not in after:
            possible.append(point)
    return remove_dups(possible)


def perform_task(processed, requirement_list, task):
    processed += task
    for item in sorted(requirement_list):
        if item[0] == task:
            if len(requirement_list) == 1 and item[1] != '':
                blank = [item[1], '']
                # processed += item[1]
                requirement_list.append(blank)
            requirement_list.remove(item)

    return processed, requirement_list


def part1(requirements):
    processed = ''
    while len(requirements) > 0:
        to_do = get_tasks(requirements)[0]
        processed, requirements = perform_task(processed, requirements, to_do)
    print(processed)


def valuate(character):
    return ord(character) - 96 + 32 + base_seconds


def tick(work, seconds, requirements):
    processed = ''
    for id, task, time in work:
        if time <= seconds:
            if task != idle:
                finished, requirements = perform_task(processed, requirements, task)
                processed += finished
                index = work.index((id, task, time))
                work.pop(index)
                record = (id, idle, time)
                work.insert(index, record)
                task = idle
            if task == idle and len(requirements) > 0:
                tasks = get_tasks(requirements)
                for item in sorted(tasks):
                    if item not in list(zip(*work))[1]:
                        if time > seconds:
                            continue
                        index = work.index((id, task, time))
                        work.pop(index)
                        id, task, time = (id, item, seconds + valuate(item))
                        work.insert(index, (id, task, time))
    return work, processed, requirements


def part2(requirements):
    work = []
    for id in range(workers):  # initialize workers as idle
        work.append((id, idle, 0))
    seconds = 0
    processed = ''
    while len(requirements) >= 1:
        work, finished, requirements = tick(work, seconds, requirements)
        processed += finished
        # print(seconds, end='')
        # for worker in work:
        #     print('\t', worker[1], end='')
        # print('\t', processed)
        if len(requirements) != 0:
            seconds += 1
    print(seconds - 1, processed)



if __name__ == '__main__':
    print('Starting part1 ', end=', Answer:  ')
    start = dt.datetime.now()
    requirements = read_file()
    part1(requirements)
    print('finished in', dt.datetime.now() - start)

    print('Starting part2 ')  #, end=', Answer:  ')
    start = dt.datetime.now()
    part2(read_file())
    print('finished in', dt.datetime.now() - start)

    # sum = 0
    # sequence = 'CABDFE'
    # for c in sequence:
    #     sum += valuate(c)
    # print(sum, sum - len(sequence))

