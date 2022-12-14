# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""
import math

def readMonkey(mfile, monkeys):
    lvec = mfile.readline().strip().split()
    lvec[-1] = lvec[-1] + ","
    items = []
    for item in lvec[2:]:
        items.append(int(item[:-1]))
    lvec = mfile.readline().strip().split('=')
    lvec = lvec[1].split()
    operation = lvec
    lvec = mfile.readline().strip().split()
    assert(lvec[-3] == "divisible")
    test = int(lvec[-1])
    lvec = mfile.readline().strip().split()
    iftrue = int(lvec[-1])
    lvec = mfile.readline().strip().split()
    iffalse = int(lvec[-1])
    monkey = [items, operation, test, iftrue, iffalse]
    monkeys.append(monkey)
    mfile.readline()
    return mfile.readline()


monkeyfile = open("day11_input.txt")
#monkeyfile = open("day11_example.txt")

monkeys = []

line = monkeyfile.readline()
while line != "":
    lvec = line.strip().split()
    assert(int(lvec[1][0]) == len(monkeys))
    line = readMonkey(monkeyfile, monkeys)

def calcNewValue(item, operation):
    ret = 0
    old = item
    if operation[0] == "old":
        ret = old
    else:
        raise("Unknown beginning operation in ", operation)
    if operation[2] == "old":
        newval = item
    else:
        newval = int(operation[2])
    if operation[1] == "*":
        return ret * newval
    elif operation[1] == "+":
        return ret + newval
    else:
        raise("Unknown operation", operation)

def add(val1, val2):
    return val1+val2

def multiply(val1, val2):
    return val1*val2

def square(val1, val2):
    return val1*val1

def determineOperations(monkeys):
    for monkey in monkeys:
        operation = monkey[1]
        if operation[2] == "old":
            assert(operation[1] == "*")
            monkey[1] = (square, 1)
        elif operation[1] == "*":
            monkey[1] = (multiply, int(operation[2]))
        elif operation[1] == "+":
            monkey[1] = (add, int(operation[2]))

print(monkeys)
throws = [0] * len(monkeys)

def decideAndThrow(monkeys, mindex, throws):
    (items, operation, test, iftrue, iffalse) = monkeys[mindex]
    item = items[0]
    item = calcNewValue(item, operation)
    item = math.floor(item/3)
    if item % test:
        throwTo = iffalse
    else:
        throwTo = iftrue
    monkeys[throwTo][0].append(item)
    monkeys[mindex][0] = items[1:]
    throws[mindex] += 1
    
# for round in range(20):
#     for mindex in range(len(monkeys)):
#         while len(monkeys[mindex][0]):
#             decideAndThrow(monkeys, mindex, throws)


print(throws)
throws.sort()
print(throws[-1] * throws[-2])

determineOperations(monkeys)
print(monkeys)

allTests = 1
for monkey in monkeys:
    (items, operation, test, iftrue, iffalse) = monkey
    allTests = allTests * test



def decideAndThrowFast(monkeys, mindex, throws, allTests):
    (items, operation, test, iftrue, iffalse) = monkeys[mindex]
    item = items[0]
    item = operation[0](item, operation[1])
    if item > allTests:
        item = item % allTests
    if item % test:
        throwTo = iffalse
    else:
        throwTo = iftrue
    monkeys[throwTo][0].append(item)
    monkeys[mindex][0] = items[1:]
    throws[mindex] += 1
    


for round in range(10000):
    for mindex in range(len(monkeys)):
        while len(monkeys[mindex][0]):
            decideAndThrowFast(monkeys, mindex, throws, allTests)
    if not(round%100):
        print(round, throws)


print(throws)
throws.sort()
print(throws[-1] * throws[-2])



