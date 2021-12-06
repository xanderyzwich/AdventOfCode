"""
Day 4: Giant Squid
"""
from unittest import TestCase


class BingoCard:

    def __init__(self, list_of_rows):
        self.numbers = list_of_rows
        self.marks = [[False for _ in range(5)] for _ in range(5)]
        self.last_mark = None
        # print('Initializing board')
        # for row in self.numbers:
        #     print(row)

    def mark(self, number):
        found = False
        for row in range(5):
            for col in range(5):
                if number == self.numbers[row][col]:
                    self.marks[row][col] = True
                    self.last_mark = number
                    found = True
                    break
            if found:
                break
        return self.is_winner() if found else False

    def is_winner(self):
        sum_marks_per_col = [0 for _ in range(5)]
        for row in range(5):
            if self.marks[row] == [True for _ in range(5)]:
                return True
            for col in range(5):
                sum_marks_per_col[col] += 1 if self.marks[row][col] else 0
        return True if 5 in sum_marks_per_col else False

    def score(self):
        unmarked_sum = 0
        for row in range(5):
            for col in range(5):
                unmarked_sum += self.numbers[row][col] if not self.marks[row][col] else 0
        return unmarked_sum * self.last_mark

    def __repr__(self):
        return f'\tLast Mark: {self.last_mark}\n\tSum of unmarked: {self.score()/self.last_mark}\n\tScore: {self.score()} {self}'

    def __str__(self):
        representation = '\n'
        for row in range(5):
            representation += '\t'
            for col in range(5):
                representation += f'    x' if self.marks[row][col] else f'{self.numbers[row][col]:5}'
            representation += '\n'
        return representation


def parse_file(file_name):
    boards = []

    with open(file_name, 'r') as input_file:
        file_data = list(input_file)
        sequence = [int(n) for n in file_data[0].strip().split(',')]
        board = []

        for line in file_data[1:]:
            row = [int(element) for element in line.strip().split()]
            if 0 == len(row):
                continue
            board.append(row)
            if 5 == len(board):
                boards.append(BingoCard(board))
                board = []
    return sequence, boards


def play_bingo(sequence, cards):
    for n in sequence:
        for card in cards:
            if card.mark(n):
                return card.score()


def lose_at_bingo(sequence, cards):
    remaining_cards = cards
    for n in sequence:
        cards_to_keep = []
        for card in remaining_cards:
            if not card.mark(n):
                cards_to_keep.append(card)
            elif 1 == len(remaining_cards):
                return card.score()
        remaining_cards = cards_to_keep


class TestBingo(TestCase):
    example_data = parse_file('example.txt')
    input_data = parse_file('data.txt')

    @classmethod
    def setUpClass(cls) -> None:
        print(f'\nExecuting {cls.__name__}')

    def setUp(self) -> None:
        self.current_result = False
        print(f'\t Running {self._testMethodName}', end='\n\t\t')

    def assertion(self, test_passes) -> None:
        self.current_result = test_passes
        assert test_passes

    def tearDown(self) -> None:
        test_result = 'PASS' if self.current_result else 'FAIL'
        self.current_result = False
        print('\t\t' + test_result)

    def test_bingo_card(self):
        sequence, boards = self.example_data
        print('Sequence:', sequence)
        for board in boards:
            board.mark(13)
            print(board)
        self.assertion(boards)

    def test_one_example(self):
        score = play_bingo(*self.example_data)
        self.assertion(4512 == score)

    def test_one_data(self):
        score = play_bingo(*self.input_data)
        self.assertion(10374 == score)

    def test_two_example(self):
        score = lose_at_bingo(*self.example_data)
        self.assertion(1924 == score)

    def test_two_data(self):
        score = lose_at_bingo(*self.input_data)
        self.assertion(24742 == score)
