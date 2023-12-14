# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

data = open("day6.txt");
# data = open("day6_ex.txt")

times = data.readline()
distances = data.readline()

times = times.strip().split()[1:]
for n in range(len(times)):
    times[n] = int(times[n])
distances = distances.strip().split()[1:]
for n in range(len(distances)):
    distances[n] = int(distances[n])
print(times)
print(distances)

mult_total = 1
for n in range(len(times)):
    time = times[n]
    record = distances[n]
    winners = 0
    for speed in range(time):
        distance = speed * (time-speed)
        if distance > record:
            winners += 1
    mult_total = mult_total * winners
    print(winners)

print("Multiplicative total:", mult_total)

newtime = ""
for time in times:
    newtime += str(time)
newtime = int(newtime)

newdist = ""
for dist in distances:
    newdist += str(dist)
newdist = int(newdist)

print(newtime, newdist)

winners = 0
for speed in range(newtime):
    distance = speed * (newtime-speed)
    if distance > newdist:
        winners += 1
    # print(winners)
print(winners)
