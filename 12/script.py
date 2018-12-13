"""
Day 12: Subterranean Sustainability
https://adventofcode.com/2018/day/12
"""


def read_data(file_name):
    initial_string = ''
    rules = {}
    with open(file_name, 'r') as input_file:
        for line in input_file:
            line = line.replace('\n', '')
            if 'initial state' in line:
                initial_string = line
            elif line == '':
                pass
            else:
                key, value = line.split(' ')[0::2]  # ignore '=>' element
                rules[key] = value
    return initial_string, rules


def rules_check(rules):
    for i in range(2 ** 5):
        s = str(bin(i))[2:].zfill(5).replace('0', '.').replace('1', '#')
        # print(s, self.rules[s])
        if s not in rules.keys():
            rules[s] = '.'
            # print('inserting', s)
    return rules


def total(state):
    offset, data = state
    sum = 0
    for i in range(len(state)):
        if data[i] == '#':
            sum += i - offset
    return sum


if __name__ == '__main__':
    # state = read_data('demo.txt')
    data, rules = read_data('input.txt')
    rules = rules_check(rules)
    data = 'mn0123456789'
    print(data)
