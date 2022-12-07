# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import numpy as np

def readLS(file, current_dir):
    line = file.readline()
    if line=="":
        return ""
    if line[0] == "$":
        return line
    lvec = line.strip().split()
    if lvec[0] == "dir":
        current_dir[lvec[1]] = {}
    else:
        current_dir[lvec[1]] = int(lvec[0])
    return readLS(file, current_dir)

def readCommandsThisDir(line, file, current_dir, updir):
    while (line != ""):
        lvec = line.strip().split()
        assert(lvec[0] == "$")
        if lvec[1] == "cd":
            if lvec[2] == "..":
                return file.readline()
            elif lvec[2] == "/":
                line = file.readline()
            else:
                subdir = current_dir[lvec[2]]
                line = file.readline()
                line = readCommandsThisDir(line, file, subdir, current_dir)
        elif lvec[1] == "ls":
            line = readLS(file, current_dir)
    return ""


rootdir = {}

file = open("day7_input.txt")
#file = open("day7_example.txt", "r")

line = file.readline()
while (line != ""):
    line = readCommandsThisDir(line, file, rootdir, None)
print(rootdir)

#Now that it's parsed, look at the sizes:

def get10kDirsFrom(direc, dirs):
    total = 0
    for key in direc:
        if isinstance(direc[key], int):
            total += direc[key]
        else:
            total += get10kDirsFrom(direc[key], dirs)
    if total < 100000:
        dirs.append(total)
    return total

def getAllDirSizes(direc, dirs, id, path):
    total = 0
    for key in direc:
        if isinstance(direc[key], int):
            total += direc[key]
        else:
            total += getAllDirSizes(direc[key], dirs, key, path + "/" + id)
    dirs[path + "/" + id] = total
    return total

tenKdirs = []
print(get10kDirsFrom(rootdir,tenKdirs))
print(tenKdirs)
print(sum(tenKdirs))

dirSizes = {}
root = getAllDirSizes(rootdir, dirSizes, "", "")
total = 70000000 - root
need = 30000000 - total

print(dirSizes)

smallest = "/"
smallestdiff = need - root
for direc in dirSizes:
    diff = need - dirSizes[direc]
    if diff < 0:
        print(direc, diff)
    if diff < 0 and diff > smallestdiff:
        smallest = direc
        smallestdiff = diff

print(smallest, smallestdiff, dirSizes[smallest])
















