# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

data = open("day5.txt");
# data = open("day5_ex.txt")

def readSeeds(data):
    seeds = data.readline().strip().split()[1:]
    for n in range(len(seeds)):
        seeds[n] = int(seeds[n])
    data.readline()
    return seeds

def part2Seeds(seeds):
    newseeds = []
    for n in range(int(len(seeds)/2)):
        index = n*2
        newseeds.append((seeds[index], seeds[index+1]))
    return newseeds

def readMap(data):
    label = data.readline()
    print("Reading", label)
    line = data.readline().strip()
    retmap = []
    while line != "":
        vals = line.split()
        vals = [int(i) for i in vals]
        retmap.append(vals)
        line = data.readline().strip()
    return retmap

def getNext(val, mapping):
    for (dest, source, length) in mapping:
        if val >= source and val < source + length:
            return dest + val - source
    return val

def getNextRange(start, stop, mapping):
    unmapped = [(start, stop)]
    outranges = []
    for (dest, source, length) in mapping:
        for (start, stop) in unmapped:
            
        

seeds = readSeeds(data)
seed2soil = readMap(data)
soil2fert = readMap(data)
fert2water = readMap(data)
water2light = readMap(data)
light2temp = readMap(data)
temp2humid = readMap(data)
humid2loc = readMap(data)

minloc = 1e500
for seed in seeds:
    soil = getNext(seed, seed2soil)
    fert = getNext(soil, soil2fert)
    water = getNext(fert, fert2water)
    light = getNext(water, water2light)
    temp = getNext(light, light2temp)
    humid = getNext(temp, temp2humid)
    loc = getNext(humid, humid2loc)
    print(loc)
    minloc = min(minloc, loc)

print("minloc:", minloc)

newseeds = part2Seeds(seeds)
minloc = 1e500

for (start, length) in newseeds:
    print("range:", start, length)
    for seed in range(start, start+length):
        # print("seed:", seed)
        soil = getNext(seed, seed2soil)
        fert = getNext(soil, soil2fert)
        water = getNext(fert, fert2water)
        light = getNext(water, water2light)
        temp = getNext(light, light2temp)
        humid = getNext(temp, temp2humid)
        loc = getNext(humid, humid2loc)
        # print("loc:", loc)
        minloc = min(minloc, loc)

print("New minloc:", minloc)
