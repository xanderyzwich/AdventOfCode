"""
Day 15: Rambunctious Recitation
"""
from unittest import TestCase


class MemoryGame:

    def __init__(self, start_set):
        self.turn = 1
        self.memory = {}
        for n in start_set[:-1]:
            self.memory[n] = self.turn
            self.turn += 1
        self.last_number = start_set[-1]
        # print(self)

    def play(self):
        if self.last_number in self.memory:
            value = self.turn - self.memory[self.last_number]
        else:
            value = 0
        # print('  Before play:', self.last_number, self.turn, value)
        self.memory[self.last_number] = self.turn
        self.last_number = value
        self.turn += 1
        # print('  After play: ', self.last_number, self.turn, value)

    def play_to(self, stop=2020):
        while self.turn < stop:
            self.play()
        print(self)

    def __str__(self):
        result = f'Last Number: {self.last_number} on turn: {self.turn}\t'
        # result += f'Current sequence state: {self.memory}'
        return result


class TestThing(TestCase):
    data = [16, 11, 15, 0, 1, 7]
    test_data = [
        {'arg': [0, 3, 6], 2020: 436, 30000000: 175594},
        {'arg': [1, 3, 2], 2020: 1, 30000000: 2578},
        {'arg': [2, 1, 3], 2020: 10, 30000000: 3544142},
        {'arg': [1, 2, 3], 2020: 27, 30000000: 261214},
        {'arg': [2, 3, 1], 2020: 78, 30000000: 6895259},
        {'arg': [3, 2, 1], 2020: 438, 30000000: 18},
        {'arg': [3, 1, 2], 2020: 1836, 30000000: 362}
    ]

    def test_one_example(self):
        end_turn = 2020
        for test in self.test_data:
            mg = MemoryGame(test['arg'])
            mg.play_to(end_turn)
            assert mg.last_number == test[end_turn]

    def test_one_data(self):
        mg = MemoryGame(self.data)
        mg.play_to()
        assert mg.last_number == 662

    def test_two_example(self):
        end_turn = 30000000
        for test in self.test_data:
            mg = MemoryGame(test['arg'])
            mg.play_to(end_turn)
            assert mg.last_number == test[end_turn]

    def test_two_data(self):
        mg = MemoryGame(self.data)
        mg.play_to(30000000)
        assert mg.last_number == 37312
