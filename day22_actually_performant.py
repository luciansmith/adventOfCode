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

def calculateOneMinusTwo1d(axis1, axis2):
    retAxes = []
    if axis1[-1] < axis2[0] or axis2[-1] < axis1[0]:
        return ([axis1], "None")
    if axis1[0] < axis2[0] and axis2[0] < axis1[-1]:
        retAxes.append(range(axis1[0], axis2[0]))
        if axis1[-1] < axis2[-1]:
            return (retAxes, "Left")
        else:
            retAxes.append(range(axis2[-1]+1, axis1[-1]+1))
            return (retAxes, "LeftAndRight")
    elif axis2[0] < axis1[-1] and axis1[-1] < axis2[-1]:
        return (range(axis2[-1], axis1[-1]+1), "Right")
    else:
        return ([], "Inside")

print(calculateOneMinusTwo1d(range(0,10), range(15, 20)))
print(calculateOneMinusTwo1d(range(0,10), range(-10, -1)))
print(calculateOneMinusTwo1d(range(0,10), range(5,15)))
print(calculateOneMinusTwo1d(range(0,10), range(5,7)))
print(calculateOneMinusTwo1d(range(0,10), range(-1,15)))
print(calculateOneMinusTwo1d(range(0,10), range(-1,1)))
print(calculateOneMinusTwo1d(range(0,10), range(10,11)))
print(calculateOneMinusTwo1d(range(0,10), range(9,10)))
print(calculateOneMinusTwo1d(range(0,10), range(0,10)))

def calculateOneMinusTwo3d(axes1, axes2):
    pass    

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

# print(setupCubeSets(rules))
