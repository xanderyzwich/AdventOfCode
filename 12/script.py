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
                initial_string = line.split(' ')[2]
                # print(initial_string)
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


def total(offset, data):
    sum = 0
    for i in range(len(data)):
        if data[i] == '#':
            sum += i - offset
    return sum


def next_gen(offset, data, rules):
    section, next = '', ''
    if data.startswith('#'):
        data = '..' + data
        offset += 2
    elif data.startswith('.#'):
        data = '.' + data
        offset += 1
    if data.endswith('#'):
        data = data + '..'
    elif data.endswith('#.'):
        data = data + '.'
    for i in range(0, len(data)):
        start, end = i - 2, i + 3
        if i == 0:
            section = '..'
            section += data[0:end]
            # offset += 2
        elif i == 1:
            section = '.'
            section += data[0:end]
            # offset += 1
        elif i == len(data) - 1:
            section = data[start:len(data)]
            section += '..'
        elif i == len(data) - 2:
            section = data[start:len(data)]
            section += '.'
        else:
            section = data[start:end]
        # print(i, section, next)
        next += rules[section]
    offset, next = trim_front(offset, next)
    next = trim_back(next)
    return offset, next


def trim_front(offset, data):
    if data.startswith('.'):
        data = data[1:]
        offset -= 1
        # print('start')
    else:
        return offset, data
    return trim_front(offset, data)


def trim_back(data):
    if data.endswith('.'):
        # print('ends')
        data = data[:len(data) - 1]
    else:
        return data
    return trim_back(data)


if __name__ == '__main__':
    # data, rules = read_data('demo.txt')
    data, rules = read_data('input.txt')
    offset = 0
    rules = rules_check(rules)
    # offset, data = -2, 'mn0123456789'
    # print('0', data)
    for i in range(1, 21):
        offset, data = next_gen(offset, data, rules)
        # print(i, data, 'offset =', offset)
    print('After 20 generations:', total(offset, data))
    for i in range(21, 50000000000 + 1):
        last_data, last_offset = data, offset
        offset, data = next_gen(offset, data, rules)
        # print(i, data, 'offset =', offset)
        if last_data == data:
            delta = offset - last_offset
            future = offset + ((50000000000 - i) * delta)
            offset = future
            break
        # if i % 1000 == 0:
        #     print(i % 1000, end='-')
    print('After 50000000000 generations:', total(offset, data))
