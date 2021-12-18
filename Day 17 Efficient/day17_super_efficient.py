import numpy as np
import sys

example = False

xmin = 70
xmax = 125
ymin = -159
ymax = -121

if example:
    xmin = 20
    xmax = 30
    ymin = -10
    ymax = -5

#We're optimizing for part 1 here; might add part 2 later.

#These are global values that will alternately decrease over the course of our search:  the higher this value, the higher the 

def getTriangularNumbers(xmax, ymin):
    n = 0
    triangles = [0]
    step = 1
    while n < xmax or step < -ymin+1:
        n += step
        triangles.append(n)
        step += 1
    #One more past the end
    n += step
    triangles.append(n)
    return triangles

# def getHighestPoint(xInit, xSteps, yInit, ySteps, triangles):
#     while(yInit > -1):
#         if ySteps > xSteps:
#             yInit, ySteps = getYInitStepsLessThan(xSteps)
#         elif xSteps > ySteps:
#             xInit, xSteps = getXInitStepsLessThan(ySteps)
#         else:
#             return triangles[yInit]
#     return 0

def checkXStepsInf(xmin, xmax, triangles):
    for x in range(xmin, xmax+1):
        try:
            xInit = triangles.index(x)
            return xInit
        except:
            pass
    return -1
#The main loop
triangles = getTriangularNumbers(xmax, ymin)

ySteps = -2*ymin-1
xSteps = np.inf
yInit = -ymin-1
xInit = checkXStepsInf(xmin, xmax, triangles)
if xInit <= ySteps:
    print("Highest point is", triangles[yInit])
    sys.exit(0)






#The above script happens to work for part 1 for the example and for my input, so I'll implement this bit next:
#highest = getHighestPoint(xInit, xSteps, yInit, ySteps, triangles)

