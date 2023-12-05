# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

data = open("day3.txt");
# data = open("day3_ex.txt")


total = 0
grid = []
for line in data:
    grid.append(line.strip())

symbols = set()
gears = {}
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if not(ch.isnumeric()) and ch != ".":
            symbols.add((r, c))
        if ch == '*':
            gears[(r,c)] = []
                
print(symbols)

def checkPart(partstr, symbols, r, c):
    print(partstr, r, c)
    for row in range(3):
        for col in range(len(partstr)+2):
            checkr = r + row - 1
            checkc = c + col -1
            if (checkr, checkc) in symbols:
                return int(partstr)
    return 0
            
# Part 1:
# partstr = ""
# for r, row in enumerate(grid):
#     if partstr != "":
#         total += checkPart(partstr, symbols, r-1, len(row)-len(partstr))
#     partstr = ""
#     for c, ch in enumerate(row):
#         if ch.isnumeric():
#             partstr = partstr + ch
#         else:
#             if partstr != "":
#                 total += checkPart(partstr, symbols, r, c-len(partstr))
#             partstr = ""
# if partstr != "":
#     total += checkPart(partstr, symbols, r-1, len(row)-len(partstr))

def checkGear(partstr, gears, r, c):
    print(partstr, r, c)
    for row in range(3):
        for col in range(len(partstr)+2):
            checkr = r + row - 1
            checkc = c + col -1
            if (checkr, checkc) in gears:
                gears[(checkr, checkc)].append(partstr)

partstr = ""
for r, row in enumerate(grid):
    if partstr != "":
        checkGear(partstr, gears, r-1, len(row)-len(partstr))
    partstr = ""
    for c, ch in enumerate(row):
        if ch.isnumeric():
            partstr = partstr + ch
        else:
            if partstr != "":
                checkGear(partstr, gears, r, c-len(partstr))
            partstr = ""
if partstr != "":
    checkGear(partstr, gears, r-1, len(row)-len(partstr))

geartot = 0
for gearloc in gears:
    labels = gears[gearloc]
    if len(labels) == 2:
        geartot += int(labels[0]) * int(labels[1])
    
# print("Total:", total)
print("Gear total:", geartot)