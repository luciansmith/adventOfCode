# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import numpy as np

overlaps = 0

def checkAll(e1, e2):
    if e2[1] <= e1[1]:
        return 1
    return 0

def checkSome(e1, e2):
    if e2[0] > e1[1]:
        print("don't overlap:", e1, e2)
        return 0
    if e2[0] <= e1[1]:
        return 1
    if e2[1] <= e1[1]:
        return 1
    print("don't overlap:", e1, e2)
    return 0



for line in open("day4_input.txt"):
#for line in open("day4_example.txt"):
    (elf1, elf2) = line.strip().split(',')
    elf1 = elf1.split('-')
    elf2 = elf2.split('-')
    elf1 = int(elf1[0]), int(elf1[1])
    elf2 = int(elf2[0]), int(elf2[1])
    if elf1[0] == elf2[0]:
        overlaps += 1
        
    elif elf1[0] < elf2[0]:
        overlaps += checkSome(elf1, elf2)
    else:
        overlaps += checkSome(elf2, elf1)
    print (elf1, elf2, overlaps)
        

print(overlaps)
