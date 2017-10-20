#! /usr/bin/env python

from itertools import product, combinations


def all_pairs(a, b, c):

    combos = []

    unique_pairs = set()

    every_set = map(' '.join, product(a, b, c))

    for item in every_set:

        parts = item.split()

        inner_perms = {''.join(a) for a in combinations(parts, 2)}

        difference = inner_perms.difference(unique_pairs)

        unique_pairs.update(difference)

        if difference:
            combos.append(item)

    print(len(combos))


list_a = ['0', '1']
list_b = ['A', 'B', 'C']
list_c = ['D', 'E', 'F', 'G']

all_pairs(list_a, list_b, list_c)
