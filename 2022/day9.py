# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import numpy as np

def tailCatchUp(head, tail):
    rowdiff = head[0]-tail[0]
    coldiff = head[1]-tail[1]
    if abs(rowdiff) == 2 and abs(coldiff) == 2:
        tail[1] += round(coldiff/2)
        tail[0] += round(rowdiff/2)
    elif abs(rowdiff) == 2:
        tail[1] = head[1]
        tail[0] += round(rowdiff/2)
    elif abs(coldiff) == 2:
        tail[0] = head[0]
        tail[1] += round(coldiff/2)

def execute(line, head, tail, tailvisited):
    (direc, move) = line.split()
    move = int(move)
    movevec = [0, 0]
    if direc=="R":
        movevec = [1, 0]
    if direc=="L":
        movevec = [-1, 0]
    if direc=="U":
        movevec = [0, 1]
    if direc=="D":
        movevec = [0, -1]
    for n in range(move):
        head[0] += movevec[0]
        head[1] += movevec[1]
        tailCatchUp(head, tail[0])
        for n in range(len(tail)-1):
            tailCatchUp(tail[n], tail[n+1])
        tailvisited.add(tuple(tail[8]))
    

head = [0, 0]
longtail = []
for n in range(9):
    longtail.append([0, 0])
tailvisited = set()

for line in open("day9_input.txt"):
#for line in open("day9_example.txt"):
    line = line.strip()
    execute(line, head, longtail, tailvisited)

print(tailvisited)
print("Total positions:", len(tailvisited))
