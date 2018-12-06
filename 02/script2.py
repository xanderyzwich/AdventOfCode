"""
Pattern Matching
Find the two lines that differ by exactly one character
"""


def diff(input1, input2):
    # print('Diffing:  ' + input1 + ' & ' + input2)
    match_count = 0
    if len(input1) != len(input2) and False:
        print('dIfF eRrOr')
        return len(input1)
    else:
        for i in range(len(input1)-1):
            if input1[i] == input2[i]:
                match_count += 1
        # print(len(input1) - match_count - 1)
        return len(input1) - 1 - match_count


def same(input1, input2):
    print('Entering Same')
    output_string = ''
    if len(input1) != len(input2):
        print('sAmE eRrOr')
        return 'eRrOr'
    else:
        for i in range(len(input1)-1):
            if input1[i] == input2[i]:
                output_string += input1[i]
        return output_string


if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        one, two, total = 1, 1, 1
        lines = list(input_file)
        for line1 in lines:
            for line2 in lines:
                print(str(one) + ' : ' + str(two) + ' : ' + str(total))
                if diff(line1, line2) == 1:
                    print('FOUND')
                    print(same(line1, line2))
                    exit(0)
                total += 1
                two += 1
            one += 1
            two = 1



