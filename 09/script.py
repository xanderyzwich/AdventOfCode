"""
Day 9: Marble Mania
https://adventofcode.com/2018/day/9
"""

import datetime as dt


class CircleNode:
    def __init__(self, value=0):
        self.clockwise = self
        self.counterclockwise = self
        self.value = value


def play(new, current=CircleNode):
    if new == 0:
        return CircleNode(new), 0
    elif new % 23 == 0:
        value = new
        for i in range(7):
            current = current.counterclockwise
            # print(current.value, end=' - ')
        current.clockwise.counterclockwise = current.counterclockwise
        current.counterclockwise.clockwise = current.clockwise
        value += current.value
        # print(value)
        return current, value
    else:
        temp = CircleNode(new)
        one = current.clockwise
        two = one.clockwise
        temp.counterclockwise = one
        temp.clockwise = two
        one.clockwise = temp
        two.counterclockwise = temp
        return temp, 0


def game(players, last):
    current = None
    scores = {}
    i = 0
    while True:
        for player in range(players):
            if current:
                current, score = play(i, current)
            else:
                current, score = play(0)
            if player in scores.keys():
                scores[player] += score
                # if score > 0:
                #     print('Player', player, 'scored', score)
            else:
                scores[player] = score
                # print('insert')
            if last == i:
                return max(scores.values())
        i += 1


if __name__ == '__main__':
    # print('Starting part1...', end='Answer:  ')
    # start = dt.datetime.now()
    # print('finished in', dt.datetime.now() - start)

    # print('Starting part2...', end='Answer:  ')
    # start = dt.datetime.now()
    # print('finished in', dt.datetime.now() - start)

    print(game(10, 23))
    print(game(10, 1618))
    print(game(13, 7999))
    print(game(17, 1104))
    print(game(21, 54718))
    print(game(30, 37385))





