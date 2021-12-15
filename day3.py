import numpy as np

ones = np.zeros(50)

nlines = 0
ndigits = 0
for line in open("day3_input.txt"):
    line = line.strip()
    if len(line) > 0:
        ndigits = len(line) 
        nlines += 1
        for (n, digit) in enumerate(line):
            if digit=="1":
                ones[n] += 1

twos = []
for d in range(ndigits):
    twos.append(2**d)

twos.reverse()

gamma = 0
epsilon = 0
for (n, place) in enumerate(twos):
    if ones[n] > nlines/2:
        gamma += place
    else:
        epsilon += place

print(gamma, epsilon, gamma*epsilon)
