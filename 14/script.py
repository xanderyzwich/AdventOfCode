"""
 Day 14: Chocolate Charts
 https://adventofcode.com/2018/day/14
"""


def new_recipes(elf_one_score, elf_two_score):
    total = elf_one_score + elf_two_score
    new_recipe_list = []
    for character in str(total):
        new_recipe_list.append(character)
    return new_recipe_list


def next_recipe_index(old_recipe_index, old_recipe_score):
    movement = old_recipe_index + old_recipe_score + 1
    score_length = len(scores)
    new_index = movement % score_length
    return new_index


def part1(state_input, input_round):
    scores, elf_recipe_one_index, elf_recipe_two_index = state_input
    for round_number in range(1, input_round + 11):
        elf_recipe_one_score = scores[elf_recipe_one_index]
        elf_recipe_two_score = scores[elf_recipe_two_index]
        new_scores_list = new_recipes(elf_recipe_one_score, elf_recipe_two_score)
        for score in new_scores_list:
            scores.append(int(score))
        elf_recipe_one_index = next_recipe_index(elf_recipe_one_index, elf_recipe_one_score)
        elf_recipe_two_index = next_recipe_index(elf_recipe_two_index, elf_recipe_two_score)
    print(''.join(map(str, scores[input_round: input_round + 10])))


def part2(state_input, input_scores):
    scores, elf_recipe_one_index, elf_recipe_two_index = state_input
    input_string = str(input_scores)
    score_string = ''.join(map(str, scores))
    completed = False
    while not completed:
        elf_recipe_one_score = scores[elf_recipe_one_index]
        elf_recipe_two_score = scores[elf_recipe_two_index]
        new_scores_list = new_recipes(elf_recipe_one_score, elf_recipe_two_score)
        for score in new_scores_list:
            scores.append(int(score))
            score_string += str(score)
            score_string = score_string[0 - len(input_string):]
            if input_string == score_string:
                completed = True
                break
            # if len(scores) % (10 ** 6) == 0:
            #     print(len(scores))
        elf_recipe_one_index = next_recipe_index(elf_recipe_one_index, elf_recipe_one_score)
        elf_recipe_two_index = next_recipe_index(elf_recipe_two_index, elf_recipe_two_score)

    print(''.join(map(str, scores)).find(str(input_scores)))


if __name__ == '__main__':
    input_value = 793061
    elf_recipe_one_index = 0
    elf_recipe_two_index = 1
    scores = [3, 7]
    state = [scores, elf_recipe_one_index, elf_recipe_two_index]

    # part1(state, 9)
    # part1(state, 5)
    # part1(state, 18)
    # part1(state, 2018)
    # part1(state, input_value)

    # part2(state, 51589)
    # part2(state, '01245')
    # part2(state, 92510)
    # part2(state, 59414)
    part2(state, input_value)
