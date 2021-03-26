import re
from time import sleep


def read_file(file_name):
    rules, messages = [], []
    with open(file_name, 'r') as input_file:
        for l in input_file:
            line = l.rstrip()
            if re.match(r'^[0-9]+(:).*.$', l):  # is a rule
                rule = line.replace(r': ', ':').replace(' | ', '|').replace(r' ', '.').replace('"', '')
                rules.append(rule)
            elif re.match(r'^[a-zA-Z]+$', l):
                messages.append(line)
    return rules, messages


def process_simple(rules):
    rule_dict, to_remove = {}, []
    for r in rules:
        k, v = r.split(':')
        if re.match(r'[a-zA-Z]+', v):
            rule_dict[int(k)] = v
            to_remove.append(r)
    for d in to_remove:
        rules.remove(d)
    # print(rule_dict, rules)
    return rule_dict, rules


def process_complex(rule_dict, rules):
    my_dict, my_rules = rule_dict, rules
    for r in my_rules:
        k, v = r.split(':')
        deps = list(map(int, set(re.findall('[0-9]+', v))))
        # print(k, v, deps)
        temp_rule = v
        if all([d in my_dict for d in deps]):
            for d in deps:
                temp_rule = temp_rule.replace(str(d), f'({my_dict[d]})')
            temp_rule = temp_rule.replace('.', '')
            my_dict[int(k)] = temp_rule
            my_rules.remove(r)
            # print(k, temp_rule)
    return my_dict, my_rules


def simulate(file_name):
    rules, messages = read_file(file_name)
    rule_set, complex_rules = process_simple(rules)
    while len(complex_rules) != 0:
        rule_set, complex_rules = process_complex(rule_set, rules)
        # print(len(rule_set), len(complex_rules))

    print(len(rule_set), len(messages), len(rule_set[0]))
    count = 0
    for m in messages:
        if re.match(f'^{rule_set[0]}$', m):
            count += 1
    print(f'Found {count} matches')
    return count



if __name__ == '__main__':
    simulate('data.txt')
    # results = []
    # for i in range(100):
    #     print(i)
    #     r = simulate('data.txt')
    #     if r not in results:
    #         results.append(r)
    #     sleep(1)
    # print(sorted(results))

