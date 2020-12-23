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
        for l in input_file:
            line = l.rstrip().replace(r'(', '').replace(')', '')
            pieces = [x.replace(',', '') for x in line.split()]
            divider = pieces.index('contains')
            piece = {
                'ingredients': pieces[:divider],
                'allergens': pieces[divider + 1:]
            }
            datum.append(piece)
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


def deduce(data, part=1):
    allergy_info = {}
    ingredient_spam = []  # used for counting times an ingredient was found
    for entry in data:
        ingredients = entry['ingredients']
        ingredient_spam.extend(ingredients)
        allergens = entry['allergens']  # food may contain other allergens as well
        for a in allergens:
            if a in allergy_info:
                allergy_info[a].append(ingredients)
            else:
                allergy_info[a] = [ingredients]
    # print('deduce allergy info', allergy_info)
    # print('ingredient spam', ingredient_spam)
    counter = collections.Counter(ingredient_spam)
    # print('counted spam', counter)
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
    safe = [x for x in set(ingredient_spam) if x not in probably_something]
    # print('likely nothing:', safe)
    result = sum([y for x, y in counter.items() if x in safe])

    if part == 1:
        print('part1 solution:', result)
        return result

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
    # print(json.dumps(final_decision, sort_keys=True, indent=4))
    canonical_dangerous_ingredient_list = ''
    for f in sorted(final_decision):
        canonical_dangerous_ingredient_list += final_decision[f] + ','
    result = canonical_dangerous_ingredient_list.rstrip(',')
    print('part2 solution:', result)
    return result

class TestThing(TestCase):

    def setUp(self) -> None:
        print(f'\n--- Running test: {self._testMethodName} ---')

    def test_one_dev(self):
        data = parse_input('example.txt')
        print('file data', data)
        rendered_data = deduce(data)
        print('rendered data:', rendered_data)

    def test_one_example(self):
        assert deduce(parse_input('example.txt')) == 5

    def test_one_data(self):
        assert deduce(parse_input('data.txt')) == 2485

    def test_two_example(self):
        assert deduce(parse_input('example.txt'), part=2) == 'mxmxvkd,sqjhc,fvjkl'

    def test_two_data(self):
        assert deduce(parse_input('data.txt'), part=2) == 'bqkndvb,zmb,bmrmhm,snhrpv,vflms,bqtvr,qzkjrtl,rkkrx'
