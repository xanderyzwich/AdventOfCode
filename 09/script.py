"""
Day 9: Marble Mania
https://adventofcode.com/2018/day/9
"""

import datetime as dt


class CircleNode:
    def __init__(self, value=0):
        self.value = value
        self.clockwise = self
        self.counterclockwise = self


def play(new, current=CircleNode):
    if new == 0:
        return CircleNode(new), 0
    elif new == 1:
        one = CircleNode(new)
        zero = current
        zero.clockwise = one
        zero.counterclockwise = one
        one.clockwise = zero
        one.counterclockwise = zero
        return one, 0
    elif new % 23 == 0:
        value = new
        for i in range(7):
            current = current.counterclockwise
            # print('moving to ', current.value)
        cw = current.clockwise
        ccw = current.counterclockwise
        cw.counterclockwise = ccw
        ccw.clockwise = cw
        value += current.value
        # print(current.value)
        return cw, value
    else:
        temp = CircleNode(new)
        one = current.clockwise
        two = one.clockwise
        temp.counterclockwise = one
        temp.clockwise = two
        one.clockwise = temp
        two.counterclockwise = temp
        return temp, 0


def view(current):
    it = current
    print('Current Ring: ', it.value, end=', ')
    temp = it.clockwise
    it = temp
    while it != current:
        print(it.value, end=', ')
        temp = it.clockwise
        it = temp
    print('')



def game(players, last):
    current = None
    scores = {}
    i = 0
    print("Starting game til:", last, ' - Answer: ', end='')
    while True:
        for player in range(players):
            if current:
                current, score = play(i, current)
                # print(i, end=', ')
            else:
                current, score = play(0)
                # print("Zero Setup", end=', ')
            if player in scores.keys():
                scores[player] += score
                # if score > 0:
                #     print('Player', player, 'scored', score)
            else:
                scores[player] = score
                # print('insert')
            # print(i, end=': \t[')
            # for points in scores.values():
            #     print(points, end=', ')
            # print(']')
            if last == i:
                return max(scores.values())
        # print(i, end='\t')
        # view(current)
            i += 1


if __name__ == '__main__':

    # DEMO INPUT
    # print(game(10, 23))
    # print(game(10, 1618))
    # print(game(13, 7999))
    # print(game(17, 1104))
    # print(game(21, 54718))
    # print(game(30, 37385))

    ## Actual input
    ## 418 players; last marble is worth 70769 points
    start = dt.datetime.now()
    print('Part 1 - Answer', end=' ')
    print(game(418, 70769), end=' ')
    print('finished in', dt.datetime.now() - start)

    start = dt.datetime.now()
    print('Part 1 - Answer', end=' ')
    print(game(418, 70769 * 100), end=' ')
    print('finished in', dt.datetime.now() - start)


