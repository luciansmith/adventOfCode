# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

data = open("day2.txt");
# data = open("day2ex.txt")

maxes= {
        "red": 12,
        "green": 13,
        "blue": 14,}

total = 0
totpower = 0
gamenum = 0
for line in data:
    gamenum += 1
    print("game", gamenum)
    line = line.strip()
    (num, data) = line.split(':')
    hands = data.split(';')
    gamemaxes = {}
    for hand in hands:
        counts = hand.split(',')
        for count in counts:
            count = count.strip()
            (num, color) = count.split(' ')
            num = int(num)
            # print(num, color)
            if color in gamemaxes:
                if gamemaxes[color] < num:
                    gamemaxes[color] = num
            else:
                gamemaxes[color] = num
    possible = True
    power = 1
    for color in maxes:
        if color in gamemaxes:
            if gamemaxes[color] > maxes[color]:
                # print("Game", gamenum, "impossible.")
                possible = False
                break
    for color in gamemaxes:
        power = power * gamemaxes[color]
    if possible:
        total += gamenum
    totpower += power
    print("power:", power)
                
            
    
print("Total:", total)
print("Power:", totpower)