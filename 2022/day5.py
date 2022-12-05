# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import numpy as np


crates = []
rules = []
for line in open("day5_input.txt"):
#for line in open("day5_example.txt"):
    if len(line) > 1:
        if "move" in line:
            lvec = line.split(' ')
            rules.append((int(lvec[1]), int(lvec[3])-1, int(lvec[5])-1))
        else:
            crates.append(line)

cratelen = round(len(crates[0])/4)
stacks = []
for stack in range(cratelen):
    stacks.append([])

crates.pop()

for line in crates:
    for p in range(cratelen):
        pos = p*4+1
        if line[pos] != " ":
            stacks[p].append(line[pos])

print(stacks)


# for (num, frm, to) in rules:
#     for mv in range(num):
#         stacks[to].insert(0, stacks[frm][0])
#         stacks[frm] = stacks[frm][1:]
#     print(stacks)

for (num, frm, to) in rules:
    for mv in range(num):
        stacks[to].insert(0, stacks[frm][num-mv-1])
    stacks[frm] = stacks[frm][num:]
    print(stacks)

result = ""
for stack in stacks:
    result += stack[0]
    
print(result)