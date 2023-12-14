# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

import numpy as np

data = open("day13.txt");
# data = open("day13_ex.txt")

total = 0
grid = []

def checkGridRowReflection(grid, n):
    for step in range(n+1):
        if len(grid) < n+step+2:
            return True
        if grid[n-step] != grid[n+step+1]:
            return False
    return True


def countGridReflectionScore(grid):
    total = 0
    for n in range(0, len(grid)-1):
        if checkGridRowReflection(grid, n):
            print("horizontal reflection at", n)
            total += 100*(n+1)
    tgrid = np.array(grid)
    tgrid = tgrid.transpose()
    tgrid = [list(x) for x in tgrid]
    for n in range(0, len(tgrid)-1):
        if checkGridRowReflection(tgrid, n):
            print("vertical reflection at", n)
            total += n+1
    return total

def twoRowsOffByOne(candidateRows):
    if not candidateRows:
        return False
    (row1, row2) = candidateRows
    diff = 0
    for n in range(len(row1)):
        if row1[n] != row2[n]:
            diff += 1
    return diff==1

def gridRowReflectionOffByExactlyOne(grid, n):
    candidateRows = None
    candidateIndexes = (0,0)
    for step in range(n+1):
        if len(grid) < n+step+2:
            if candidateRows and twoRowsOffByOne(candidateRows):
                return True
            return False
        if grid[n-step] != grid[n+step+1]:
            if not candidateRows:
                candidateRows = (grid[n-step], grid[n+step+1])
                candidateIndexes = (n-step, n+step+1)
            else:
                return False
    if candidateRows and twoRowsOffByOne(candidateRows):
        return True
    return False

def findAndReportSmudge(grid):
    for n in range(0, len(grid)-1):
        if gridRowReflectionOffByExactlyOne(grid, n):
            return 100*(n+1)
    tgrid = np.array(grid)
    tgrid = tgrid.transpose()
    tgrid = [list(x) for x in tgrid]
    for n in range(0, len(tgrid)-1):
        if gridRowReflectionOffByExactlyOne(tgrid, n):
            return n+1
    raise Exception("No smudge found")

for line in data:
    if line.strip() == "":
        total += findAndReportSmudge(grid)
        grid.clear()
    else:
        grid.append([x for x in line.strip()])
total += findAndReportSmudge(grid)

print(total)