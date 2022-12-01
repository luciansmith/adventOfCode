import numpy as np
import sys
import time

start = time.time()

example = False

p1pos = 4
p2pos = 6

if example:
    p1pos = 4
    p2pos = 8
    
scorepos1 = {}
scorepos2 = {}
scorepos1[(0, p1pos)] = 1
scorepos2[(0, p2pos)] = 1

def rollAndAdd(roll, scorepos, freq):
    new_scorepos = {}
    
    for (score, pos) in scorepos:
        current = scorepos[(score, pos)]
        pos += roll
        if pos>10:
            pos -= 10
        score += pos
        new_scorepos[(score, pos)] = current*freq
    return new_scorepos

def combineScorePos(all_scorepositions):
    new_scorepos = {}
    for scorepos in all_scorepositions:
        for sp in scorepos:
            if sp not in new_scorepos:
                new_scorepos[sp] = scorepos[sp]
            else:
                new_scorepos[sp] += scorepos[sp]
    return new_scorepos

def reapWinners(scorepos):
    winners = []
    wins = 0
    for (score, pos) in scorepos:
        if score > 20:
            winners.append((score, pos))
    for sp in winners:
        wins += scorepos[sp]
        scorepos.pop(sp)
    return wins

def getNumActiveUniverses(scorepos):
    ret = 0
    for sp in scorepos:
        ret += scorepos[sp]
    return ret

def multiplyUniverses(scorepos, newUniverseNumber, prevUniverseNumber):
    # print(newUniverseNumber/prevUniverseNumber)
    for sp in scorepos:
        scorepos[sp] = scorepos[sp]*newUniverseNumber/prevUniverseNumber

p1wins = 0
p2wins = 0
rollfreqs = [(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]

for p1start in range(1,11):
    for p2start in range(1,11):
        scorepos1 = {}
        scorepos1[(0, p1start)] = 1
        scorepos2 = {}
        scorepos2[(0, p2start)] = 1
        print("\nStarting from", p1start, p2start)
        while(True):
            new_sp1 = []
            for (roll, freq) in rollfreqs:
                new_sp1.append(rollAndAdd(roll, scorepos1, freq))
            scorepos1 = combineScorePos(new_sp1)
            p1wins += reapWinners(scorepos1)
            if (len(scorepos1)==0):
                print(p1wins, p2wins)
                break
            
            # print("p1, p2 states", len(scorepos1), len(scorepos2), len(scorepos1)*len(scorepos2))
            #boucher said the largest state set he had was 11544.  Let's figure out which one it was:
            if (len(scorepos1)*len(scorepos2) == 11544):
                print("p1, p2 states", len(scorepos1), len(scorepos2), len(scorepos1)*len(scorepos2))
            n1Universes = getNumActiveUniverses(scorepos1)
            n2Universes = getNumActiveUniverses(scorepos2)
            multiplyUniverses(scorepos2, n1Universes, n2Universes)
            
        
            new_sp2 = []
            for (roll, freq) in rollfreqs:
                new_sp2.append(rollAndAdd(roll, scorepos2, freq))
            scorepos2 = combineScorePos(new_sp2)
            newwins = reapWinners(scorepos2)
            p2wins += newwins
            if (len(scorepos2)==0):
                print(p1wins, p2wins)
                break
        
            # print("p1, p2 states", len(scorepos1), len(scorepos2), len(scorepos1)*len(scorepos2))
            if (len(scorepos1)*len(scorepos2) == 11544):
                print("p1, p2 states", len(scorepos1), len(scorepos2), len(scorepos1)*len(scorepos2))
            n1Universes = getNumActiveUniverses(scorepos1)
            n2Universes = getNumActiveUniverses(scorepos2)
            multiplyUniverses(scorepos1, n2Universes, n1Universes)

end = time.time()
print("Elapsed time:", end - start)
