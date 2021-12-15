import copy
import numpy as np

grid = []
#for line in open("day15_example.txt"):
for line in open("day15_input.txt"):
#for line in open("day15_simple_break.txt"):
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

def onePass(risk):
    redo = False
    for row in range(len(risk)):
        for col in range(len(risk[0])):
            if row==0 and col==0:
                risk[row][col] = 0
            else:
                orig = risk[row][col]
                neighbors = []
                if row > 0:
                    neighbors.append(risk[row-1][col])
                if col > 0:
                    neighbors.append(risk[row][col-1])
                if row < len(risk)-1:
                    neighbors.append(risk[row+1][col])
                if col < len(risk[0])-1:
                    neighbors.append(risk[row][col+1])

                risk[row][col] = min(neighbors) + lookup(grid, row, col)
                if risk[row][col] < orig:
                    redo = True
                    # if orig != np.inf:
                    #     print(neighbors, orig, risk[row][col])
    return redo

redo = onePass(risk)
pnum = 0
while (redo):
    redo = onePass(risk)
    pnum += 1
    print(pnum)


print(risk[-1])
