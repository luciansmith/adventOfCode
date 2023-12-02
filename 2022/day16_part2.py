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

def pathIsNotEfficient(path, valves, closedvalves, othergoal, n):
    length = len(path)
    if length >= 25-n:
        return True
    if length==1:
        return False
    netPressure = valves[path[-1]][0]
    for n in range(length):
        if path[n] in closedvalves and path[n] != othergoal:
            altPressure = valves[path[n]][0]*(length-n)
            if altPressure > netPressure:
                return True
    return False

def cullPaths(paths, n, valves):
    newpaths = []
    bestPressure = 0
    for path in paths:
        (pos1, action1, pos2, action2, pressure, closedvalves) = path[-1]
        if pressure > bestPressure:
            bestPressure = pressure
    for path in paths:
        (pos1, action1, pos2, action2, pressure, closedvalves) = path[-1]
        pressurelist = []
        for valve in closedvalves:
            pressurelist.append(valves[valve][0])
        pressurelist.sort()
        possiblePressure = 0
        for loop in range(0, len(pressurelist), 2):
            #Pretend we can get to them as efficiently as possible:
            possiblePressure += pressurelist[loop]*(25-n)
            try:
                possiblePressure += pressurelist[loop+1]*(25-n)
            except:
                pass
        if possiblePressure + pressure >= bestPressure:
            newpaths.append(path)
    return newpaths

def isPathUnique(path):
    lastpath = path[-1]
    if type(lastpath[1]) == list:
        if(lastpath[1][-1] == lastpath[3][-1]):
            printPath(path)
            return False
    return True
            

def printPath(path):
    for (pos1, action1, pos2, action2, pressure, closedvalves) in path:
        print(pos1, action1, pos2, action2, pressure)
    print(closedvalves)

