# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

data = open("day12.txt");
# data = open("day12_ex.txt")

part = 2

total = 0

def matchesAt(springs, group):
    if len(springs) < group:
        return False
    for pos in range(group):
        if springs[pos] == ".":
            return False
    if len(springs) > pos+1 and springs[pos+1] == "#":
        return False
    return True

knownMatches = {}

def countMatches(springs, groups):
    knownIndex = (springs, tuple(groups))
    if knownIndex in knownMatches:
        return knownMatches[knownIndex]
    matches = 0
    if len(groups) == 0:
        return 0
    maxStart = len(springs) - len(groups) + 1
    for g in groups:
        maxStart -= g
    firstGroup = groups[0]
    for n in range(0, maxStart+1):
        subspring = springs[n:]
        if matchesAt(subspring, firstGroup):
            if len(groups) == 1:
                if "#" not in subspring[firstGroup+1:]:
                    matches += 1
            else:
                matches += countMatches(subspring[firstGroup+1:], groups[1:])
        if subspring[0] == "#":
            knownMatches[knownIndex] = matches
            return matches
    knownMatches[knownIndex] = matches
    return matches
    
        
    

for line in data:
    (springs, groups) = line.strip().split(' ')
    if part==2:
        springs = 5*(springs + "?")
        groups = 5*(groups + ",")
        springs = springs[:-1]
        groups = groups[:-1]
    groups = groups.split(',')
    groups = [int(i) for i in groups]
    rowtotal = countMatches(springs, groups)
    total += rowtotal
    print(springs, groups)
    print(rowtotal)

print("total:", total)

