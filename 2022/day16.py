# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""
import copy
import time
begin = time.perf_counter()

import re

valves = {}
closedvalves = set()

for  line in open("day16_input.txt"):
#for line in open("day16_example.txt"):
    lvec = re.split('=|,|;| ',line.strip())
    valve = lvec[1]
    rate = int(lvec[5])
    links = [lvec[11]]
    nextl = 13
    while len(lvec) > nextl:
        links.append(lvec[nextl])
        nextl += 2
    valves[valve] = (rate, links)
    if rate != 0:
        closedvalves.add(valve)

def travelFromTo(curr, dest, valves):
    (__, links) = valves[curr]
    if dest in links:
        return [dest]
    paths = []
    visited = {curr}
    for link in links:
        (__, newlinks) = valves[link]
        if dest in newlinks:
            return [link, dest]
        for newlink in newlinks:
            visited.add(link)
            if newlink in visited:
                continue
            visited.add(newlink)
            paths.append([link, newlink])
    while True:
        newpaths = []
        for path in paths:
            (__, newlinks) = valves[path[-1]]
            if dest in newlinks:
                path.append(dest)
                return path
            for newlink in newlinks:
                if newlink in visited:
                    continue
                newpath = copy.copy(path)
                newpath.append(newlink)
                newpaths.append(newpath)
                visited.add(newlink)
        paths = newpaths

def pathIsNotEfficient(path, valves, closedvalves):
    length = len(path)
    if length==1:
        return False
    netPressure = valves[path[-1]][0]
    for n in range(length):
        if path[n] in closedvalves:
            altPressure = valves[path[n]][0]*(length-n)
            if altPressure > netPressure:
                return True
    return False

def printPath(path):
    for (pos, action, pressure, closedvalves) in path:
        print(pos, action, pressure)
    print(closedvalves)

paths = [[("AA", "start", 0, closedvalves)]]
for n in range(30):
    print("Step", n)
    newpaths = []
    for path in paths:
        (pos, action, pressure, closedvalves) = path[-1]
        if len(closedvalves) == 0:
            #We're done; just hang out.
            newpaths.append(path)
            continue
        (rate, links) = valves[pos]
        if pos == action[-1]:
            #Open the valve
            newpath = copy.deepcopy(path)
            newpressure = rate * (29 - n)
            newclosedvalves = copy.deepcopy(closedvalves)
            newclosedvalves.remove(pos)
            newpath.append((pos, "open", pressure+newpressure, newclosedvalves))
            newpaths.append(newpath)
        elif action == "open" or action == "start":
            for valve in closedvalves:
                #Head to one of the closed valves:
                newaction = travelFromTo(pos, valve, valves)
                if pathIsNotEfficient(newaction, valves, closedvalves):
                    continue
                newpos = newaction[0]
                #We travel to link.
                newpath = copy.deepcopy(path)
                newpath.append((newpos, newaction, pressure, copy.deepcopy(closedvalves)))
                newpaths.append(newpath)
        else:
            #Continue heading to your destination:
            newaction = copy.copy(action)
            newaction.remove(newaction[0])
            newpos = newaction[0]
            # #If the place you're heading has a lower pressure
            # # than where you are, and it's closed, this path
            # # is not worth pursuing.
            # if newpos in closedvalves:
            #     herepress = valves[newpos][0]
            #     destpress = valves[action[-1]][0]
            #     if herepress > destpress:
            #         continue
            
            #Otherwise, travel to link.
            newpath = copy.deepcopy(path)
            newpath.append((newpos, newaction, pressure, copy.deepcopy(closedvalves)))
            newpaths.append(newpath)
            
    # for path in newpaths:
    #     printPath(path)
    paths = newpaths

mostpressure = 0
for path in paths:
    (__, __, pressure, __) = path[-1]
    if pressure > mostpressure:
        mostpressure = pressure
        print(path)

print(mostpressure)