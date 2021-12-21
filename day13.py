import numpy as np

example = False

filename = "day13_input.txt"

if example:
    filename = "day13_example.txt"

coordinates = []
folds = []
rows = 0
cols = 0
for line in open(filename):
    line = line.strip()
    if "," in line:
        coor = line.split(",")
        coor = int(coor[0]), int(coor[1])
        coordinates.append(coor)
        cols = max(cols, coor[0])
        rows = max(rows, coor[1])
    elif "fold" in line:
        fold = line.split()[2]
        fold = fold.split("=")
        folds.append(fold)

grid = np.zeros([rows+1, cols+1])

for coor in coordinates:
    grid[coor[1]][coor[0]] = 1

def applyFold(grid, axis, val):
    if axis=="x":
        #Columns
        newgrid = grid[:,:val]
        foldgrid = np.flip(grid[:,val+1:],1)
        diff = len(newgrid[0]) > len(foldgrid[0])
        add = np.zeros([len(newgrid), abs(diff)])
        if diff > 0:
            foldgrid = np.hstack((add, foldgrid))
        elif diff < 0:
            newgrid = np.hstack((add, newgrid))
        newgrid = newgrid + foldgrid
        # for row in range(len(foldgrid)):
        #     for col in range(len(foldgrid[0])):
        #         newgrid[row][val-col] = max(foldgrid[row][col], newgrid[row][val-col])
        return newgrid
    if axis=="y":
        newgrid = grid[:val,:]
        foldgrid = np.flip(grid[val+1:,:],0)
        diff = len(newgrid) - len(foldgrid)
        add = np.zeros([abs(diff), len(newgrid[0])])
        if diff > 0:
            foldgrid = np.vstack((add, foldgrid))
        elif diff < 0:
            newgrid = np.vstack((add, newgrid))
        newgrid = newgrid + foldgrid
        # for row in range(len(foldgrid)):
        #     for col in range(len(foldgrid[0])):
        #         newgrid[val-row][col] = max(foldgrid[row][col], newgrid[val-row][col])
        return newgrid
    raise ValueError("Unknown fold axis.")

print(grid)
for fold in folds:
    grid = applyFold(grid, fold[0], int(fold[1]))
    grid = np.where(grid > 0, 1, 0)
    print(grid)
    print(sum(sum(grid)))

paper = ""
for row in grid:
    for col in row:
        if col:
            paper = paper + "#"
        else:
            paper = paper + "."
    paper = paper + "\n"

print(paper)
