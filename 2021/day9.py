import numpy as np

example = False

filename = "day9_input.txt"
if example:
    filename = "day9_example.txt"

rownum = 0
grid = []
for line in open(filename):
    row = []
    for digit in line.strip():
        row.append(int(digit))
    grid.append(np.array(row, int))
    rownum += 1

grid = np.array(grid)

def getNeighbors(grid, row, col):
    ret = []
    if row > 0:
        ret.append(grid[row-1][col])
    if col > 0:
        ret.append(grid[row][col-1])
    if row < len(grid)-1:
        ret.append(grid[row+1][col])
    if col < len(grid[row])-1:
        ret.append(grid[row][col+1])
    return ret

def getNeighborCoors(grid, row, col):
    ret = set()
    if row > 0:
        ret.add((row-1, col))
    if col > 0:
        ret.add((row, col-1))
    if row < len(grid)-1:
        ret.add((row+1, col))
    if col < len(grid[row])-1:
        ret.add((row, col+1))
    return ret

def isImmediateMin(grid, row, col):
    neighbors = getNeighbors(grid, row, col)
    for neighbor in neighbors:
        if neighbor <= grid[row][col]:
            return False
    return True

def findEntireBasin(grid, row, col):
    basin = set()
    basin.add((row, col))
    neighbors = getNeighborCoors(grid, row, col)
    while len(neighbors)>0:
        newneighbors = set()
        for (r, c) in neighbors:
            if grid[r][c] == 9:
                continue
            if (r, c) in basin:
                continue
            newneighbors.add((r, c))
        neighbors.clear()
        for (r,c) in newneighbors:
            neighbors = neighbors.union(getNeighborCoors(grid, r, c))
        basin = basin.union(newneighbors)
    return basin
    
    

mins = []
mincoors = []
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if isImmediateMin(grid, row, col):
            mins.append(grid[row][col])
            mincoors.append((row, col))

print(mins, sum(mins)+len(mins))

basins = []
basinlens = []
for (row, col) in mincoors:
    basin = findEntireBasin(grid, row, col)
    basins.append(basin)
    basinlens.append(len(basin))

# print(basins)
basinlens.sort()
print(basinlens, basinlens[-1]*basinlens[-2]*basinlens[-3])
