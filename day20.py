import numpy as np
example = False

filename = "day20_input.txt"
if example:
    filename = "day20_example.txt"

def getRow(image, row, col, width, height):
    if row==-1 or row==height:
        return edge*3
    if col==0:
        return edge + image[row][col:col+2]
    elif col > width-2:
        return image[row][col-1:col+1] + edge
    else:
        return image[row][col-1:col+2]

def getBinaryPixelsAround(image, row, col, width, height):
    ret = ""
    #First row
    ret += getRow(image, row-1, col, width, height)
    ret += getRow(image, row, col, width, height)
    ret += getRow(image, row+1, col, width, height)
    assert(len(ret)==9)
    return ret;
    
def getValueFor(image, algmap, row, col, width, height):
    val = getBinaryPixelsAround(image, row, col, width, height)
    val = int(val, 2)
    return algmap[val]

def arrayToString(image):
    ret = []
    for row in image:
        strs = ""
        for col in row:
            if (col):
                strs = strs + "1"
            else:
                strs = strs + "0"
        ret.append(strs)
    return ret

#Main algorithm
iterations = 50
edge = "0"
algmap = {}
image = []
for line in open(filename):
    line = line.strip()
    line = line.replace("#", "1")
    line = line.replace(".", "0")
    if len(algmap)==0:
        algmap = line
        continue
    if len(line)==0:
        continue
    image.append(edge*50*2 + line + edge*50*2)

for n in range(iterations):
    image.insert(0, "0"*len(image[0]))
    image.insert(0, "0"*len(image[0]))
    image.append("0"*len(image[0]))
    image.append("0"*len(image[0]))

width = len(image[0])
height = len(image)


for n in range(iterations):
    image2 = np.zeros([height, width])
    for row in range(height):
        for col in range(width):
            image2[row][col] = getValueFor(image, algmap, row, col, width, height)
    
    if edge == "0" and algmap[0] == "1":
        edge = "1"
    elif edge == "1" and algmap[-1] == "0":
        edge = "0"
    
    print(sum(sum(image2)))
    image = arrayToString(image2)
    

