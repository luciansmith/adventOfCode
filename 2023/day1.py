# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:42:07 2023

@author: Lucian
"""

data = open("day1.txt");
# data = open("day1ex.txt")
total = 0

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getFirst(line):
    for n in range(0,len(line)):
        subline = line[0:n]
        for (z, name) in enumerate(digits):
            newline = subline.replace(name, str(z))
            if newline != subline:
                return z
        ch = line[n]
        if ch <= '9' and ch >= '0':
            return ord(ch) - ord('0')
    raise Exception("No number found.")

def getLast(line):
    for n in range(len(line), 0, -1):
        subline = line[n:]
        for (z, name) in enumerate(digits):
            newline = subline.replace(name, str(z))
            if newline != subline:
                return z
        ch = line[n-1]
        if ch <= '9' and ch >= '0':
            return ord(ch) - ord('0')
    raise Exception("No number found.")
    


for line in data:
    first = -1;
    last = -1;
    print(line)
    first = getFirst(line)
    last = getLast(line)
    print(first, last)
    total = total+first*10+last
    
print(total)