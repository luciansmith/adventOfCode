import numpy as np

example = False

filename = "day8_input.txt"
if (example):
    filename = "day8_example.txt"

counts = np.zeros(10)

def getDigitMapFrom(uniques):
    digitmap = dict()
    for unique in uniques:
        if len(unique) == 2:
            digitmap[unique] = 1
        if len(unique) == 3:
            digitmap[unique] = 7
        if len(unique) == 4:
            digitmap[unique] = 4
        if len(unique) == 7:
            digitmap[unique] = 8
    return digitmap


for line in open(filename):
    uniques, digits = line.strip().split(" | ")
    uniques = uniques.split(" ")
    digits = digits.split(" ")
    assert(len(uniques)==10)
    assert(len(digits)==4)
    for u in range(len(uniques)):
        uset = set()
        for letter in uniques[u]:
            uset.add(letter)
        uniques[u] = frozenset(uset)
    for d in range(len(digits)):
        dset = set()
        for letter in digits[d]:
            dset.add(letter)
        digits[d] = frozenset(dset)
    
    digitmap = getDigitMapFrom(uniques)
    for digit in digits:
        if digit in digitmap:
            counts[digitmap[digit]] += 1
            

print(counts)
print(sum(counts))
