"""
Day 21: Dirac Dice
"""
from unittest import TestCase


class GameData:
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self, starting_positions):
        self.next_up = 1
        self.player_data = {}
        for p in [1, 2]:
            self.player_data[p] = {
                'position': starting_positions[p - 1],
                'score': 0,
                'wins': 0,
            }
        print(self)

    def copy(self):
        copy = GameData([0, 0])
        copy.next_up = self.next_up
        for p in [1, 2]:
            copy.player_data[p]['position'] = self.player_data[p]['position']
            copy.player_data[p]['score'] = self.player_data[p]['score']
            copy.player_data[p]['wins'] = self.player_data[p]['wins']
        return copy

    def increment_score(self, player, points):
        self.player_data[player]['score'] += points

    def get_score(self, player):
        return self.player_data[player]['score']

    def increment_position(self, player, distance):
        board_index = (distance + self.player_data[player]['position'] - 1) % 10
        board_position = self.board[board_index]
        self.player_data[player]['position'] = board_position
        self.increment_score(player, board_position)

    def get_position(self, player):
        return self.player_data[player]['position']

    def increment_wins(self, player, count):
        self.player_data[player]['wins'] += count

    def get_wins(self, player):
        return self.player_data[player]['wins']

    @property
    def next_player(self):
        result = self.next_up
        self.next_up = 2 if result == 1 else 1
        return result

    def __repr__(self):
        representation = f'\nNext Up: {self.next_up}\n'
        for p in [1, 2]:
            representation += f'Player {p}:\t'
            representation += f'Score: {self.player_data[p]["score"]}\t'
            representation += f'Position: {self.player_data[p]["position"]}\t'
            representation += f'Wins: {self.player_data[p]["wins"]}\n'
        return representation


class DeterministicDie:

    def __init__(self):
        self.next_value = 1
        self.roll_count = 0

    def roll(self):
        output = self.next_value
        self.next_value = 1 if self.next_value == 100 else self.next_value + 1
        self.roll_count += 1
        return output

    def roll_multiple(self, count=3):
        return sum([self.roll() for _ in range(count)])


def practice_game(player_data):
    game = GameData(player_data)
    dice = DeterministicDie()
    while True:
        player = game.next_player
        move = dice.roll_multiple(3)
        game.increment_position(player, move)
        print(game)
        if game.get_score(player) >= 1000:
            game.increment_wins(player, 1)
            break
    print(game)
    return dice.roll_count * min([game.get_score(p) for p in [1, 2]])


def dirac_game(game_data):
    game = game_data.copy()
    dice = [1, 2, 3]
    player = game.next_player
    for d in dice:
        next_game = game.copy()
        game.increment_position(player, d)

        if game.get_score(player) >= 1000:
            game.increment_score(player, 1)
        else:
            child_result = dirac_game(next_game)
            game.increment_wins(child_result.get_wins(1))
            game.increment_wins(child_result.get_wins(2))
    print(game)
    return game


def play_dirac_game(player_data):
    game = GameData(player_data)
    game = dirac_game(game)
    print(game)
    return max([game.get_wins(p) for p in [1, 2]])


def parse_file(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            start = int(line.strip()[-1])
            data.append(start)
    return data


class TestDiracDice(TestCase):
    example_data = parse_file('example.txt')
    input_data = parse_file('input.txt')

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

    def test_game(self):
        game = GameData(self.example_data)

        game.increment_position(1, 6)
        print(game)

    def test_one_example(self):
        result = practice_game(self.example_data)
        print(result)
        self.assertion(739785 == result)

    def test_one_data(self):
        result = practice_game(self.input_data)
        self.assertion(1067724 == result)

    def test_two_example(self):
        result = play_dirac_game(self.example_data)
        self.assertion(444356092776315 == result)

    def test_two_data(self):
        self.assertion(True)
