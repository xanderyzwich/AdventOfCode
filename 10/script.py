"""
Day 10: The Stars Align
https://adventofcode.com/2018/day/10
"""

import re
from datetime import datetime


class StarMap:
    def __init__(self, star_data):
        self.star_data = star_data
        self.offsets, radius = [], 3
        for i in range(-radius, radius + 1):
            for j in range(-radius, radius + 1):
                self.offsets.append((i, j))

    def star_map(self, second):
        x_data = []
        y_data = []

        for x, y, i, j in self.star_data:
            if second == 0:
                x_data.append(x)
                y_data.append(y)
            else:
                x_data.append(x + (i * second))
                y_data.append(y + (j * second))
        return x_data, y_data


    def area(self, second):
        minx, maxx, miny, maxy = self.minmax(second)
        return (maxx - minx) * (maxy - miny)


    def focus(self):
        area_tracker = 99999999999999999
        i = 1
        while True:
            # print('Checking second', i)
            temp = self.area(i)
            if temp <= area_tracker:
                area_tracker = temp
            else:
                return i - 1
            i += 1

    def minmax(self, second):
        x_set, y_set = self.star_map(second)
        minx = min(x_set)
        maxx = max(x_set)
        miny = min(y_set)
        maxy = max(y_set)
        return minx, maxx, miny, maxy

    def window(self, second):
        minx, maxx, miny, maxy = self.minmax(second)
        return maxx - minx, maxy - miny

    def display(self, second):
        minx, maxx, miny, maxy = self.minmax(second)
        x, y = self.star_map(second)
        for j in range(miny, maxy + 1):
            s = ''
            for i in range(minx, maxx + 1):
                if (i, j) in zip(x, y):
                    s += '#'
                else:
                    s += ' '
            print(s)


def read_input(input_file):
    input_data = []
    with open(input_file, 'r') as read_data:
        for line in read_data:
            clean_data = line.strip().replace('velocity', ',')
            for piece in ('position', '<', '>', '=', ' '):
                clean_data = clean_data.replace(piece, '')
            # print(re.split(',', clean_data))
            x, y, i, j = map(int, re.split(',', clean_data))
            # print(x, y, i, j)
            input_data.append((x, y, i, j))
    return input_data


if __name__ == '__main__':
    print('Starting')
    data_vector = read_input('input.txt')
    print('Input received')
    starry_night = StarMap(data_vector)
    print('StarMap Created')
    focus_point = starry_night.focus()
    print('focus point found')
    starry_night.display(focus_point)
    print('Message found at', focus_point)




