example = False

input = {
    "xmin": 70,
    "xmax": 125,
    "ymin": -159,
    "ymax": -121,
    }
if example:
    input = {
        "xmin": 20,
        "xmax": 30,
        "ymin": -10,
        "ymax": -5,
        }

def getValidXs(xmin, xmax):
    validxs = []
    for x in range(xmax+1):
        dist = x
        drag = x
        steps = 1
        while dist < xmax+1 and drag > -1:
            if dist in range(xmin, xmax+1):
                validxs.append((x, steps))
            drag -= 1
            dist += drag
            steps += 1
    return validxs

def getValidYs(ymin, ymax):
    validys = []
    for y in range(ymin, -ymin):
        dist = y
        drag = y
        steps = 1
        maxheight = 0
        while dist >= ymin:
            if dist in range(ymin, ymax+1):
                validys.append((y, steps, maxheight))
            drag -= 1
            dist += drag
            steps += 1
            maxheight = max(maxheight, dist)
    return validys

def getValidCombos(validxs, validys):
    validcombos = set()
    for (y, ysteps, maxheight) in validys:
        for (x, xsteps) in validxs:
            if ysteps == xsteps:
                validcombos.add((x, y, maxheight))
            elif xsteps==x and ysteps > xsteps:
                validcombos.add((x, y, maxheight))
    return validcombos

def findBest(validcombos):
    best = (-1, -1, -1)
    for (x, y, maxheight) in validcombos:
        if maxheight > best[2]:
            best = (x, y, maxheight)
    return best

validxs = getValidXs(input["xmin"], input["xmax"])
print(validxs)
validys = getValidYs(input["ymin"], input["ymax"])
print(validys)
validcombos = getValidCombos(validxs, validys)
print(validcombos)
print(findBest(validcombos))
print(len(validcombos))
# valid_trajectories = getValidTrajectories(validxs, input["ymin"], input["ymax"])

# print(valid_trajectories)
                                                                       
