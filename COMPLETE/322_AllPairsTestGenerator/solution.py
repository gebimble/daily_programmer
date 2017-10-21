#! /usr/bin/env python

from itertools import product, combinations


def all_pairs(*args):

    combos = []

    unique_pairs = set()

    every_set = list(map(' '.join, product(*args)))

    for i in range(len(args), 0, -1):

        combos, unique_pairs = create_combos(every_set,
                                             unique_pairs,
                                             combos, i)

    return combos


def create_combos(every_set, unique_pairs, combos, required):

    for item in every_set:

        parts = item.split()

        inner_perms = {''.join(a) for a in combinations(parts, 2)}

        difference = inner_perms.difference(unique_pairs)

        if len(difference) >= required:

            unique_pairs.update(difference)

            combos.append(item)

    return combos, unique_pairs


'''Part 1'''
list_a = ['0', '1']
list_b = ['A', 'B', 'C']
list_c = ['D', 'E', 'F', 'G']

combos = all_pairs(list_a, list_b, list_c)

print(len(combos))

'''Part 2'''
list_a = ['0', '1', '2', '3']
list_b = ['A', 'B', 'C', 'D']
list_c = ['E', 'F', 'G', 'H', 'I']

combos = all_pairs(list_a, list_b, list_c)

print(len(combos))

'''Part 3'''
list_a = ['0', '1', '2', '3', '4']
list_b = ['A', 'B', 'C', 'D', 'E']
list_c = ['F', 'G', 'H', 'I']
list_d = ['J', 'K', 'L']

combos = all_pairs(list_a, list_b, list_c, list_d)

print(len(combos))
