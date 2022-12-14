# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""
import math

elevations = []
start = ()
for line in open("day12_input.txt"):
#for line in open("day12_example.txt"):
    if "S" in line:
        start = (len(elevations), line.find("S"))
        line = line.replace("S", "a")
    elevations.append(line.strip())

def takeStep(chains):
    newchains = []
    for chain in chains:
        lastpos = chain[-1]
        (row, col) = lastpos
        up = (lastpos[0]-1, lastpos[1])
        down = (lastpos[0]+1, lastpos[1])
        right = (lastpos[0], lastpos[1]+1)
        left = (lastpos[0], lastpos[1]-1)
        
        lastval = elevations[row][col]
        if lastval == "z":
            print("close!")
        if up not in visited and up[0] >=0:
            upval = elevations[up[0]][up[1]]
            if upval == "E":
                if ord("z") - ord(lastval) <= 1:
                    chain.append(up)
                    return [chain], True
            elif ord(upval) - ord(lastval) <= 1:
                newchain = chain.copy()
                newchain.append(up)
                visited.add(up)
                newchains.append(newchain)
            
        if down not in visited and down[0] < len(elevations):
            downval = elevations[down[0]][down[1]]
            if downval == "E":
                if ord("z") - ord(lastval) <= 1:
                    chain.append(down)
                    return [chain], True
            elif ord(downval) - ord(lastval) <= 1:
                newchain = chain.copy()
                newchain.append(down)
                visited.add(down)
                newchains.append(newchain)
            
        if right not in visited and right[1] < len(elevations[0]):
            rightval = elevations[right[0]][right[1]]
            if rightval == "E":
                if ord("z") - ord(lastval) <= 1:
                    chain.append(right)
                    return [chain], True
            elif ord(rightval) - ord(lastval) <= 1:
                newchain = chain.copy()
                newchain.append(right)
                visited.add(right)
                newchains.append(newchain)
            
        if left not in visited and left[1] >= 0:
            leftval = elevations[left[0]][left[1]]
            if leftval == "E":
                if ord("z") - ord(lastval) <= 1:
                    chain.append(left)
                    return [chain], True
            elif ord(leftval) - ord(lastval) <= 1:
                newchain = chain.copy()
                newchain.append(left)
                visited.add(left)
                newchains.append(newchain)
        
    return newchains, False
            
def printChainEnds(chains):
    print("Chain ends: ", end="")
    for chain in chains:
        print(elevations[chain[-1][0]][chain[-1][1]], ":", chain[-1], " ",end="")
    print()

chains = [[start]]
visited = set()
visited.add(start)

chains, finished = takeStep(chains)
while not finished:
    chains, finished = takeStep(chains)
    assert(len(chains))
    printChainEnds(chains)
    # print(len(chains))    

print("Steps: ", len(chains[0])-1)

visited = set()
chains = []
for row in range(len(elevations)):
    for col in range(len(elevations[row])):
        if elevations[row][col] == "a":
            chains.append([(row, col)])
            visited.add((row, col))

chains, finished = takeStep(chains)
while not finished:
    chains, finished = takeStep(chains)
    assert(len(chains))
    # printChainEnds(chains)
    # print(len(chains))    

print("Steps: ", len(chains[0])-1)
