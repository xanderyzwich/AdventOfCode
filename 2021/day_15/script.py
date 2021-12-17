"""
Day 15: Chiton
"""
import copy
import sys
from unittest import TestCase


class PriorityQueue:
    class PriorityNode:
        def __init__(self, sequence, cost):
            self.path = sequence
            self.next = None
            self.cost = cost

        def __str__(self):
            return f'NodeValues:\tcost:{self.cost}\tpath:{self.path}'

    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, sequence, cost):
        self.length += 1
        new = PriorityQueue.PriorityNode(sequence, cost)

        if self.head is None:
            self.head = new
            return

        previous, current = None, self.head
        while current.cost <= new.cost:
            previous, current = current, current.next
            # print('Previous:', previous, 'Current:', current)
            if current is None:
                break
        if previous is None:
            new.next = self.head
            self.head = new
        elif current is None:
            previous.next = new
        else:
            new.next = current
            previous.next = new

    def pull(self):
        self.length -= 1
        result, self.head = self.head, self.head.next
        return result

    def __len__(self):
        return self.length


class DjikstraQueue:
    class DjikstraNode:
        def __init__(self, row, col, cost):
            self.row = row
            self.col = col
            self.next = None
            self.cost = cost

        def __str__(self):
            return f'NodeValues:\tcost:{self.cost}\tpath:{self.path}'

    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, row, col, cost):
        self.length += 1
        new = DjikstraQueue.DjikstraNode(row, col, cost)

        if self.head is None:
            self.head = new
            return

        previous, current = None, self.head
        while current.cost <= new.cost:
            previous, current = current, current.next
            # print('Previous:', previous, 'Current:', current)
            if current is None:
                break
        if previous is None:
            new.next = self.head
            self.head = new
        elif current is None:
            previous.next = new
        else:
            new.next = current
            previous.next = new

    def pull(self):
        self.length -= 1
        result, self.head = self.head, self.head.next
        return result

    def __len__(self):
        return self.length


def get_adjacent_indexes(current_row, current_col, full_2d_list):
    adjacents = []
    if 0 < current_row:
        adjacents.append((current_row - 1, current_col))
    if len(full_2d_list) > current_row + 1:
        adjacents.append((current_row + 1, current_col))
    if 0 <= current_col - 1:
        adjacents.append((current_row, current_col - 1))
    if len(full_2d_list[current_row]) > current_col + 1:
        adjacents.append((current_row, current_col + 1))
    return adjacents


def find_shortest_path(field):
    queue = PriorityQueue()

    queue.insert([(0, 0, field[0][0])], 0)  # Starting Point
    visited = [(0, 0)]

    end = len(field)-1, len(field[0])-1
    while True:

        # get shortest known path
        best_candidate = queue.pull()
        candidate_path = best_candidate.path

        # currently considered point on the map
        current_row, current_col, _ = candidate_path[-1]
        if end == (current_row, current_col):
            # draw_path(field, best_candidate.path)
            return best_candidate.cost

        # possible next steps
        adjacent_indexes = get_adjacent_indexes(current_row, current_col, field)
        if 1 < len(candidate_path):  # don't go backwards
            previous_row, previous_col, _ = candidate_path[-2]
            adjacent_indexes.remove((previous_row, previous_col))

        for r, c in adjacent_indexes:
            if (r, c) in visited:
                continue
            # Move to next position
            next_cost = best_candidate.cost + field[r][c]
            next_sequence = copy.deepcopy(candidate_path)
            next_sequence.append((r, c, field[r][c]))
            queue.insert(next_sequence, next_cost)
            visited.append((r, c))


def extend_field(small_field):
    big_field = []
    for i in range(5):
        for r in range(len(small_field)):
            big_row = []
            for j in range(5):
                for c in range(len(small_field[r])):
                    original_value = small_field[r][c]
                    bigger_value = (i + j + original_value)
                    wrapped_value = (bigger_value % 10) + 1
                    new_value = bigger_value if bigger_value < 10 else wrapped_value
                    big_row.append(new_value)
            big_field.append(big_row)
    return big_field


def draw_path(big_field, path):
    rows, cols = len(big_field), len(big_field[0])
    blank_field = [['.' for _ in range(cols)] for _ in range(rows)]
    for r, c, _ in path:
        blank_field[r][c] = 'X'
    for row in blank_field:
        print(row)


def djikstra(field):
    # TODO: Implement Djikstras algorithm from https://www.dougmahugh.com/dijkstra/
    rows, cols = len(field), len(field[0])
    end = rows-1, cols-1
    dist_field = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
    dist_field[0][0], to_visit = 0, DjikstraQueue()
    to_visit.insert(0, 0, 0)

    while 0 < len(to_visit):
        here = to_visit.pull()
        here_row, here_col, here_distance = here.row, here.col, here.cost
        if end == (here_row, here_col):
            return here_distance
        adjacents = get_adjacent_indexes(here_row, here_col, field)
        for a_row, a_col in adjacents:

            a_cost = field[a_row][a_col] + here_distance
            # is this a shorter path to a
            # if so then we will want to visit a again
            if a_cost < dist_field[a_row][a_col]:
                dist_field[a_row][a_col] = a_cost
                to_visit.insert(a_row, a_col, a_cost)




def parse_file(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = [int(a) for a in list(line.strip())]
            data.append(clean)
    return data


class TestThing(TestCase):
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

    def test_one_example(self):
        result = find_shortest_path(self.example_data)
        self.assertion(40 == result)

    def test_one_data(self):
        result = find_shortest_path(self.input_data)
        self.assertion(423 == result)

    def test_two_example(self):
        # print()
        # for row in extend_field([[8]]):
        #     print(row)
        # print()

        # result = find_shortest_path(extend_field(self.example_data))
        # print(result)
        # self.assertion(315 == result)

        result = djikstra(extend_field(self.example_data))
        self.assertion(315 == result)

    def test_two_data(self):
        result = djikstra(extend_field(self.input_data))
        print(result)
        self.assertion(2778 == result)
