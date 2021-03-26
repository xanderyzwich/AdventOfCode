"""
Frequency adjustments
https://adventofcode.com/2018/day/1#part2
"""

if __name__ == '__main__':
    total = 0
    visited_frequencies = [0]
    found = False
    loop_time = 1
    while not found:
        with open('input.txt', 'r') as input_file:
            print(str(loop_time) + " time in loop")
            for line in input_file:
                if line.startswith('+'):
                    total += int(line[1:])
                elif line.startswith('-'):
                    total -= int(line[1:])
                else:
                    print('unexpected line start character')
                if total in visited_frequencies:
                    print(total)
                    found = True
                    break
                else:
                    visited_frequencies.append(total)
        loop_time += 1
    # print(total)

