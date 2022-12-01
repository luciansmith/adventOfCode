import numpy as np

example = False

filename = "day22_input.txt"

if example:
    filename = "day22_example.txt"


def checkCoor(coor, rules, default):
    for (toggle, axes) in rules:
        if coor[0] in axes[0] and coor[1] in axes[1] and coor[2] in axes[2]:
                return toggle
    return default

def setupCubeSets(rules):
    cubesOn = set()
    cubesOff = set()
    for (toggle, axes) in rules:
        print("Checking", toggle, axes)
        if toggle=="on":
            for x in axes[0]:
                for y in axes[1]:
                    for z in axes[2]:
                        coor = (x, y, z)
                        if coor in cubesOff:
                            continue
                        cubesOn.add(coor)
        elif toggle=="off":
            for x in axes[0]:
                for y in axes[1]:
                    for z in axes[2]:
                        coor = (x, y, z)
                        if coor in cubesOn:
                            continue
                        cubesOff.add(coor)
    return len(cubesOn)

rules = []
for line in open(filename):
    lvec = line.strip().split()
    toggle = lvec[0]
    coors = lvec[1].split(",")
    axes = []
    for axis in coors:
        axis = axis.split("=")[1]
        axis = axis.split("..")
        axis = [int(axis[0]), int(axis[1])]
        axes.append(range(axis[0], axis[1]+1))
    rules.append((toggle, axes))

rules.reverse()

print(setupCubeSets(rules))
