# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import numpy as np

pairs = []
fullList = []

pairfile = open("day13_input.txt")
#pairfile = open("day13_example.txt")

line = pairfile.readline()
while line != "":
    pair = []
    left = 0
    right = 0
    exec("left = " + line)
    exec("right = " + pairfile.readline())
    pairs.append([left, right])
    fullList.append(left)
    fullList.append(right)
    pairfile.readline()
    line = pairfile.readline().strip()
    
def compare(left, right):
    if type(left) == int and type(right) == int:
        if left == right:
            return 0
        if left < right:
            return 1
        return -1
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    for n in range(len(left)):
        if n > len(right)-1:
            return -1
        result = compare(left[n], right[n])
        if result == 1:
            return 1
        if result == -1:
            return -1
    if len(left) == len(right):
        return 0
    return 1

# print(pairs)
correct = []
for n in range(len(pairs)):
    if compare(pairs[n][0], pairs[n][1]) == 1:
        correct.append(n+1)

print(correct)
print(sum(correct))


#Part 2:
    
def negCompare(left, right):
    return -compare(left, right)

from functools import cmp_to_key

fullList.append([[2]])
fullList.append([[6]])
full_sorted = sorted(fullList, key=cmp_to_key(negCompare))

key = 1
for n in range(len(full_sorted)):
    #print(full_sorted[n])
    if full_sorted[n] == [[2]]:
        key = key * (n+1)
        print(n+1)
    if full_sorted[n] == [[6]]:
        key = key * (n+1)
        print(n+1)
print(key)