# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import numpy as np

elves = []
elf = []

for line in open("day1_input.txt"):
#for line in open("day1_example.txt"):
    line = line.strip()
    if line == "":
        elves.append(elf)
        elf = []
    else:
        calories = int(line.strip())
        elf.append(calories)

if (len(elf)):
    elves.append(elf)
    
#part 1:
top3 = [0, 0, 0]
for elf in elves:
    total = np.sum(elf)
    if total>top3[0]:
        top3[0] = total
        if top3[1] < top3[0]:
            save = top3[1]
            top3[1] = top3[0]
            top3[0] = save
            if top3[2] < top3[1]:
                save = top3[2]
                top3[2] = top3[1]
                top3[1] = save

print(top3)
print(np.sum(top3))
