"""
Frequency adjustments
https://adventofcode.com/2018/day/1
"""

if __name__ == '__main__':
    total = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            if line.startswith('+'):
                total += int(line[1:])
            elif line.startswith('-'):
                total -= int(line[1:])
            else:
                print('unexpected line start character')
    print(total)

