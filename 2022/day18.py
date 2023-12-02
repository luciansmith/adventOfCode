# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import copy
import numpy as np

cubes = set()
airSet = set()
airNeighbors = {}

for line in open("day18_input.txt"):
#for line in open("day18_example.txt"):
    lvec = line.strip().split(",")
    cubes.add((int(lvec[0]), int(lvec[1]), int(lvec[2])))
 
exposed = 0
for (x, y, z) in cubes:
    if (x+1, y, z) not in cubes:
        exposed += 1
        airSet.add((x+1, y, z))
    if (x, y+1, z) not in cubes:
        exposed += 1
        airSet.add((x, y+1, z))
    if (x, y, z+1) not in cubes:
        exposed += 1
        airSet.add((x, y, z+1))
    if (x-1, y, z) not in cubes:
        exposed += 1
        airSet.add((x-1, y, z))
    if (x, y-1, z) not in cubes:
        exposed += 1
        airSet.add((x, y-1, z))
    if (x, y, z-1) not in cubes:
        exposed += 1
        airSet.add((x, y, z-1))

print(exposed)


for air in airSet:
    (x, y, z) = air
    airNeighbors[air] = [0, []]
    if (x+1, y, z) in cubes:
        airNeighbors[air][0] += 1
    if (x+1, y, z) in airSet:
        airNeighbors[air][1].append((x+1, y, z))

    if (x, y+1, z) in cubes:
        airNeighbors[air][0] += 1
    if (x, y+1, z) in airSet:
        airNeighbors[air][1].append((x, y+1, z))

    if (x, y, z+1) in cubes:
        airNeighbors[air][0] += 1
    if (x, y, z+1) in airSet:
        airNeighbors[air][1].append((x, y, z+1))

    if (x-1, y, z) in cubes:
        airNeighbors[air][0] += 1
    if (x-1, y, z) in airSet:
        airNeighbors[air][1].append((x-1, y, z))

    if (x, y-1, z) in cubes:
        airNeighbors[air][0] += 1
    if (x, y-1, z) in airSet:
        airNeighbors[air][1].append((x, y-1, z))

    if (x, y, z-1) in cubes:
        airNeighbors[air][0] += 1
    if (x, y, z-1) in airSet:
        airNeighbors[air][1].append((x, y, z-1))
    
def isPocket(air, airNeighbors, used):
    (cubes, airs) = airNeighbors[air]
    for neighborAir in airs:
        if neighborAir in used:
            continue
        used.add(neighborAir)
        if isPocket(neighborAir, airNeighbors, used):
            continue
        else:
            return False
    return True

allUsed = set()
openAir = set()
for air in airNeighbors:
    (cubes, airs) = airNeighbors[air]
    if cubes == 6:
        exposed -= 6
    elif cubes + len(airs) == 6:
        numPockets = 0
        for neighborAir in airs:
            if neighborAir in allUsed:
                numPockets += 1
            elif neighborAir in openAir:
                continue
            else:
                used = {air}
                if isPocket(neighborAir, airNeighbors, used):
                    numPockets += 1
                    for usedAir in used:
                        allUsed.add(usedAir)
                else:
                    for usedAir in used:
                        openAir.add(usedAir)
        if cubes + numPockets == 6:
            exposed -= cubes
            
            
print(exposed)
#2882 is too high