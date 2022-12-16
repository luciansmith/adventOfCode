# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import time
begin = time.perf_counter()

import re

#Sensor at x=2, y=18: closest beacon is at x=-2, y=15

sensors = {}
beacons = []

for  line in open("day15_input.txt"):
#for line in open("day15_example.txt"):
    lvec = re.split('=|,|:',line.strip())
    sensor = (int(lvec[1]), int(lvec[3]))
    beacon = (int(lvec[5]), int(lvec[7]))
    dist = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
    print(sensor, beacon, dist)
    sensors[sensor] = dist
    beacons.append(beacon)

xmin = sensor[0] - dist
xmax = sensor[0] + dist

for sensor in sensors:
    xmin1 = sensor[0] - sensors[sensor]
    xmax1 = sensor[0] + sensors[sensor]
    if xmin1 < xmin:
        xmin = xmin1
    if xmax1 > xmax:        
        xmax = xmax1

print(xmin, xmax)
yrow = 2000000

#Very slow, but working, part 1:
# count = 0
# for x in range(xmin, xmax+1):
#     covered = False
#     for sensor in sensors:
#         dist = sensors[sensor]
#         if dist >= abs(sensor[0]-x) + abs(sensor[1]-yrow):
#             covered = True
#             break
#     if covered:
#         if (x, yrow) not in beacons:
#             count += 1

maxval = 4000000
#maxval = 20

import sys

#Very slow, but working, part 2:
count = 0
for y in range(maxval+1):
    print(y)
    for x in range(maxval+1):
        covered = False
        for sensor in sensors:
            dist = sensors[sensor]
            if dist >= abs(sensor[0]-x) + abs(sensor[1]-y):
                covered = True
                break
        if not covered:
            print(x, y, x*4000000 + y)
            sys.exit(0)

