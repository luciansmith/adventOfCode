# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import copy
import numpy as np

pit = [[2]*7]

#Rocks are upside down so leading edge is always 0,0
rock1 = [[1,1,1,1]]
rock2 = [[0,1,0],
         [1,1,1],
         [0,1,0]]
rock3 = [[1,1,1],
         [0,0,1],
         [0,0,1]]
rock4 = [[1],
         [1],
         [1],
         [1]]
rock5 = [[1,1],
         [1,1]]

rocks = [rock1, rock2, rock3, rock4, rock5]

jets = ""
#for line in open("day17_input.txt"):
for line in open("day17_example.txt"):
    line = line.strip()
    jets = jets + line

def printPit(pit):
    for n in range(len(pit)-1, -1, -1):
        print(pit[n])
    print()

def checkRight(pit, rowmin, rowmax):
    for row in range(rowmin, rowmax):
        for col in range(len(pit[row])):
            if pit[row][col] == 1:
                if col == 6:
                    return False
                if pit[row][col+1] == 2:
                    return False
    return True

def checkLeft(pit, rowmin, rowmax):
    for row in range(rowmin, rowmax):
        for col in range(len(pit[row])):
            if pit[row][col] == 1:
                if col == 0:
                    return False
                if pit[row][col-1] == 2:
                    return False
    return True

def checkDown(pit, rowmin, rowmax):
    for row in range(rowmin, rowmax):
        for col in range(len(pit[row])):
            if pit[row][col] == 1:
                if pit[row-1][col] == 2:
                    return False
    return True

def moveOnesRight(pit, rowmin, rowmax):
    for row in range(rowmin, rowmax):
        for col in range(len(pit[row])-1, -1, -1):
            if pit[row][col] == 1:
                pit[row][col+1] = 1
                pit[row][col] = 0

def moveOnesLeft(pit, rowmin, rowmax):
    for row in range(rowmin, rowmax):
        for col in range(len(pit[row])):
            if pit[row][col] == 1:
                pit[row][col-1] = 1
                pit[row][col] = 0
    
def moveOnesDown(pit, rowmin, rowmax):
    for row in range(rowmin, rowmax):
        for col in range(len(pit[row])):
            if pit[row][col] == 1:
                pit[row-1][col] = 1
                pit[row][col] = 0

def rockify(pit, rowmin, rowmax):    
    for row in range(rowmin, rowmax):
        for col in range(len(pit[row])):
            if pit[row][col] == 1:
                pit[row][col] = 2

def trimTop(pit):
    while 2 not in pit[-1]:
        pit.remove(pit[-1])

def trimBottom(pit):
    lowest = len(pit)
    for col in range(7):
        row = len(pit)-1
        while pit[row][col] == 0:
            row -= 1
        if row<lowest:
            lowest = row
    return lowest
    

rockIndex = 0
jetIndex = 0
removedPit = 0
jetZeroPit = []
n = -1
targetN = 1000000000000
while n < targetN:
    n += 1
    if not n % 100000:
        print(n)
    rock = rocks[rockIndex]
    rockIndex += 1
    if rockIndex == 5:
        rockIndex = 0
    for nr in range(3+len(rock)):
        row = [0]*7
        pit.append(row)
    for rr in range(len(rock)):
        rockrow = rock[rr]
        for rc in range(len(rockrow)):
            pit[-(len(rock))+rr][rc+2] = rockrow[rc]
    # printPit(pit)
    
    falling = True
    rowmin = len(pit)-len(rock)-1
    rowmax = len(pit)
    skipRepeat = False
    while(falling):
        jet = jets[jetIndex]
        jetIndex += 1
        if jetIndex == len(jets):
            print("Jet repeat", n)
            printPit(pit)
            pitcopy = copy.deepcopy(pit)
            if len(jetZeroPit) and pitcopy == jetZeroPit[0]:
                print("Repeat at", n)
                skipRepeat = True
                loop = n - jetZeroPit[1]
                skip = targetN-n
                skip = np.floor(skip/loop)
                n += skip * loop
                removedPit += skip * (removedPit - jetZeroPit[2])
            else:
                jetZeroPit = (pitcopy, n, removedPit)
            jetIndex = 0
        
        if jet == ">":
            if checkRight(pit, rowmin, rowmax):
                moveOnesRight(pit, rowmin, rowmax)
        elif jet == "<":
            if checkLeft(pit, rowmin, rowmax):
                moveOnesLeft(pit, rowmin, rowmax)
        falling = checkDown(pit, rowmin, rowmax)
        if falling:
            moveOnesDown(pit, rowmin, rowmax)
            rowmin -= 1
            rowmax -= 1
#        printPit(pit)
    rockify(pit, rowmin, rowmax)
    trimTop(pit)
    # printPit(pit)
    removed = trimBottom(pit)
    if (removed):
        removedPit += removed
        pit = pit[removed:]
#    print("Previous:")
#    printPit(prevPit)
        

print(len(pit)-1, removedPit, removedPit+len(pit)-1)