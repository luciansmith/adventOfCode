import numpy as np

example = False

filename = "day8_input.txt"
if (example):
    filename = "day8_example.txt"


def getDigitMapFrom(uniques):
    digitmap = dict()
    reversemap = dict()
    upper = ""  #top line
    middle = "" #middle line
    lower = ""  #lower line
    ul = ""     #upper left
    ur = ""     #upper right
    ll = ""     #lower left
    lr = ""     #lower right
    
    #1, 7, 4, and 8 have unique set sizes
    for unique in uniques:
        if len(unique) == 2:
            digitmap[unique] = 1
            reversemap[1] = unique
        if len(unique) == 3:
            digitmap[unique] = 7
            reversemap[7] = unique
        if len(unique) == 4:
            digitmap[unique] = 4
            reversemap[4] = unique
        if len(unique) == 7:
            digitmap[unique] = 8
            reversemap[8] = unique

    #Diff between 7 and 1 is upper
    for letter in reversemap[7]:
        if letter not in reversemap[1]:
            upper = letter
    
    #size-six set without ur is 6, and tells us which is ur and lr
    for unique in uniques:
        if (len(unique)) == 6:
            for right in reversemap[1]:
                if right not in unique:
                    digitmap[unique] = 6
                    reversemap[6] = unique
                    ur = right
    for right in reversemap[1]:
        if right != ur:
            lr = right

    #Now we can tell the difference in the size-5 sets: missing UR is 5, missing LR is 2, missing neither is 3
    for unique in uniques:
        if (len(unique)) == 5:
            if ur not in unique:
                digitmap[unique] = 5
                reversemap[5] = unique
            elif lr not in unique:
                digitmap[unique] = 2
                reversemap[2] = unique
            else:
                digitmap[unique] = 3
                reversemap[3] = unique
    
    #And now we can tell UL and LR:
    for digit in reversemap[8]:
        if digit not in reversemap[2] and digit != lr:
            ul = digit
        if digit not in reversemap[5] and digit != ur:
            ll = digit
    
    #Only ones left are 9 and 0, which we can check ll for:
    for unique in uniques:
        if unique not in digitmap:
            if ll not in unique:
                digitmap[unique] = 9
                reversemap[9] = unique
            else:
                digitmap[unique] = 0
                reversemap[0] = unique

    print(reversemap.keys(), len(uniques))
    return digitmap, reversemap


counts = np.zeros(10)
values = []

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
    
    digitmap, reversemap = getDigitMapFrom(uniques)
    print(digits)
    value = 0
    for n, digit in enumerate(digits):
        val = digitmap[digit]
        if digit in digitmap:
            counts[val] += 1
        value += val * 10**(3-n)
    values.append(value)
            

print(counts)
print(sum(counts))

print(values)
print(sum(values))
