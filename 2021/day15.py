import copy
import numpy as np

grid = []
for line in open("day15_input.txt"):
    line = line.strip()
    vec = []
    for digit in line:
        vec.append(int(digit))
    grid.append(vec)

totals = copy.deepcopy(grid)

grid[0][0] = 0
risk = []

for (x, vec) in enumerate(grid):
    riskline = []
    for (y, digit) in enumerate(vec):
        if x==0:
            if y==0:
                riskline.append(0)
            else:
                riskline.append(riskline[y-1] + grid[x][y])
        else:
            if y==0:
                riskline.append(risk[x-1][y] + grid[x][y])
            else:
                riskline.append(min(risk[x-1][y], riskline[y-1]) + grid[x][y])
    risk.append(riskline)
    

print(risk)
            
        
