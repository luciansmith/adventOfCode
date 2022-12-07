# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import numpy as np

def checkHeader(header):
    for (n, ch) in enumerate(header):
        if ch in header[n+1:]:
            return True
    return False

def checkMessage(header):
    for (n, ch) in enumerate(header):
        if ch in header[n+1:]:
            return True
    return False

for line in open("day6_input.txt"):
#for line in open("day6_example.txt"):
    line.strip()
    for (n, ch) in enumerate(line):
        if n<4:
            continue
        if checkHeader(line[n-4:n]):
            continue
        print("End of header:", n, ch)
        if n<14:
            continue
        if checkMessage(line[n-14:n]):
            continue
        print("End of message:", n, ch)
        break