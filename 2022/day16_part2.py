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
    plans = []
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
            plans.append([link, newlink])
    while True:
        newplans = []
        for plan in plans:
            (__, newlinks) = valves[plan[-1]]
            if dest in newlinks:
                plan.append(dest)
                return plan
            for newlink in newlinks:
                if newlink in visited:
                    continue
                newplan = copy.copy(plan)
                newplan.append(newlink)
                newplans.append(newplan)
                visited.add(newlink)
        plans = newplans

def planIsNotEfficient(plan, valves, closedvalves):
    length = len(plan)
    if length==1:
        return False
    netPressure = valves[plan[-1]][0]
    for n in range(length):
        if plan[n] in closedvalves:
            altPressure = valves[plan[n]][0]*(length-n)
            if altPressure > netPressure:
                return True
    return False

def printPath(path):
    for (pos, action, pressure, closedvalves) in path:
        print(pos, action, pressure)
    print(closedvalves)

def getNewPathsFor(path, otherpath, newpaths):
    (pos, action, pressure, closedvalves) = path[-1]
    if len(closedvalves) == 0:
        #We're done; just hang out.
        newpaths.append(path)
        return
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
            if planIsNotEfficient(newaction, valves, closedvalves):
                continue
            #We travel along the action plan.
            newpos = newaction[0]
            newpath = copy.deepcopy(path)
            newpath.append((newpos, newaction, pressure, copy.deepcopy(closedvalves)))
            newpaths.append(newpath)
    else:
        #Continue heading to your destination:
        newaction = copy.copy(action)
        newaction.remove(newaction[0])
        newpos = newaction[0]
        newpath = copy.deepcopy(path)
        newpath.append((newpos, newaction, pressure, copy.deepcopy(closedvalves)))
        newpaths.append(newpath)

paths = [[(("AA", "start", 0, closedvalves),("AA", "start", 0, closedvalves))]]
for n in range(26):
    print("Step", n)
    newpaths = []
    for (mepath, elpath) in paths:
        mepaths = getNewPathsFor(mepath, elpath, newpaths)
        elpaths = getNewPathsFor(elpath, mepath, newpaths)
            
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

path1, path2
create new paths for path1, taking path2 into consideration
