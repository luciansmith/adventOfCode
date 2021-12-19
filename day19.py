import numpy as np
import itertools

example = False

filename = "day19_input.txt"
if example:
    filename = "day19_example.txt"


class Scanner:
    def __init__(self):
        self.beacons = []
        self.distances = []
        self.distanceSet = set()
        self.absorbedScanners = [(0,0,0),]

    def addBeacon(self, x, y, z):
        for (n, beacon) in enumerate(self.beacons):
            self.distances[n].append(round(np.sqrt((beacon[0]-x)**2 + (beacon[1]-y)**2 + (beacon[2]-z)**2), 10))
            self.distanceSet.add(self.distances[n][-1])
        self.beacons.append((x, y, z))
        self.distances.append([])
        
    def getPairWithDist(self, distance):
        ret = []
        for n1 in range(len(self.distances)):
            for n2 in range(len(self.distances[n1])):
                if self.distances[n1][n2] == distance:
                    ret.append(n1)
                    ret.append(n2+n1+1)
        if len(ret)<2:
            raise ValueError("Unable to find distance", distance)
        return ret
    
    def getSecondPairWithDist(self, distance):
        first = True
        for n1 in range(len(self.distances)):
            for n2 in range(len(self.distances[n1])):
                if self.distances[n1][n2] == distance:
                    if first:
                        first = False
                    else:
                        return (n1, n2+n1+1)
        raise ValueError("Unable to find distance", distance)
    
    def getBeacon(self, n):
        return self.beacons[n]
    
    def getLargestManhattanDist(self):
        maxdist = 0
        for n1 in range(len(self.absorbedScanners)-1):
            for n2 in range(n1+1, len(self.absorbedScanners)):
                dist = abs(self.absorbedScanners[n1][0] - self.absorbedScanners[n2][0]) + \
                       abs(self.absorbedScanners[n1][1] - self.absorbedScanners[n2][1]) + \
                       abs(self.absorbedScanners[n1][2] - self.absorbedScanners[n2][2])
                # print(n1, n2, dist)
                if dist>maxdist:
                    maxdist = dist
        return maxdist
    
    def combineWith(self, scanner2, commonDistances):
        commonDistances = list(commonDistances)
        ret = Scanner()
        ret.beacons = self.beacons
        ret.distances = self.distances
        ret.distanceSet = self.distanceSet
        (b1, b2) = self.getPairWithDist(commonDistances[0]) #might need to 
            
        oneSelfPairSet = [(b1, b2),]
        oneOtherPairSet = [scanner2.getPairWithDist(commonDistances[0])]
        otherB1 = -1
        for n, distance in enumerate(commonDistances):
            if n==0:
                continue
            beacons = self.getPairWithDist(distance)
            if b1 in beacons:
                if b1 in beacons[0:2]:
                    oneSelfPairSet.append((beacons[0], beacons[1]))
                elif b1 in beacons[2:]:
                    oneSelfPairSet.append((beacons[2], beacons[3]))
                else:
                    raise ValueError("Need to implement triple distance matches.")
                otherBeacons = scanner2.getPairWithDist(distance)
                if otherB1 == -1:
                    if oneOtherPairSet[0][0] == otherBeacons[0]:
                        otherB1 = oneOtherPairSet[0][0]
                    elif oneOtherPairSet[0][0] == otherBeacons[1]:
                        otherB1 = oneOtherPairSet[0][0]
                    elif oneOtherPairSet[0][1] == otherBeacons[0]:
                        otherB1 = oneOtherPairSet[0][1]
                    elif oneOtherPairSet[0][1] == otherBeacons[1]:
                        otherB1 = oneOtherPairSet[0][1]
                    else:
                        raise ValueError("Unable to find matching pair in other set.")
                if otherB1 in otherBeacons[0:2]:
                    oneOtherPairSet.append(otherBeacons[0:2])
                elif otherB1 in otherBeacons[2:4]:
                    oneOtherPairSet.append(otherBeacons[0:2])
                elif len(otherBeacons)<5:
                    oneSelfPairSet.pop() #Doesn't actually have a match.
                else:
                    raise ValueError("Need to implement triple distance matches.")

        selfBeacons = []
        otherBeacons = []
        selfBeacons.append(self.getBeacon(oneSelfPairSet[0][0]))
        otherBeacons.append(scanner2.getBeacon(otherB1))
        for n in range(len(oneSelfPairSet)):
            if b1 == oneSelfPairSet[n][0]:
                selfBeacons.append(self.getBeacon(oneSelfPairSet[n][1]))
            elif b1 == oneSelfPairSet[n][1]:
                selfBeacons.append(self.getBeacon(oneSelfPairSet[n][0]))
            if otherB1 == oneOtherPairSet[n][0]:
                otherBeacons.append(scanner2.getBeacon(oneOtherPairSet[n][1]))
            elif otherB1 == oneOtherPairSet[n][1]:
                otherBeacons.append(scanner2.getBeacon(oneOtherPairSet[n][0]))
            else:
                #The distance was repeated--get the other one.
                (c1, c2) = scanner2.getSecondPairWithDist(commonDistances[n])
                if otherB1 == c1:
                    otherBeacons.append(scanner2.getBeacon(c2))
                elif otherB1 == c2:
                    otherBeacons.append(scanner2.getBeacon(c1))
                else:
                    raise ValueError("Even the second distance gave us the wrong pair.")
        if example:
            for n in range(len(selfBeacons)):
                print(selfBeacons[n], ",", otherBeacons[n])
        pairdist = [selfBeacons[0][0] - selfBeacons[1][0],
                    selfBeacons[0][1] - selfBeacons[1][1],
                    selfBeacons[0][2] - selfBeacons[1][2]]
        if abs(pairdist[0]) == abs(pairdist[1]) or (abs(pairdist[0]) == abs(pairdist[2])) or abs(pairdist[1]) == abs(pairdist[2]):
            raise ValueError("Must implement picking a different pair of coordinates.")
        other_pairdist = [otherBeacons[0][0] - otherBeacons[1][0],
                          otherBeacons[0][1] - otherBeacons[1][1],
                          otherBeacons[0][2] - otherBeacons[1][2]]
        
        gridMap = {}
        for axis in [0, 1, 2]:
            for otheraxis in [0, 1, 2]:
                if pairdist[axis] == other_pairdist[otheraxis]:
                    gridMap[axis] = (otheraxis, 1, -selfBeacons[0][axis] + otherBeacons[0][otheraxis])
                elif pairdist[axis] == -other_pairdist[otheraxis]:
                    gridMap[axis] = (otheraxis, -1, -selfBeacons[0][axis] - otherBeacons[0][otheraxis])
        print(gridMap)

        #Now actually combine them
        #Transform the other pair set into a bunch of indexes for beacons we already have:
        otherBeaconsAlreadyHere = set()
        for (c1, c2) in oneOtherPairSet:
            otherBeaconsAlreadyHere.add(c1)
            otherBeaconsAlreadyHere.add(c2)
        
        (otherx, xdirection, xoffset) = gridMap[0]
        (othery, ydirection, yoffset) = gridMap[1]
        (otherz, zdirection, zoffset) = gridMap[2]
        for n, otherbeacon in enumerate(scanner2.beacons):
            newx = xdirection * otherbeacon[otherx] - xoffset
            newy = ydirection * otherbeacon[othery] - yoffset
            newz = zdirection * otherbeacon[otherz] - zoffset
            if n in otherBeaconsAlreadyHere:
                print("Already have", newx, newy, newz)
                assert self.beacons.index((newx, newy, newz)) >= 0
                continue
            ret.addBeacon(newx, newy, newz)
        ret.absorbedScanners = self.absorbedScanners
        for otherScanner in scanner2.absorbedScanners:
                    
            ret.absorbedScanners.append((otherScanner[0]-xoffset, otherScanner[1]-yoffset, otherScanner[2]-zoffset))
        
        return ret
        
