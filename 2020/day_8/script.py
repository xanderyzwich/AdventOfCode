"""
Day 8: Handheld Halting
"""
from unittest import TestCase


def get_instructions(file_name):
    instructions = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = line.replace('\n', '').split(' ')
            # print(clean[0], int(clean[1]))
            instructions.append((clean[0], int(clean[1])))
    return instructions


def run_part1(instructions):
    functions = {
        'acc': lambda x: (accumulator+x, next_op+1),
        'jmp': lambda x: (accumulator, next_op+x),
        'nop': lambda x: (accumulator, next_op+1)
    }

    accumulator, next_op = 0, 0
    visited = []
    while next_op not in visited:
        visited.append(next_op)  # don't forget where you've been
        op, v = instructions[next_op]
        # print(f'Current: {accumulator:5} {next_op:5} Instruction: {op:5} {v:5} ')
        accumulator, next_op = functions[op](v)
        if next_op >= len(instructions):
            break
    # print(accumulator, next_op, visited)
    return accumulator, next_op


def run_part2(instructions):
    ops = ['jmp', 'nop']  # options to swap
    for i in range(len(instructions)):
        test_instructions = instructions.copy()
        op, val = instructions[i]
        if op in ops:
            test_instructions[i] = ops[(ops.index(op)+1) % 2], val  # swap with other
            # print(test_instructions[i])
            acc, nex = run_part1(test_instructions)
            if nex >= len(instructions):
                print(f'returning {acc}')
                return acc
    print("reached end without solution")


class TestThing(TestCase):

    def setUp(self) -> None:
        print(f'In method: {self._testMethodName}')
        self.example_instructions = get_instructions('example.txt')
        self.data_instructions = get_instructions('data.txt')

    def test_one_example(self):
        acc_val, _ = run_part1(self.example_instructions)
        assert acc_val == 5

    def test_one_data(self):
        acc_val, _ = run_part1(self.data_instructions)
        assert acc_val == 1384

    def test_two_example(self):
        assert run_part2(self.example_instructions) == 8

    def test_two_data(self):
        assert run_part2(self.data_instructions) == 761
