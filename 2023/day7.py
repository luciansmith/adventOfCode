# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

part = 2
data = open("day7.txt");
# data = open("day7_ex.txt")

types = {"five": 7,
         "four": 6,
         "full": 5,
         "three": 4,
         "2p": 3,
         "pair": 2,
         "high": 1,
         }

def getType(hand):
    handmap = {}
    for ch in hand:
        if ch in handmap:
            handmap[ch] += 1
        else:
            handmap[ch] = 1
    if len(handmap) == 1:
        return "five"
    haswild = False
    if 1 in handmap:
        haswild = True
    if len(handmap) == 2:
        if haswild:
            return "five"
        for ch in handmap:
            if handmap[ch] == 4:
                return "four"
        return "full"
    if len(handmap) == 3:
        for ch in handmap:
            if handmap[ch] == 3:
                if haswild:
                    return "four"
                return "three"
        if haswild:
            if handmap[1] == 2:
                return "four"
            return "full"
        return "2p"
    if len(handmap) == 4:
        if haswild:
            return "three"
        return "pair"
    assert(len(handmap) == 5)
    if haswild:
        return "pair"
    return "high"

def getScore(hand, htype):
    return htype*1e10 + hand[0]*1e8 + hand[1]*1e6 + hand[2]*1e4 + hand[3]*1e2 + hand[4]

total = 0
hands = []
for line in data:
    (hand, bid) = line.strip().split()
    bid = int(bid)
    ch_hand = []
    for ch in hand:
        if ch.isdigit():
            ch_hand.append(int(ch))
        elif ch == 'T':
            ch_hand.append(10)
        elif ch=='J':
            if part==1:
                ch_hand.append(11)
            if part==2:
                ch_hand.append(1)
        elif ch=='Q':
            ch_hand.append(12)
        elif ch=='K':
            ch_hand.append(13)
        elif ch=='A':
            ch_hand.append(14)
    htype = getType(ch_hand)
    score = getScore(ch_hand, types[htype])
    print(hand, htype)
    hands.append((score, ch_hand, bid, types[htype]))

hands.sort()
total = 0
for h in range(len(hands)):
    total += (h+1) * hands[h][2]
    print(total)

print(hands)
print(total)