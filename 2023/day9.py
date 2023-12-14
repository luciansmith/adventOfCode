# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

data = open("day9.txt");
# data = open("day9_ex.txt")


total = 0
earlytotal = 0
grid = []
for line in data:
    line = line.strip().split()
    grid.append([int(x) for x in line])

def getDifferences(row):
    newrow = []
    for c in range(len(row)-1):
        newrow.append(row[c+1] - row[c])
    return newrow

def isAllZeroes(row):
    for val in row:
        if val != 0:
            return False
    return True

def getRowsUntilZeroes(row):
    rowset = [row]
    newrow = getDifferences(row)
    rowset.insert(0, newrow)
    while len(newrow)>0 and not(isAllZeroes(newrow)):
        newrow = getDifferences(newrow)
        rowset.insert(0, newrow)
    return rowset

def extrapolateFrom(rowset):
    retval = 0
    for row in rowset:
        retval += row[-1]
    return retval

def extrapolateFirstFrom(rowset):
    retval = 0
    for row in rowset:
        retval = row[0] - retval
    print(retval)
    return retval

for row in grid:
    rowset = getRowsUntilZeroes(row)
    # print(rowset)
    total += extrapolateFrom(rowset)
    earlytotal += extrapolateFirstFrom(rowset)

print(total)
print(earlytotal)
