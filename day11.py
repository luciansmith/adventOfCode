import numpy as np

example = False
part1 = False

filename = "day11_input.txt"
if example:
    filename = "day11_example.txt"

grid = np.zeros([10,10], int)
rownum = 0
for line in open(filename):
    row = []
    for digit in line.strip():
        row.append(int(digit))
    grid[rownum] = np.array(row, int)
    rownum += 1

# print(grid)

def flash(grid, row, col):
    lrow = max(0, row-1)
    rrow = min(9, row+1)
    ucol = max(0, col-1)
    dcol = min(9, col+1)
    # print(row, col)
    # print(grid)
    for row in range(lrow, rrow+1):
        for col in range(ucol, dcol+1):
            grid[row][col] += 1
    # print(grid)

def step(grid):
    grid += 1
    oldflashes = set()
    newsearch = True
    while newsearch:
        newsearch = False
        newflashes = set()
        for row in range(10):
            for col in range(10):
                if grid[row][col] > 9:
                    index = (row, col)
                    if index not in oldflashes:
                        newflashes.add(index)
        if len(newflashes) > 0:
            newsearch = True
        for (row, col) in newflashes:
            flash(grid, row, col)
        oldflashes = oldflashes.union(newflashes)
    for row in range(10):
        for col in range(10):
            if grid[row][col] > 9:
                grid[row][col] = 0
    return len(oldflashes)

if part1:
    flashcount = 0
    for n in range(100):
        flashcount += step(grid)
    print(grid)
    print(flashcount)

else:
    n = 1
    while step(grid)<100:
        n += 1
    print(n)
