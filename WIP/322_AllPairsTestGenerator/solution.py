#! /usr/bin/env python

checkboxList = ['0', '1']
first_dropList = ['A', 'B', 'C']
second_dropList = ['D', 'E', 'F', 'G']

all_combos = []

for c in checkboxList:
    for f in first_dropList:
        for s in second_dropList:
            value = ' '.join([c, f, s])
            all_combos.append(value)

print(all_combos)
