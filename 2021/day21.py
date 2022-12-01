import numpy as np
import sys

example = False

p1pos = 4
p2pos = 6

if example:
    p1pos = 4
    p2pos = 8
    
p1score = 0
p2score = 0

die = 0
dierolls = 0

def rollAndAdd(score, pos, die, dierolls):
    pos += die*3+6
    die = die+3
    dierolls += 3
    while (die>100):
        die -= 100
    while pos > 10:
        pos -= 10
    score += pos
    return (score, pos, die, dierolls)
    

while(True):
    (p1score, p1pos, die, dierolls) = rollAndAdd(p1score, p1pos, die, dierolls)
    if p1score >= 1000:
        print("p1:", p1pos, p1score)
        print("p2:", p2pos, p2score)
        print("dierolls * p2score", dierolls*p2score)
        sys.exit(0)
    (p2score, p2pos, die, dierolls) = rollAndAdd(p2score, p2pos, die, dierolls)
    if p2score >= 1000:
        print("p1:", p1pos, p1score)
        print("p2:", p2pos, p2score)
        print("dierolls * p1score", dierolls*p1score)
        sys.exit(0)
