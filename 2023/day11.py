# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

import numpy as np

data = open("day11.txt");
# data = open("day11_ex.txt")

expandTo = 1000000

grid = []
galaxies = []
row = 0
for line in data:
    line = [x for x in line.strip()]
    grid.append(line)
    if "#" not in line:
        row += expandTo
    else:
        for col in range(len(line)):
            if line[col] == "#":
                galaxies.append((row, col))
        row += 1

tgrid = np.array(grid)
tgrid = tgrid.transpose()

def expandCols(galaxies, colList):
    for n, (row, col) in enumerate(galaxies):
        increaseBy = 0
        for expandMe in colList:
            if col > expandMe:
                increaseBy += expandTo - 1
        galaxies[n] = (row, col+increaseBy)

colList = []
for n, line in enumerate(tgrid):
    if "#" not in line:
        colList.append(n)

expandCols(galaxies, colList)

total = 0
for n, (row, col) in enumerate(galaxies):
    for m in range(n+1, len(galaxies)):
        (mrow, mcol) = galaxies[m]
        total += abs(mrow-row) + abs(mcol - col)

print(total)