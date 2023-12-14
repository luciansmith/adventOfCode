# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

data = open("day10.txt");
# data = open("day10_ex.txt")

total = 0
grid = []
startLoc = (0,0)
for line in data:
    line = line.strip()
    grid.append(line)
    if "S" in line:
        loc = line.find('S')
        startLoc = (len(grid)-1, loc)
        assert(grid[startLoc[0]][startLoc[1]] == 'S')


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

def nextFrom(loc, direction):
    (row, col) = loc
    char = grid[row][col]
    if char=='|':
        if direction=="south":
            return "south"
        elif direction=="north":
            return "north"
        else:
            return "none"
    if char=='-':
        if direction=="east":
            return "east"
        elif direction=="west":
            return "west"
        else:
            return "none"
    if char=='L':
        if direction=="south":
            return "east"
        elif direction=="west":
            return "north"
        else:
            return "none"
    if char=='J':
        if direction=="south":
            return "west"
        elif direction=="east":
            return "north"
        else:
            return "none"
    if char=='7':
        if direction=="east":
            return "south"
        elif direction=="north":
            return "west"
        else:
            return "none"
    if char=='F':
        if direction=="west":
            return "south"
        elif direction=="north":
            return "east"
        else:
            return "none"
    return "none"

def locFrom(loc, direction):
    (row, col) = loc
    if direction=="north":
        return (row-1, col)
    if direction=="south":
        return (row+1, col)
    if direction=="east":
        return (row, col+1)
    if direction=="west":
        return (row, col-1)

startDir = "none"
#Don't worry about S being on the edge; it isn't.
startDirs = []
if nextFrom((startLoc[0]-1, startLoc[1]), "north") != "none":
    startDirs.append("north")
if nextFrom((startLoc[0], startLoc[1]+1), "east") != "none":
    startDirs.append("east")
if nextFrom((startLoc[0], startLoc[1]-1), "west") != "none":
    startDirs.append("west")
if nextFrom((startLoc[0], startLoc[1]-1), "south") != "none":
    startDirs.append("south")
else:
    raise Exception("No good start direction")

startDir = startDirs[0]
assert(len(startDirs) == 2)
startEquiv = ""
if "north" in startDirs:
    if "east" in startDirs:
        startEquiv = "L"
    elif "west" in startDirs:
        startEquiv = "J"
    elif "south" in startDirs:
        startEquiv = "|"

elif "east" in startDirs:
    if "west" in startDirs:
        startEquiv = "-"
    elif "south" in startDirs:
        startEquiv = "F"

else:
    startEquiv = "7"

loopLocs = [startLoc]

nextLoc = locFrom(startLoc, startDir)
nextDir = startDir
loopLocs.append(nextLoc)

pathLength = 0
while nextLoc != startLoc:
    pathLength += 1
    nextDir = nextFrom(nextLoc, nextDir)
    nextLoc = locFrom(nextLoc, nextDir)
    loopLocs.append(nextLoc)

print(pathLength, (pathLength+1)/2)

numInside = 0
for r in range(1, len(grid)-1):
    row = grid[r]
    isInside = False
    lastCurve = ""
    for c in range(len(row)):
        loc = (r, c)
        if loc in loopLocs:
            char = row[c]
            if char=="S":
                char = startEquiv
            if char=="|":
                isInside = not(isInside)
            elif char=="-":
                pass
            elif char=="L":
                assert(lastCurve == "")
                lastCurve = "L"
            elif char=="F":
                assert(lastCurve == "")
                lastCurve = "F"
            elif char=="J":
                if lastCurve == "L":
                    lastCurve = ""
                elif lastCurve=="F":
                    lastCurve = ""
                    isInside = not(isInside)
                else:
                    raise Exception("Impossible curve?")
            elif char=="7":
                if lastCurve == "L":
                    lastCurve = ""
                    isInside = not(isInside)
                elif lastCurve=="F":
                    lastCurve = ""
                else:
                    raise Exception("Impossible curve?")
        else:
            if isInside:
                numInside += 1

print("Number inside:", numInside)