paths = [[("AA", "start", "AA", "start", 0, closedvalves)]]
for n in range(26):
    print("Step", n)
    newpaths = []
    for path in paths:
        (pos1, action1, pos2, action2, pressure, closedvalves) = path[-1]
        if len(closedvalves) == 0:
            #We're done; just hang out.
            newpaths.append(path)
            continue
        (rate1, links1) = valves[pos1]
        (rate2, links2) = valves[pos2]
        newpos1 = ""
        newaction1 = ""
        newpos2 = ""
        newaction2 = ""
        newpressure = pressure
        newclosedvalves = copy.deepcopy(closedvalves)
        newpath = copy.deepcopy(path)
        
        #Deal with human:
        posactionlist1 = []
        if pos1 == action1[-1]:
            #Open the valve
            newpressure += rate1 * (25 - n)
            newclosedvalves.remove(pos1)
            newpos1 = pos1
            newaction1 = "open"
        elif action1 == "open" or action1 == "start" or action1 == "stop":
            othergoal = ""
            if (len(action2)):
                othergoal = action2[-1]
            for valve in closedvalves:
                #Head to one of the closed valves:
                if valve == othergoal:
                    #The elephant is already handling this one.
                    if len(closedvalves) == 1:
                        #check to see if we can get there first.
                        newaction = travelFromTo(pos1, valve, valves)
                        if len(newaction) < len(action2)-1:
                            #I dunno; maybe deal with it?
                            print(newaction, action2)
                            # assert(False)
                        newpos1 = pos1
                        newaction1 = "stop"
                    continue
                newaction = travelFromTo(pos1, valve, valves)
                if pathIsNotEfficient(newaction, valves, closedvalves, othergoal, n):
                    continue
                newpos = newaction[0]
                #We travel to link.
                posactionlist1.append((newpos, newaction))
            if len(posactionlist1) == 0:
                newpos1 = pos1
                newaction1 = "stop"
        else:
            #Continue heading to your destination:
            newaction1 = copy.copy(action1)
            newaction1.remove(newaction1[0])
            newpos1 = newaction1[0]

        #Deal with elephant:
        if len(newclosedvalves) == 0:
            #We're done; just hang out.
            newpath.append((newpos1, newaction1, pos2, action2, newpressure, newclosedvalves))
            newpaths.append(newpath)
            newpaths.append(path)
            continue
        posactionlist2 = []
        if pos2 == action2[-1]:
            #Open the valve
            newpressure += rate2 * (25 - n)
            newclosedvalves.remove(pos2)
            newpos2 = pos2
            newaction2 = "open"
        elif action2 == "open" or action2 == "start" or action2 == "stop":
            othergoal = ""
            if len(newaction1):
                othergoal = newaction1[-1]
            for valve in newclosedvalves:
                #Head to one of the closed valves:
                if valve == othergoal:
                    #The human has this one covered
                    if len(closedvalves) == 1:
                        #check to see if we can get there first.
                        newaction = travelFromTo(pos2, valve, valves)
                        if len(newaction) < len(action2)-1:
                            #I dunno; maybe deal with it?
                            print(newaction, action2)
                            # assert(False)
                        newpos2 = pos2
                        newaction2 = "stop"
                    continue
                newaction = travelFromTo(pos2, valve, valves)
                if pathIsNotEfficient(newaction, valves, newclosedvalves, othergoal, n):
                    # print("Not", newaction)
                    continue
                newpos = newaction[0]
                #We travel to link.
                posactionlist2.append((newpos, newaction))
            if len(posactionlist2) == 0:
                newpos2 = pos2
                newaction2 = "stop"
        else:
            #Continue heading to your destination:
            newaction2 = copy.copy(action2)
            newaction2.remove(newaction2[0])
            newpos2 = newaction2[0]

        #Deal with splitting of new paths:
        if len(posactionlist1) == 1:
            newpos1 = posactionlist1[0][0]
            newaction1 = posactionlist1[0][1]
            posactionlist1.clear()
        if len(posactionlist2) == 1:
            newpos2 = posactionlist2[0][0]
            newaction2 = posactionlist2[0][1]
            posactionlist2.clear()
            if len(newaction1) and newaction2[-1] == newaction1[-1]:
                if len(newaction2) > len(newaction1):
                    newaction1 = "stop"
                else:
                    newaction2 = "stop"
        assert(len(newaction1) or len(posactionlist1))
        assert(len(newaction2) or len(posactionlist2))
        if len(posactionlist1) == 0 and len(posactionlist2) == 0:
            newpath.append((newpos1, newaction1, newpos2, newaction2, newpressure, newclosedvalves))
            assert(isPathUnique(newpath))
            newpaths.append(newpath)
        elif len(posactionlist2) == 0:
            for (newpos1, newaction1) in posactionlist1:
                if newaction1[-1] == newaction2[-1]:
                    continue
                newpath = copy.deepcopy(path)
                newpath.append((newpos1, newaction1, newpos2, newaction2, newpressure, copy.deepcopy(newclosedvalves)))
                assert(isPathUnique(newpath))
                newpaths.append(newpath)
        elif len(posactionlist1) == 0:
            for (newpos2, newaction2) in posactionlist2:
                if newaction1[-1] == newaction2[-1]:
                    continue
                newpath = copy.deepcopy(path)
                newpath.append((newpos1, newaction1, newpos2, newaction2, newpressure, copy.deepcopy(newclosedvalves)))
                assert(isPathUnique(newpath))
                newpaths.append(newpath)
        else:
            #Both human and elephant have a new set of places to visit.
            if pos1 == pos2:
                #If we're starting from the same place, divvy things up randomly
                for posaction in posactionlist2:
                    if posaction in posactionlist1:
                        continue
                    else:
                        assert(False)
                        #How?  But OK.
                        posactionlist1.append(posaction)
                for n in range(len(posactionlist1)-1):
                    (newpos1, newaction1) = posactionlist1[n]
                    for m in range(n+1, len(posactionlist1)):
                        (newpos2, newaction2) = posactionlist1[m]
                        newpath = copy.deepcopy(path)
                        newpath.append((newpos1, newaction1, newpos2, newaction2, newpressure, copy.deepcopy(newclosedvalves)))
                        assert(isPathUnique(newpath))
                        newpaths.append(newpath)
            else:
                #If we start from different places, go all places unless other is already going there.
                for (newpos1, newaction1) in posactionlist1:
                    dest = newaction1[-1]
                    for (newpos2, newaction2) in posactionlist2:
                        if dest == newaction2[-1]:
                            #Don't both go to the same place
                            continue
                        newpath = copy.deepcopy(path)
                        newpath.append((newpos1, newaction1, newpos2, newaction2, newpressure, copy.deepcopy(newclosedvalves)))
                        assert(isPathUnique(newpath))
                        newpaths.append(newpath)
                        
                    
        
    # for path in newpaths:
    #     printPath(path)
    # paths = cullPaths(newpaths, n, valves)
    paths = newpaths



mostpressure = 0
for path in paths:
    (__, __, __, __, pressure, __) = path[-1]
    if pressure > mostpressure:
        mostpressure = pressure
        printPath(path)

print(mostpressure)
#2024 is too low