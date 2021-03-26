"""
Day 5
"""


alphabet = 'abcdefghijklmnopqrstuvwxyz'


def neutralize(input_string):
    in_length = len(input_string)
    string_1 = input_string
    for char in alphabet:
        up, down = char.upper(), char.lower()
        # print(up, down, up + down, down + up)
        string_2 = string_1.replace(up + down, '')
        string_1 = string_2.replace(down + up, '')
    return int((in_length - len(string_1))/2), string_1


def fully_neutralize(string_in):
    replacements, string_1 = 1, string_in
    while replacements > 0:
        replacements, string_2 = neutralize(string_1)
        string_1 = string_2
    return string_1


def part1(string_in):
    string_out = fully_neutralize(string_in)
    print('Part1: ', len(string_in), ' - ', len(string_in) - len(string_out), ' = ', len(string_out))


def part2(string_in):
    winner, length = ' ', len(string_in)
    for char in alphabet:
        string_less =string_in.replace(char, '').replace(char.upper(), '')
        string_out = fully_neutralize(string_less)
        final = len(string_out)
        if final < length:
            winner, length = char, final
    print('Part2:', winner, 'results in length of', length)


if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        string_in = list(input_file)[0]
    part1(string_in)
    part2(string_in)

