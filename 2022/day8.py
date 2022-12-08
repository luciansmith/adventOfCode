# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:54:30 2022

@author: Lucian
"""

import numpy as np

def countVisible(grid):
    visible = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row==0 or row==len(grid)-1 or col==0 or col==len(grid[row])-1:
                visible += 1
            else:
                val = grid[row][col]
                left_lower = True
                right_lower = True
                up_lower = True
                down_lower = True
                for row2 in range(len(grid)):
                    if row2 < row:
                        if grid[row2][col] >= val:
                            left_lower = False
                    elif row2 > row:
                        if grid[row2][col] >= val:
                            right_lower = False
                for col2 in range(len(grid)):
                    if col2 < col:
                        if grid[row][col2] >= val:
                            up_lower = False
                    elif col2 > col:
                        if grid[row][col2] >= val:
                            down_lower = False
                if left_lower or right_lower or up_lower or down_lower:
                    visible += 1
    return visible

def calcVisibility(grid, row, col):
    left = 0
    right = 0
    up = 0
    down = 0
    val = grid[row][col]
    for r in range(row-1, -1, -1):
        left += 1
        if grid[r][col] >= val:
            break

    for r in range(row+1, len(grid)):
        right += 1
        if grid[r][col] >= val:
            break

    for c in range(col-1, -1, -1):
        up += 1
        if grid[row][c] >= val:
            break

    for c in range(col+1, len(grid)):
        down += 1
        if grid[row][c] >= val:
            break
    print(left, right, up, down)
    return left*right*up*down
    

def calcAllVisibilities(grid):
    bestVisibility = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row==0 or row==len(grid)-1 or col==0 or col==len(grid[row])-1:
                continue
            new = calcVisibility(grid, row, col)
            print(new, row, col)
            if new>bestVisibility:
                bestVisibility = new
    return bestVisibility

grid = []
for line in open("day8_input.txt"):
#for line in open("day8_example.txt"):
    line = line.strip()
    row = []
    for ch in line:
        row.append(int(ch))
    grid.append(row)

                    

print("Visible trees:", countVisible(grid))
print("Best visibility:", calcAllVisibilities(grid))