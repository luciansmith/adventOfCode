import numpy as np
import copy

values = []
ndigits = 0
#for line in open("day3_example.txt"):
for line in open("day3_input.txt"):
    line = line.strip()
    if len(line) > 0:
        ndigits = len(line) 
        values.append(line)

twos = []
for d in range(ndigits):
    twos.append(2**d)

twos.reverse()

def common(values, pos, moreOrLess):
    ones = []
    zeros = []
    for value in values:
        if value[pos] == "1":
            ones.append(value)
        else:
            zeros.append(value)
    # print("ones:", ones)
    # print("zeros:", zeros)
    if len(ones) == len(zeros):
        if moreOrLess:
            return ones
        return zeros
    if moreOrLess == (len(ones)>len(zeros)):
        return ones
    return zeros

oxygen = values
co2 = values
pos = 0

while len(oxygen)>1 and pos < ndigits:
    oxygen = common(oxygen, pos, True)
    # print(oxygen)
    pos += 1

pos = 0
while len(co2)>1 and pos < ndigits:
    co2 = common(co2, pos, False)
    # print(co2)
    pos += 1

def getVal(value, twos):
    ret = 0
    for n, digit in enumerate(value):
        if digit=="1":
           ret += twos[n]
    return ret

print (oxygen, co2)
oxygen = getVal(oxygen[0], twos)
co2 = getVal(co2[0], twos)
print (oxygen, co2)
print(oxygen*co2)

