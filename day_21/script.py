"""
Day X: Name
"""
import collections
from unittest import TestCase
import json


def parse_input(file_name):
    """

    :param file_name:
    :return: each item in the list is a package. It contains an ingredients list and allergens list
    """
    datum = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            pieces = line.rstrip().replace(r'(', '').replace(')', '').replace(',', '').split()
            divider = pieces.index('contains')
            datum.append({
                'ingredients': pieces[:divider],
                'allergens': pieces[divider + 1:]
            })
    return datum


def overlap(list1, list2):
    """

    :param list1:
    :param list2:
    :return: list of elements existing in both provided lists
    """
    result = [x for x in list1 if x in list2]
    # print("Overlap", list1, list2, result)
    return result


def ingredient_lists_by_allergen(data):
    allergy_info = {}
    for entry in data:
        ingredients = entry['ingredients']
        allergens = entry['allergens']  # food may contain other allergens as well
        for a in allergens:
            if a in allergy_info:
                allergy_info[a].append(ingredients)
            else:
                allergy_info[a] = [ingredients]
    # print('deduce allergy info', allergy_info)
    return allergy_info


def get_ingredient_counts(data):
    ingredient_spam = []  # used for counting times an ingredient was found
    for entry in data:
        ingredient_spam.extend(entry['ingredients'])
    # print('ingredient spam', ingredient_spam)
    return collections.Counter(ingredient_spam)


def get_probables(allergy_info):
    """
    Find the ingredients that are most likely to be each allergen
    :param allergy_info:
    :return:
    """
    probable, probably_something = {}, []
    for a in allergy_info:
        possibles = {}
        occurance_count = len(allergy_info[a])
        for l in allergy_info[a]:
            for i in l:
                if i in possibles:
                    possibles[i] += 1
                else:
                    possibles[i] = 1
        # print('counting', a, occurance_count, possibles)
        guesses = []
        for x in possibles:
            if possibles[x] == occurance_count:
                guesses.append(x)
                probably_something.append(x)
            else:
                pass
        probable[a] = guesses
    # print('probably', probable, 'something:', probably_something)
    # print(json.dumps(probable, sort_keys=True, indent=4))
    return probable, probably_something


def part1(file_name):
    data = parse_input(file_name)
    allergy_info = ingredient_lists_by_allergen(data)
    probable, probably_something = get_probables(allergy_info)

    counter = get_ingredient_counts(data)
    # print('counted spam', counter)
    safe = [x for x in counter.keys() if x not in probably_something]
    # print('likely nothing:', safe)

    result = sum([y for x, y in counter.items() if x in safe])
    print('part1 solution:', result)
    return result


def cleanup_probables(probable):
    """
    Deduplicate the probables list
    :param probable:
    :return:
    """
    final_decision, prob_len = {}, len(probable)
    while len(final_decision) != prob_len:
        delete_list = []
        for a in probable:
            if len(probable[a]) == 1:
                final_decision[a] = probable[a][0]
                delete_list.append(a)
                for p in [x for x in probable if x != a and final_decision[a] in probable[x]]:
                    probable[p].remove(final_decision[a])
        for d in delete_list:
            del probable[d]
    return final_decision


def compile_canonical_dangerous_ingredient_list(final_decision):
    """
    Create a list of the dangerous ingredients ordered by their English name
    :param final_decision:
    :return:
    """
    canonical_dangerous_ingredient_list = ''
    for f in sorted(final_decision):
        canonical_dangerous_ingredient_list += final_decision[f] + ','
    result = canonical_dangerous_ingredient_list.rstrip(',')
    return result


def part2(file_name):
    data = parse_input(file_name)
    allergy_info = ingredient_lists_by_allergen(data)
    probable, probably_something = get_probables(allergy_info)

    final_decision = cleanup_probables(probable)
    # print(json.dumps(final_decision, sort_keys=True, indent=4))

    result = compile_canonical_dangerous_ingredient_list(final_decision)
    print('part2 solution:', result)
    return result


class TestThing(TestCase):

    def setUp(self) -> None:
        print(f'\n--- Running test: {self._testMethodName} ---')

    def test_one_example(self):
        assert part1('example.txt') == 5

    def test_one_data(self):
        assert part1('data.txt') == 2485

    def test_two_example(self):
        assert part2('example.txt') == 'mxmxvkd,sqjhc,fvjkl'

    def test_two_data(self):
        assert part2('data.txt') == 'bqkndvb,zmb,bmrmhm,snhrpv,vflms,bqtvr,qzkjrtl,rkkrx'
