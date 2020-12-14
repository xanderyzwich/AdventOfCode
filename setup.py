"""
Setup the new day's directory and base files
"""
import os
import shutil
import sys
from getopt import getopt, GetoptError

if __name__ == '__main__':
    help_str = 'setup.py -d <day_num>'
    argv = sys.argv[1:]

    try:
        opts, args = getopt(argv, "h:d:l:", ["help =", "day =", "lang ="])
    except GetoptError:
        print(help_str)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ['-h', '--help']:
            print(help_str)
            sys.exit()
        elif opt in ['-d', '--day']:
            day = int(arg)

    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    dir_name = f'day_{day}'
    contents = os.listdir()
    if dir_name not in contents:
        os.mkdir(dir_name)
    destination_contents = os.listdir(dir_name)
    for name in contents:
        file_name, file_extension = os.path.splitext(name)
        if 'format' == file_name:
            destination_file_name = f'script.{file_extension}'
            if destination_file_name not in destination_contents:
                shutil.copy(name, f'{dir_name}/{destination_file_name}')

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
