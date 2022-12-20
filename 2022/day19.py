# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import copy
import numpy as np
import math

blueprints = []

for line in open("day19_input.txt"):
#for line in open("day19_example.txt"):
    lvec = line.strip().split()
    blueprint = {}
    blueprint[lvec[3]] = int(lvec[6])
    blueprint[lvec[9]] = int(lvec[12])
    blueprint[lvec[15]] = (int(lvec[18]), int(lvec[21]))
    blueprint[lvec[24]] = (int(lvec[27]), int(lvec[30]))
    
    blueprints.append(blueprint)
    
scores = []

def printPaths(paths):
    for path in paths:
        print(path)

def getOptions(robots, supplies, target, blueprint):
    options = []
    #Waiting is always an option:
    waitSupply = copy.copy(supplies)
    for n, robot in enumerate(robots):
        waitSupply[n] += robot
    
    oreRcost = blueprint['ore']
    clayRcost = blueprint['clay']
    obsRcost = blueprint['obsidian']
    geoRcost = blueprint['geode']
    maxOreCost = max(oreRcost, clayRcost)
    if robots[1]:
        maxOreCost = max(maxOreCost, obsRcost[0])
    if robots[2]:
        maxOreCost = max(maxOreCost, geoRcost[0])
    maxClayCost = obsRcost[1]
    maxObsCost = geoRcost[1]

    canWaitForSomething = False
    
    #Always build a geode robot if we can:
    if target == "none" or target == "geode":
        if supplies[0] >= geoRcost[0] and supplies[2] >= blueprint['geode'][1]:
            newSupply = copy.copy(waitSupply)
            newSupply[0] -= geoRcost[0]
            newSupply[2] -= geoRcost[1]
            newGeodeRobot = copy.copy(robots)
            newGeodeRobot[3] += 1
            options.append((newGeodeRobot, newSupply, "none"))
            return options
        elif robots[2] > 0:
            options.append((copy.copy(robots), copy.copy(waitSupply), "geode"))
    
    #If not, build an obsidian robot if we can, or wait:
    if target == "none" or target == "obsidian":
        if robots[2] < maxObsCost:
            if supplies[0] >= obsRcost[0] and supplies[1] >= obsRcost[1]:
                newSupply = copy.copy(waitSupply)
                newSupply[0] -= obsRcost[0]
                newSupply[1] -= obsRcost[1]
                newObsidianRobot = copy.copy(robots)
                newObsidianRobot[2] += 1
                options.append((newObsidianRobot, newSupply, "none"))
                if not canWaitForSomething:
                    return options
            elif robots[1] > 0:
                options.append((copy.copy(robots), copy.copy(waitSupply), "obsidian"))
    
    #Otherwise, an option is to build a clay robot:
    if target == "none" or target == "clay":
        if robots[1] < maxClayCost:
            if supplies[0] >= clayRcost:
                newSupply = copy.copy(waitSupply)
                newSupply[0] -= clayRcost
                newClayRobot = copy.copy(robots)
                newClayRobot[1] += 1
                options.append((newClayRobot, newSupply, "none"))
            else:
                options.append((copy.copy(robots), copy.copy(waitSupply), "clay"))
    
    #Or we could possibly build an ore robot:
    if target == "none" or target == "ore":
        if robots[0] < maxOreCost:
            if supplies[0] >= oreRcost:
                newSupply = copy.copy(waitSupply)
                newSupply[0] -= oreRcost
                newOreRobot = copy.copy(robots)
                newOreRobot[0] += 1
                options.append((newOreRobot, newSupply, "none"))
            else:
                options.append((copy.copy(robots), copy.copy(waitSupply), "ore"))
    
    return options

def cullBadChoices(paths, n):
    mostGeodes = 0
    for (robots, supplies, target) in paths:
        geodes = robots[3]*(24-n) + supplies[3]
        if geodes > mostGeodes:
            mostGeodes = geodes
    newpaths = []
    for path in paths:
        (robots, supplies, target) = path
        possiblegeodes = supplies[3] + robots[3]*(24-n) + sum(range(n))
        if possiblegeodes >= mostGeodes:
            newpaths.append(path)
    return newpaths

qualityScores = []
for b, blueprint in enumerate(blueprints):
    supplies = [0, 0, 0, 0]
    robots = [1, 0, 0, 0]
    paths = [(robots, supplies, "none"),]
    for n in range(24):
        print(n)
        newpaths = []
        for (robots, supplies, target) in paths:
            options = getOptions(robots, supplies, target, blueprint)
            for option in options:
                if option not in newpaths:
                    newpaths.append(option)
        paths = cullBadChoices(newpaths, n+1)
        #paths = newpaths
        # printPaths(paths)
    # printPaths(paths)
    mostObsidian = 0
    for option in newpaths:
        if option[1][3] > mostObsidian:
            mostObsidian = option[1][3]
    qualityScores.append((b+1)*mostObsidian)

print(qualityScores, sum(qualityScores))
    