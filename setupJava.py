#!/usr/bin/env python3
"""
Setup the new day's directory and base files
"""
import datetime
import os
import re
import shutil
import sys
from getopt import getopt, GetoptError

language_extensions = {
    'python': '.py',
    'java': '.java',
}

if __name__ == '__main__':
    help_str = f'{__file__} -d <day_num>'
    help_str += f'\n{__file__} -y 2021 -d 2'

    argv = sys.argv[1:]
    # Default values
    date = datetime.datetime.now().date()
    year, day = str(date.year), date.day
    lang = 'java'

    try:
        opts, args = getopt(argv, "h:y:d:l:", ["help =", "year =", "day =", "lang ="])
    except GetoptError:
        print(help_str)
        sys.exit(2)

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
    PROJECT_ROOT = CURR_DIR
    current_contents = os.listdir()
    if year not in current_contents:
        os.mkdir(year)
        os.mkdir(f'year/data')
        os.mkdir(f'year/src')
        os.mkdir(f'year/test')
    os.chdir(year)

    day_name = f'Day{day}'
    data_files = [f'{day_name}-example.txt', f'{day_name}-data.txt']
    os.chdir(os.path.join(CURR_DIR, str(year), 'data'))
    contents = os.listdir()
    for file in data_files:
        if file not in contents:
            with open(file, 'a') as thing:
                pass

    source_roots = ['src', 'test']
    for d in source_roots:
        os.chdir(f'../{d}')
        destination_contents = os.listdir(os.getcwd())
        for name in destination_contents:
            file_name, file_extension = os.path.splitext(name)
            if file_name.endswith('X') and language_extensions[lang] == file_extension:
                destination_file_name = f'{day_name}{file_extension}' \
                    if d == 'src' \
                    else f'TestDay{day_name}{file_extension}'
                if destination_file_name not in destination_contents:
                    with open(name, 'r') as source_file, open(os.path.join(PROJECT_ROOT, year, d, destination_file_name), 'a') as output_file:
                        for line in source_file:
                            output_file.write(line.replace('ayX', f'ay{day}'))

    print(f'Good luck with day # {day}!')
    if day < 25:
        print(f'Only {25 - day} days left!')
    elif 25 == day:
        print('LAST DAY! Merry Christmas!')
    else:
        print('Isn\'t Advent Over?')