def findTwoScannersToCombine(scanners):
    best = [0, -1, -1, None]
    for n1 in range(len(scanners)-1):
        for n2 in range(n1+1, len(scanners)):
            distoverlap = scanners[n1].distanceSet.intersection(scanners[n2].distanceSet)
            print(n1, n2, len(distoverlap))
            if len(distoverlap) >= 66:
                return (n1, n2, distoverlap)
            elif len(distoverlap) > best[0]:
                best[0] = len(distoverlap)
                best[1] = n1
                best[2] = n2
                best[3] = distoverlap
    #There are examples with <12 overlapped scanners.
    return (best[1], best[2], best[3])
    # raise ValueError("Couldn't find two combinable scanners.")
        
        

scanners = []
scanner = Scanner()
distances = []
for line in open(filename):
    if len(line.strip()) == 0:
        scanners.append(scanner)
        print()
        scanner = Scanner()
    elif "---" in line:
        assert(len(scanners) == int(line.split()[2]))
    else:
        [x, y, z] = line.strip().split(",")
        x = int(x)
        y = int(y)
        z = int(z)
        scanner.addBeacon(x, y, z)
if (len(scanner.beacons) > 0):
    scanners.append(scanner)

while len(scanners) > 1:
    (n1, n2, distoverlap) = findTwoScannersToCombine(scanners)
    print("Combining scanners", n1, "and", n2)
    newscanners = []
    newscanners.append(scanners[n1].combineWith(scanners[n2], distoverlap))
    for n in range(len(scanners)):
        if n == n1 or n == n2:
            continue
        newscanners.append(scanners[n])
    scanners = newscanners

print(len(scanners[0].beacons), "total beacons")
print(scanners[0].getLargestManhattanDist(), "largest Manhattan distance")


