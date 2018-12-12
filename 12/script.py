"""
Day 12: Subterranean Sustainability
https://adventofcode.com/2018/day/12
"""


class State:
    def __init__(self, init_string, rules):
        self.offset = 0
        self.state = list(init_string.split(' ')[2])
        print(''.join(self.state))
        self.rules = rules
        self.generation = 0
        self.sum = self.total()
        self.rules_check()

    def step(self):
        current_state = ['.', '.'] + self.state + ['.', '.', '.']
        next_state = ['.', '.']
        self.offset += 2
        self.generation += 1
        for i in range(2, len(current_state) - 2):
            influence = ''.join(current_state[i - 2:i + 3])
            if influence in self.rules.keys():
                next_state.append(self.rules[influence])
            else:
                print("--------------IT BROKE-----------------", influence)

        self.state = next_state
        self.sum = self.total()
        return self.sum

    def total(self):
        sum = 0
        for i in range(len(self.state)):
            if self.state[i] == '#':
                sum += i - self.offset
        return sum

    def clean(self):
        while self.state[0] == '.' and self.offset > 2:
            self.state.pop(0)
            self.offset -= 1
        while self.state[-1] == '.':
            self.state.pop(len(self.state) - 1)

    def __str__(self):
        s = str(self.generation) + ' : ' + str(self.offset) + ' : ' + str(self.sum) + ' : ' + ''.join(self.state)
        return s

    def rules_check(self):
        for i in range(2 ** 5):
            s = str(bin(i))[2:].zfill(5).replace('0', '.').replace('1', '#')
            # print(s, self.rules[s])
            if s not in self.rules.keys():
                self.rules[s] = '.'
                # print('inserting', s)


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
    return State(initial_string, rules)


if __name__ == '__main__':
    # state = read_data('demo.txt')
    state = read_data('input.txt')
    print(state)
    for i in range(20):
        state.step()
        print(state)
