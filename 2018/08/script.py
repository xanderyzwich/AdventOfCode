"""
Day 8: Memory Maneuver
https://adventofcode.com/2018/day/8
"""

import datetime as dt

def build_tree(file_name):
    input_data = ''
    with open(file_name, 'r') as input_file:
        input_data = input_file.readline().split()
    tree, input_data = build_node(input_data)
    return tree


def build_node(input_data):
    child_quantity = int(input_data.pop(0))
    metadata_quantity = int(input_data.pop(0))
    children = []
    metadata = []
    for i in range(child_quantity):
        temp_child, input_data = build_node(input_data)
        children.append(temp_child)
    for i in range(metadata_quantity):
        metadata.append(int(input_data.pop(0)))
    return (child_quantity, metadata_quantity, children, metadata), input_data


def node_sum(tree_node):
    child_quantity, metadata_quantity, children, metadata = tree_node
    total = sum(metadata)
    for child in children:
        total += node_sum(child)
    return total


def evaluate(node):
    child_quantity, metadata_quantity, children, metadata = node
    if len(children) == 0:
        return sum(metadata)
    else:
        total = 0
        for value in metadata:
            index = value - 1
            if 0 <= index < len(children):
                total += evaluate(children[index])
        return total


if __name__ == '__main__':
    tree = build_tree('input.txt')
    print('Starting part1...', end='Answer:  ')
    start = dt.datetime.now()
    tree = build_tree('input.txt')
    print(node_sum(tree))
    print('finished in', dt.datetime.now() - start)

    print('Starting part2...', end='Answer:  ')
    start = dt.datetime.now()
    print(evaluate(tree))
    print('finished in', dt.datetime.now() - start)


