"""
Find entries without overlap
https://adventofcode.com/2018/day/3#part2
"""

import numpy as np
import re

fabric = np.zeros([1000, 1000])
not_overlapped = []


def mark(elf_id, x, y, width, height):
    overlapped = False
    for i in range(width):
        for j in range(height):
            value = fabric[x + i][y + j]
            if value == 0:
                fabric[x + i][y + j] = elf_id
            else:
                overlapped = True
                if value and value in not_overlapped:
                    not_overlapped.remove(value)
                fabric[x + i][y + j] = None
    if not overlapped:
        not_overlapped.append(elf_id)


def process_line(line):
    text = line.strip()
    for c in '@:x':
        text = text.replace(c, ',')
    trash, elf_id, x, y, width, height = re.split('\W+', text)
    return int(elf_id), int(x), int(y), int(width), int(height)


def main():
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            mark(*process_line(line))
        print(not_overlapped)


if __name__ == '__main__':
    main()

