"""
Day X: Name
"""
from unittest import TestCase


class SeatMap:
    states = {
        'floor': '.',
        'empty': 'L',
        'occupied': '#'
    }

    rules = {
        'L': lambda x: '#' if x == 0 else 'L',
        '#': lambda x: 'L' if x >= 4 else '#',
        '.': lambda x: '.'
    }

    def __init__(self, file_name):
        self.grid = []
        with open(file_name, 'r') as input_file:
            for line in input_file:
                grid_line = []
                for char in line.replace('\n', ''):
                    grid_line.append(char)
                self.grid.append(grid_line)
        self.ticks = 0

    def is_state(self, row, col, state):
        """
        return whether the position is in the given state
        :param row: 0 indexed grid position
        :param col: 0 indexed grid position
        :param state: 'floor', 'empty', or 'occupied'
        :return:
        """
        return self.grid[row][col] == self.states[state]

    def apply_rules(self):
        next_map = []
        changed = False
        for row in range(len(self.grid)):
            map_row = []
            for col in range(len(self.grid[row])):
                current_value = self.grid[row][col]
                count_adjacent = self.adjacent_occupied(row, col)
                next_value = self.rules[current_value](count_adjacent)
                map_row.append(next_value)
                if next_value != current_value:
                    changed = True
            next_map.append(map_row)
        if changed:
            self.ticks += 1
            self.grid = next_map.copy()
        # print(self.ticks)
        return changed

    def adjacent_occupied(self, row, col):
        count = 0
        for r in [x for x in [row - 1, row, row + 1] if 0 <= x < len(self.grid)]:
            for c in [x for x in [col - 1, col, col + 1] if 0 <= x < len(self.grid[row])]:
                if r == row and c == col:
                    continue
                count += 1 if self.grid[r][c] == '#' else 0
        return count

    def total_occupied(self):
        count = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                count += 1 if self.grid[row][col] == '#' else 0
        return count

    def __str__(self):
        temp = ''
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                temp += self.grid[row][col] + ' '
            temp += '\n'
        return temp

    def __eq__(self, other):
        same_rows = len(self.grid) == len(other.grid)
        same_cols = len(self.grid[0]) == len(other.grid[0])
        same_vals = True
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] != other.grid[row][col]:
                    same_vals = False
        # print([same_rows, same_cols, same_vals])
        return all([same_rows, same_cols, same_vals])


class ImprovedSeatMap(SeatMap):
    rules = {
        'L': lambda x: '#' if x == 0 else 'L',
        '#': lambda x: 'L' if x >= 5 else '#',
        '.': lambda x: '.'
    }

    def adjacent_occupied(self, row, col):
        directions = (
            (-1, -1),  # top left diag
            (-1, 0),  # up
            (-1, 1),  # top right diag
            (0, 1),  # right
            (1, 1),  # low right diag
            (1, 0),  # down
            (1, -1),  # low left diag
            (0, -1)  # left
        )
        # print('checking point', row, col)
        return sum([self.follow((row, col), d) for d in directions])

    def follow(self, point, direction):
        cursor_row, cursor_col = point
        direction_row, direction_col = direction
        count = 0
        cursor_row += direction_row
        cursor_col += direction_col
        # print('checking', point)
        while (cursor_row, cursor_col) in self:
            char = self.grid[cursor_row][cursor_col]
            # print(cursor_row, cursor_col, char)
            if char == '#':
                count += 1
                break
            elif char == 'L':
                break
            cursor_row += direction_row
            cursor_col += direction_col
        return count

    def __contains__(self, item):
        row, col = item
        result = (0 <= row < len(self.grid)) and (0 <= col < len(self.grid[row]))
        # print(result, row, col)
        return result

    @staticmethod
    def get_distance(x1, y1, x2, y2):
        x = x1 - x2 if x1 >= x2 else x2 - x1
        y = y1 - y2 if y1 >= y2 else y2 - y1
        return x if x >= y else y


def part1(file_name):
    seat_map = SeatMap(file_name)
    changed = True
    while changed:
        # print(seat_map)
        changed = seat_map.apply_rules()
    print(seat_map.total_occupied())
    return seat_map.total_occupied()


def part2(file_name):
    seat_map = ImprovedSeatMap(file_name)
    changed = True
    while changed:
        # print(seat_map.ticks, "ticks and counting")
        # print(seat_map)
        changed = seat_map.apply_rules()
    print("occupied count=", seat_map.total_occupied())
    return seat_map.total_occupied()


class TestThing(TestCase):

    def test_adjacent_count(self):
        seat_map = SeatMap('example.txt')
        count_str = ''
        for row in range(len(seat_map.grid)):
            for col in range(len(seat_map.grid[row])):
                if seat_map.is_state(row, col, 'floor'):
                    count_str += '. '
                else:
                    count_str += str(seat_map.adjacent_occupied(row, col)) + ' '
            count_str += '\n'
        # print(count_str)

    def test_functions(self):
        seat_map = SeatMap('example.txt')
        next_map_str = ''
        for row in range(len(seat_map.grid)):
            for col in range(len(seat_map.grid[row])):
                current_char = seat_map.grid[row][col]
                count = seat_map.adjacent_occupied(row, col)
                # print(seat_map.rules[current_char](count), ' ', end='')
            # print()

    def test_apply_rules(self):
        seat_map = SeatMap('example.txt')
        for i in range(1, 6):
            # print(f'Testing SeatMap plus {i}')
            changed = seat_map.apply_rules()
            assert changed
            seat_map_next = SeatMap(f'example_plus_{i}.txt')
            # print('example\n' + str(seat_map))
            # print('plus one\n' + str(seat_map_next))
            assert seat_map == seat_map_next

    def test_one_example(self):
        assert part1('example.txt') == 37

    def test_one_data(self):
        assert part1('data.txt') == 2281

    def test_improved_seat_map(self):
        seat_map = ImprovedSeatMap('example_two_1.txt')
        # for r, c in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, -1), (1, 0), (1, -1), (0, -1)]:
        #     print(r, c, seat_map.follow((4, 3), (0, -1)))
        assert seat_map.adjacent_occupied(4, 3) == 8
        seat_map = ImprovedSeatMap('example_two_2.txt')
        assert seat_map.adjacent_occupied(1, 1) == 0
        seat_map = ImprovedSeatMap('example_two_3.txt')
        assert seat_map.adjacent_occupied(3, 3) == 0
        seat_map = ImprovedSeatMap('example.txt')
        seat_map.apply_rules()
        print(seat_map)
        assert seat_map.adjacent_occupied(8, 0) == 4
        assert seat_map.adjacent_occupied(2, 0) == 5

    def test_two_example(self):
        assert part2('example.txt') == 26

    def test_two_data(self):
        assert part2('data.txt')
