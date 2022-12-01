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

def check50(rules, default):
    ret = 0
    for x in range(-50, 51):
        for y in range(-50, 51):
            for z in range(-50, 51):
                if checkCoor((x, y, z), rules, default) == "on":
                    ret += 1
    return ret

def checkAll(rules, default, Xrange, Yrange, Zrange):
    ret = 0
    for x in Xrange:
        print(x)
        for y in Yrange:
            for z in Zrange:
                if checkCoor((x, y, z), rules, default) == "on":
                    ret += 1
    return ret


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

minX = 0
maxX = 0
minY = 0
maxY = 0
minZ = 0
maxZ = 0
for (toggle, axes) in rules:
    minX = min(minX, axes[0][0])
    maxX = max(maxX, axes[0][-1])
    minY = min(minY, axes[0][0])
    maxY = max(maxY, axes[0][-1])
    minZ = min(minZ, axes[0][0])
    maxZ = max(maxZ, axes[0][-1])

#part 1.  Takes forever
#print(check50(rules, "off"))

#part 2.  Takes forever
print(checkAll(rules, "off", range(minX, maxX), range(minY, maxY), range(minZ, maxZ)))
