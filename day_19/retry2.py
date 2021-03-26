import re

temp_rules, messages = {}, []
# keys_to_delete = []
final_rules = {}


def parse_rule(line):
    nbr, val = line.rstrip().split(': ')
    if '"' in val:
        val = val.replace('"', '')
    return int(nbr), val


def add_rule(rule_num, rule_str):
    if all([re.match('[a-zA-Z]+', p) for p in re.findall(r'[\w]+', rule_str)]):
        # print(f'FOUND-- {rule_num}: {rule_str}')
        cleaned_rule = f'({rule_str})'.replace(' ', '')
        final_rules[rule_num] = cleaned_rule
        for r in [t for t in temp_rules if t != rule_num]:
            temp_rules[r] = temp_rules[r].replace(f' {str(rule_num)} ', f' {cleaned_rule} ')
        return True
    # rule isn't strictly alphabetic
    print(f'Failed to add {rule_num}: {rule_str}')
    return False


def add_rules():
    # print('Entering add_rules')
    keys_to_delete = []
    for nbr, txt in temp_rules.items():
        if add_rule(nbr, txt):
            keys_to_delete.append(nbr)
    # print(final_rules, temp_rules)
    changed = len(keys_to_delete) > 0
    for ktd in keys_to_delete:
        del temp_rules[ktd]
    return changed


def part1():
    count = 0
    print(sorted(final_rules))
    for m in messages:
        rule_zero = f'^{final_rules[0]}$'
        if re.match(rule_zero, m):
            count += 1
    print('Part1 solution:', count)
    return count



if __name__ == '__main__':
    # file_name = 'example.txt'
    file_name = 'data.txt'
    with open(file_name, 'r') as input_file:
        for line in input_file:
            if re.match('^[0-9]+: ', line):
                k, v = parse_rule(line)
                # print(f'{k}: {v}')
                temp_rules[k] = v
            elif re.match(r'^[a-zA-Z]+$', line):
                messages.append(line.rstrip())
    rule_count = len(temp_rules)
    while len(final_rules) < rule_count:
        add_rules()
        print(len(final_rules))
    # add_rules()
    print(temp_rules)
    part1()
    print(final_rules, temp_rules, messages)
