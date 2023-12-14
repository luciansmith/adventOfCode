# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

part = 2
data = open("day8.txt");
# data = open("day8_ex.txt")
# data = open("day8_ex2.txt")

instructions = data.readline().strip()
data.readline()

rights = {}
lefts = {}
As = set()
allZs = set()
for line in data:
    at, dest = line.split(' = ')
    (left, right) = dest.split(',')
    left = left[1:]
    right = right[1:-2]
    rights[at] = right
    lefts[at] = left
    if at[-1] == 'A':
        As.add(at)
    if at[-1] == 'Z':
        allZs.add(at)
    
# print(rights, lefts)

if part==1:
    location = "AAA"
    steps = 0
    
    while location != "ZZZ":
        for ch in instructions:
            if ch=="L":
                location = lefts[location]
                steps += 1
            if ch=="R":
                location = rights[location]
                steps += 1
            if location == "ZZZ":
                break
    
    print(steps)


else:
    steps = 0
    walks = {}
    
    def getFirstZFrom(start, instructions, rights, lefts):
        steps = 0
        location = start
        while location not in allZs:
            for (n, ch) in enumerate(instructions):
                if ch=="L":
                    location = lefts[location]
                if ch=="R":
                    location = rights[location]
                steps += 1
                if location in allZs:
                    return steps
        return steps
    
    Zdists = []
    for start in As:
        Zdist = getFirstZFrom(start, instructions, rights, lefts)
        Zdists.append(Zdist)
        print("First Z from", start, Zdist)

    import math
    print(math.lcm(Zdists[0], Zdists[1], Zdists[2], Zdists[3], Zdists[4], Zdists[5]))


            
    