"""
Find overlap of defined shapes
https://adventofcode.com/2018/day/3
"""

import numpy as np
import re

fabric = np.zeros([1000, 1000])


def mark(x, y, width, height):
    for i in range(width):
        for j in range(height):
            fabric[x + i][y + j] += 1


def find_overlap():
    overlap = 0
    for row in fabric:
        for cell in row:
            if cell > 1:
                overlap += 1
    return overlap


def process_line(line):
    text = line.strip()
    for c in '@:x':
        text = text.replace(c, ',')
    trash, elf_id, x, y, width, height = re.split('\W+', text)
    return int(x), int(y), int(width), int(height)


def main():
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            mark(*process_line(line))
    print(find_overlap())


if __name__ == '__main__':
    main()

