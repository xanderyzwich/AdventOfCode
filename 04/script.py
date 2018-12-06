"""
Guard sleep patterns
https://adventofcode.com/2018/day/4
"""

import re


class Record:
    """
    Used to consolidate events per night
    """
    def __init__(self):
        self.guard = None
        self.date = None
        self.sleep = {}

    def format_sleep(self):
        output = ''
        char = '.'
        for i in range(60):
            if i in self.sleep.keys():
                char = self.sleep[i]
            output += char
        return output

    def __str__(self):
        # output = str(self.guard) + '   \t' + str(self.date) + '   \t' # OUTPUT FOR PRETTY PRINT
        output = str(self.guard) + ' ' + str(self.date) + ' '
        return output + self.format_sleep()


def get_date(line):
    temp = re.split('\W+', line)[2:4]
    date = str(temp[0]) + '/' + str(temp[1])
    return date


def get_minute(line):
    return int(re.split('\W+', line)[5])


def parse_input():
    with open('input.txt', 'r') as input_file:
        input_set = sorted(list(input_file))
        output_set = []
        record = Record()
        for line in input_set:
            if 'Guard' in line:
                if record.guard:
                    output_set.append(str(record))
                    record = Record()
                record.guard = int(re.split('\W+', line)[7])
                record.date = get_date(line)
            if 'falls asleep' in line:
                record.sleep[get_minute(line)] = '#'
            if 'wakes up' in line:
                record.date = get_date(line)
                record.sleep[get_minute(line)] = '.'
        # for row in sorted(output_set):
        #     # data_file.write(make_entry(row))
        #     print(row)
        return sorted(output_set)


def sleep_add(old, new):
    sleep_output = []
    # print(old, '/n', new)
    for i, j in zip(old, new):
        sleep_output.append(int(i) + int(j))
    return sleep_output


def guard_summary(shift_data):
    guard_data = {}
    for line in shift_data:
        guard_id, date, sleep = re.split(' ', line)
        sleep = sleep.replace('.', '0').replace('#', '1')
        if guard_id in guard_data.keys():
            old = guard_data.get(guard_id)
            guard_data[guard_id] = sleep_add(old, sleep)
        else:
            guard_data[guard_id] = sleep

    return guard_data


def part1(schedule):
    winner, total = -1, -1
    for key, value in schedule.items():
        if sum(value) > total:
            winner, total, = key, sum(value)
    print('Part1 winner is ', winner, ' with ', total, end='')

    minute, count = -1, -1
    for time, value in enumerate(schedule.get(winner)):
        # print(time, value)
        if value > count:
            minute, count = time, value
    print(int(minute) * int(winner))


def part2(schedule):
    winner, highest = -1, -1
    for key, value in schedule.items():
        if max(value) > highest:
            winner, highest = key, max(value)

    minute =  -1
    for time, value in enumerate(schedule.get(winner)):
        if value == highest:
            minute = time

    print('Part2 winner is ', winner, ' with ', int(winner) * int(minute))

if __name__ == '__main__':
    shift_data = parse_input()
    schedules = guard_summary(shift_data)
    part1(schedules)
    part2(schedules)




