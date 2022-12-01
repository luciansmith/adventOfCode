import copy
import numpy as np
import time

t0 = time.time()
grid = []
# for line in open("day15_example.txt"):
for line in open("day15_input.txt"):
# for line in open("day15_simple_break.txt"):
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

row = [np.inf]*len(grid[0])*5
risk = []
for n in range(len(grid)*5):
    risk.append(row.copy())

def checkOne(risk, row, col, revisit):
    if row==0 and col==0:
        risk[row][col] = 0
    else:
        orig = risk[row][col]
        neighbors = []
        neighborindices = []
        if row > 0:
            neighbors.append(risk[row-1][col])
            neighborindices.append((row-1, col))
        if col > 0:
            neighbors.append(risk[row][col-1])
            neighborindices.append((row, col-1))
        if row < len(risk)-1:
            neighbors.append(risk[row+1][col])
            neighborindices.append((row+1, col))
        if col < len(risk[0])-1:
            neighbors.append(risk[row][col+1])
            neighborindices.append((row, col+1))

        risk[row][col] = min(neighbors) + lookup(grid, row, col)
        if risk[row][col] < orig:
            revisit.update(neighborindices)
            # if orig != np.inf:
            #     print(neighbors, orig, risk[row][col])
    

def onePass(risk):
    revisit = set()
    for row in range(len(risk)):
        for col in range(len(risk[0])):
            checkOne(risk, row, col, revisit)
    return revisit

risk[0][0] = 0
revisit = onePass(risk)
pnum = 0
while (len(revisit)>0):
    newset = set()
    for (row, col) in revisit:
        checkOne(risk, row, col, newset)
    revisit = newset
    print(revisit)
    pnum += 1
    print(pnum)


# print(risk)
print(risk[-1])

t1 = time.time()
print("elapsed time:", t1-t0)
