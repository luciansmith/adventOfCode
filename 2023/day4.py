# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

data = open("day4.txt");
# data = open("day4_ex.txt")


tot_orig = 0
tot_cards = 0
nexts = [0]*11
for line in data:
    copies = nexts[0] + 1
    tot_cards += copies
    nexts = nexts[1:]
    nexts.append(0)
    line = line.strip()
    (winning, have) = line.split('|')
    (card, winning) = winning.split(':')
    winning = winning.split(' ')
    have = have.split(' ')
    matches = 0
    for num in have:
        if num != "" and num in winning:
            matches += 1
    if matches>0:
        print(card, matches)
        tot_orig += 2**(matches-1)
    for n in range(matches):
        nexts[n] += copies
    
    
print("Total score:", tot_orig)
print("Total cards:", tot_cards)
