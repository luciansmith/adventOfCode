import numpy as np

example = False
part2 = True

filename = "day5_input.txt"
if (example):
    filename = "day5_example.txt"

vents = []
maxx = 0
maxy = 0
for line in open(filename):
    (start, end) = line.strip().split(" -> ")
    (x1, y1) = start.split(",")
    (x2, y2) = end.split(",")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    vents.append(((x1, y1), (x2, y2)))
    maxx = max(maxx, x1)
    maxx = max(maxx, x2)
    maxy = max(maxy, y1)
    maxy = max(maxy, y2)

seafloor = np.zeros([maxy+1, maxx+1])

# print(seafloor)

def drawvents(seafloor, vents):
    for (x1, y1), (x2, y2) in vents:
        if x1==x2:
            ymin = min(y1, y2)
            ymax = max(y1, y2)
            for y in range(ymin, ymax+1):
                seafloor[y][x1] += 1
        elif y1==y2:
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            for x in range(xmin, xmax+1):
                seafloor[y1][x] += 1
        elif part2:
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            ymin = min(y1, y2)
            ymax = max(y1, y2)
            assert(xmax-xmin == ymax-ymin)
            if (x1==xmin and y1==ymin) or (x2==xmin and y2==ymin):
                for inc in range(xmax-xmin+1):
                    seafloor[ymin+inc][xmin+inc] += 1
            else:
                for inc in range(xmax-xmin+1):
                    seafloor[ymax-inc][xmin+inc] += 1
                

drawvents(seafloor, vents)
print(seafloor)

unique, counts = np.unique(seafloor, return_counts=True)
allcounts = dict(zip(unique, counts))
print(allcounts[2.0])
tot = 0
for index in unique:
    if index <2:
        continue
    tot += allcounts[index]

print(tot)
