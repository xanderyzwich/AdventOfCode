"""
Day 13: Shuttle Search
"""
from unittest import TestCase


def read_file(file_name):
    """
    Parse puzzle data from given file
    :param file_name: file to read
    :return want: The earliest timestampt you can depart
    :return bus_list: list of the bus id's
    """
    with open(file_name, 'r') as input_file:
        input_list = list(input_file)
        want = int(input_list[0])
        bus_list = input_list[1].split(',')
    # print(want, bus_list)
    return want, bus_list


def find_first_bus(target, bus_list):
    """
    Which bus will arrive first?
    :param target: earliest timestamp you can depart
    :param bus_list: list of bus id's
    :return my_bus: The first bus arriving after target
    :return first_arrival: number of mins between target and arrival
    """
    actual_bus_list = sorted([int(id) for id in bus_list if id != 'x'])
    wait_times = [b - (target % b) for b in actual_bus_list]
    # [print(x, y) for x, y in zip(bus_list, wait_times)]
    first_arrival = min(wait_times)
    my_bus = actual_bus_list[wait_times.index(first_arrival)]
    # print(my_bus, first_arrival)
    return my_bus, first_arrival


def part_1(file_name):
    bus, time = find_first_bus(*read_file(file_name))
    result = bus * time
    print(f'Part 1 w/ {file_name}: {result}')
    return result


def get_offset(bus_list):
    offset_list = {}
    for offset, bus in enumerate(bus_list):
        if bus != 'x':
            offset_list[int(bus)] = offset

    thing = sorted(map(list, offset_list.items()), key=lambda k: k[1])
    print(thing)
    return thing


def check_schedule(time, offset_list):
    # print(f'checking: {time}')
    for bus, offset in offset_list:
        if bus == 'x':
            continue
        work = (time + offset) % int(bus) == 0
        print(time + offset, bus, work)
        if not work:
            return False
    return True


def part_2(file_name):
    _, bus_list = read_file(file_name)
    offset_list = get_offset(bus_list)
    biggest_bus, biggest_offset = offset_list[0]

    check_num = biggest_bus - biggest_offset
    while True:
        # print(f'checking {check_num}')
        found, count = True, 0
        for bus, offset in offset_list[1:]:
            if not (check_num + offset) % int(bus) ==0:
                found = False
                break
        if found:
            return check_num
        if count > 0:
            print(f'{check_num}  {count}:{len(offset_list)-1}')
        check_num += biggest_bus


class TestThing(TestCase):

    def test_dev_steps(self):
        target, bus_list = read_file('example.txt')
        assert target == 939
        assert bus_list == ['7', '13', 'x', 'x', '59', 'x', '31', '19']
        bus, time = find_first_bus(target, bus_list)
        assert bus == 59
        assert time == 5

    def test_one_example(self):
        assert part_1('example.txt') == 295

    def test_one_data(self):
        assert part_1('data.txt') == 104

    def test_dev_steps_2(self):
        _, bus_list = read_file('example.txt')
        offset_list = get_offset(bus_list)
        assert check_schedule(1068781, offset_list)
        for bus, offset in offset_list:
            assert (1068781+offset) % bus == 0

    def test_two_example(self):
        expected = 1068781
        result = part_2('example.txt')
        print(result, expected)
        assert result == expected

    def test_two_data(self):
        assert part_2('data.txt')
