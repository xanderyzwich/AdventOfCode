#!/usr/bin/env python3
"""
Setup the new day's directory and base files
"""
import datetime
import os
import shutil
import sys
from getopt import getopt, GetoptError

if __name__ == '__main__':
    help_str = f'{__file__} -d <day_num>'
    help_str += f'\n{__file__} -y 2021 -d 2'
    argv = sys.argv[1:]
    date = datetime.datetime.now().date()
    year, day = str(date.year), date.day

    try:
        opts, args = getopt(argv, "h:y:d:l:", ["help =", "year =", "day =", "lang ="])
    except GetoptError:
        print(help_str)
        sys.exit(2)

    print(f'OPTS= {opts}')
    print(f'ARGS= {args}')
    for opt, arg in opts:
        if opt in ['-h', '--help']:
            print(help_str)
            sys.exit()
        elif opt in ['-d', '--day']:
            day = int(arg)
            print(f'day = {day}')
        elif opt in ['-y', '--year']:
            year = str(arg)
            print(f'year = {year}')

    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    current_contents = os.listdir()
    if year not in current_contents:
        os.mkdir(year)

    day_name = f'day_{day}'
    dir_name = os.path.join(CURR_DIR, str(year), day_name)
    print(dir_name)
    contents = os.listdir(year)
    if day_name not in contents:
        os.mkdir(dir_name)

    destination_contents = os.listdir(dir_name)
    print(destination_contents)
    for name in current_contents:
        file_name, file_extension = os.path.splitext(name)
        if 'format' == file_name:
            destination_file_name = f'script{file_extension}'
            # print(file_extension)
            if destination_file_name not in destination_contents:
                shutil.copy(name, os.path.join(dir_name, destination_file_name))

    os.chdir(dir_name)
    contents = os.listdir()
    data_files = ['example.txt', 'data.txt']
    for file in data_files:
        if file not in contents:
            with open(file, 'a') as thing:
                pass

    print(f'Good luck with day # {day}!')
    if day < 25:
        print(f'Only {25-day} days left!')
