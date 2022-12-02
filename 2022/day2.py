# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import numpy as np

def translate(sheet):
    (them, me) = sheet
    if them=="A":
        them = 1
    elif them=="B":
        them = 2
    elif them=="C":
        them = 3
    if me=="X":
        me=1
    elif me=="Y":
        me=2
    elif me=="Z":
        me=3
    return (them, me)

def translateForReal(sheet):
    (them, me) = sheet
    if them=="A":
        them = 1
    elif them=="B":
        them = 2
    elif them=="C":
        them = 3
    if me=="X":
        me=them-1
    elif me=="Y":
        me=them
    elif me=="Z":
        me=them+1
    if me==0:
        me = 3
    if me==4:
        me = 1
    return (them, me)
        

def calcScore(opponent, me):
    if opponent == me:
        return me + 3
    diff = me - them
    if diff == 1:
        return me + 6
    if diff == -1:
        return me
    if diff == 2:
        return me
    if diff == -2:
        return me + 6
    raise("Unaccounted-for score")

score = 0
for line in open("day2_input.txt"):
#for line in open("day2_example.txt"):
    lvec = line.strip().split()
    (them, me) = translateForReal(lvec)
    score += calcScore(them, me)
    print(them, me, score)

print(score)