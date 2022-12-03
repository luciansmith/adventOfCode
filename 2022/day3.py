# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import numpy as np

def assign(sack, sackmap, label):
    ret = ""
    for ch in sack:
        if ch in sackmap and sackmap[ch] != label:
            ret = ch
            sackmap[ch] = "both"
        else:
            sackmap[ch]= label
    return ret

def getVal(ch):
    val = ord(ch) - ord('a') + 1
    if val<=0 or val > 26:
        val = ord(ch) - ord('A') + 27
    return val

def findCommon(groups):
    (one, two, three) = groups
    for ch in three:
        if ch in one and ch in two:
            return ch
    raise("No common found.")

sum_priorities = 0
badge_priorities = 0
groups = []
for line in open("day3_input.txt"):
#for line in open("day3_example.txt"):
    line = line.strip()
    groups.append(line)
    half = round(len(line)/2)
    lsack = line[0:half]
    rsack = line[half:]
    sackmap = {}
    assign(lsack, sackmap, "left")
    both = assign(rsack, sackmap, "right")
    sum_priorities += getVal(both)
    #print(both, getVal(both))
    if len(groups) == 3:
        badge = findCommon(groups)
        badge_priorities += getVal(badge)
        print(badge, getVal(badge))
        groups = []
if len(groups) == 3:
    badge = findCommon(groups)
    badge_priorities += getVal(badge)
    print(badge, getVal(badge))

print(sum_priorities)
print(badge_priorities)