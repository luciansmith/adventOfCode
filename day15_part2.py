import copy
import numpy as np

grid = []
#for line in open("day15_example.txt"):
for line in open("day15_input.txt"):
    line = line.strip()
    vec = []
    for digit in line:
        vec.append(int(digit))
    grid.append(vec)
    
def lookup(grid, row, col):
    if row<len(grid):
        if col<len(grid[0]):
            return grid[row][col]
        else:
            val = 1 + lookup(grid, row, col-len(grid[0]))
    else:
        val = 1 + lookup(grid, row-len(grid), col)
    while val>9:
        val = val-9
    return val

prevrisk = []

for row in [0]:#range(len(grid)*5):
    riskline = []
    for col in range(len(grid[0])*5):
        if row==0:
            if col==0:
                riskline.append(0)
            else:
                riskline.append(riskline[col-1] + lookup(grid, row, col))
        else:
            if col==0:
                riskline.append(prevrisk[col] + lookup(grid, row, col))
            else:
                riskline.append(min(prevrisk[col], riskline[col-1]) + lookup(grid, row, col))
    prevrisk = copy.deepcopy(riskline)
    print(riskline)
            
        
lookup(grid, 48, 0)
