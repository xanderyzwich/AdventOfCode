"""
Finding letters occurring exactly 2 or 3 times in a line
https://adventofcode.com/2018/day/2
"""

if __name__ == '__main__':
    twos, threes = 0, 0
    with open("input.txt", 'r') as input_file:
        # line_number = 1
        for line in input_file:
            counts = {}
            two, three = False, False
            for character in line:
                if character in counts:
                    counts[character] += 1
                else:
                    counts[character] = 1
            for key in counts:
                if counts[key] == 2:
                    two = True
                if counts[key] == 3:
                    three = True
            if two:
                twos += 1
            if three:
                threes += 1
            # print(str(line_number) + ' : ' + str(two) + ' : ' + str(three))
            # line_number += 1
        print('Final')
        print('Twos:    ' + str(twos))
        print('Threes:  ' + str(threes))
        print('Product: ' + str(twos*threes))

