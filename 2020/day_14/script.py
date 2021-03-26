"""
Day 14: Docking Data
"""
import re
from unittest import TestCase
from itertools import product


def dec_to_bin(number, length=36):
    # print(number)
    return str(bin(int(number)))[2:].zfill(length)


def apply_mask(mask, number):
    number_string = dec_to_bin(number)
    result = ''
    for i in range(36):
        c = mask[i]
        result += c if c != 'X' else number_string[i]
    # print(f'{number_string}\n{mask}\n{result}')
    return bin_to_dec(result)

def bin_to_dec(number):
    return int(number, 2)


def part1(file_name):
    memory = {}
    mask = ''
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = line.replace('\n', '')
            if 'mask' in line:
                mask = re.split(r'( = )', clean)[2]
            else:
                data = re.split(r'mem\[|\] =', clean)[1:]
                # print(data)
                slot, value = data
                memory[slot] = apply_mask(mask, value)

    result = sum(memory.values())
    print(result)
    return result


def apply_mask_2(mask, number):
    number_string = dec_to_bin(number)
    result = ''
    for i in range(len(mask)):
        c = mask[i]
        if c == '0':
            result += number_string[i]
        elif c in ['1', 'X']:
            result += c
        else:
            print('sumtin dun borked')
    # print(f'{number_string}\n{mask}\n{result}')
    return result

def get_addresses(masked_addr):
    wild_values = []
    base = bin_to_dec(masked_addr.replace('X', '0'))
    for i in range(len(masked_addr)):
        char = masked_addr[-1-i]
        if char == 'X':
            wild_values.append(2**i)
    things = []
    for n in wild_values:
        things.append([0, n])
    # print(wild_values)
    # print(things)
    possibilities = sorted([base + sum(x) for x in list(product(*things))])
    # print(possibilities)
    return possibilities


def part2(file_name):
    memory = {}
    mask = ''
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = line.replace('\n', '')
            if 'mask' in line:
                mask = re.split(r'( = )', clean)[2]
            else:
                data = re.split(r'mem\[|\] =', clean)[1:]
                # print(data)
                slot, value = data
                addresses = get_addresses(apply_mask_2(mask, slot))
                for a in addresses:
                    memory[a] = int(value)
    result = sum(memory.values())
    print(result)
    return result



class TestThing(TestCase):

    def test_dev_one(self):
        tests = ['11', '101', '0']
        mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        for t in tests:
            result = apply_mask(mask, t)
            print(bin_to_dec(result))

    def test_one_example(self):
        assert part1('example_one.txt') == 165

    def test_one_data(self):
        assert part1('data.txt')

    def test_two_dev(self):
        result = apply_mask_2('000000000000000000000000000000X1001X', '42')
        assert result == '000000000000000000000000000000X1101X'
        assert get_addresses(result) == [26, 27, 58, 59]

        result = apply_mask_2('00000000000000000000000000000000X0XX', '26')
        get_addresses(result)

    def test_two_example(self):
        assert part2('example_two.txt') == 208

    def test_two_data(self):
        assert part2('data.txt')
