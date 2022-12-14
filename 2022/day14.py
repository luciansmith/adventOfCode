# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import copy
import time

begin = time.perf_counter()

caverow = [0]*1000
cave = [caverow]

def addCaveRowsTo(cave, val):
    caverow = [0]*1000
    while len(cave) < val+1:
        cave.append(copy.copy(caverow))

def printSmallCave(cave):
    for n in range(len(cave)):
        print(cave[n][494:504])

for  line in open("day14_input.txt"):
#for line in open("day14_example.txt"):
    lvec = line.strip().split(" -> ")
    pairvec = []
    for prval in lvec:
        prval = prval.split(",");
        prval = (int(prval[0]), int(prval[1]))
        pairvec.append(prval)
    for c in range(len(pairvec)-1):
        (scol, srow) = pairvec[c]
        (ecol, erow) = pairvec[c+1]
        addCaveRowsTo(cave, max(srow, erow))
        if scol==ecol:
            for r in range(min(srow, erow), max(srow, erow)+1):
                cave[r][scol] = 1
        elif srow == erow:
            for c in range(min(scol, ecol), max(scol, ecol)+1):
                cave[erow][c] = 1
        else:
            raise("Unworkable row/column", pairvec)

#Part 2:
cave.append([0]*1000)
cave.append([1]*1000)

sandCount = 0
#printSmallCave(cave)

def dropSandFrom(row, col, cave):
    if len(cave) == row+1:
        return False
    if cave[row][col] != 0:
        return False
    if cave[row+1][col] == 0:
        return dropSandFrom(row+1, col, cave)
    elif cave[row+1][col-1] == 0:
        return dropSandFrom(row+1, col-1, cave)
    elif cave[row+1][col+1] == 0:
        return dropSandFrom(row+1, col+1, cave)
    else:
        cave[row][col] = 2
        return True

while dropSandFrom(0, 500, cave):
    sandCount += 1

print(sandCount)    
print(time.perf_counter()-begin, "seconds")
        
        