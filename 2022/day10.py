# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import numpy as np

values = [1]
for line in open("day10_input.txt"):
#for line in open("day10_example.txt"):
    lvec = line.strip().split()
    if lvec[0] == "noop":
        values.append(values[-1])
    elif lvec[0] == "addx":
        val = int(lvec[1])
        values.append(values[-1])
        values.append(values[-1] + val)

strsum = 0
for n in range(19, 220, 40):
    sigstr = (n+1) * values[n]
    strsum += sigstr
    print(n+1, sigstr)

print(strsum)

#Part 2:
def drawScr(scr):
    for n in range(6):
        print(scr[n*40:(n*40)+39])
    
screen = ""
currstr = 0
pos = 0
row = 0
for n in range(len(values)):
    if n>=(row+1)*40:
        row += 1
    pos = n - row*40
    if abs(pos - values[n]) < 2:
        screen = screen + "#"
    else:
        screen = screen + "."

drawScr(screen)
