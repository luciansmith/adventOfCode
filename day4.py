import copy
import numpy as np

example = False
part1 = False

calllist = [15,62,2,39,49,25,65,28,84,59,75,24,20,76,60,55,17,7,93,69,32,23,44,81,8,67,41,56,43,89,95,97,61,77,64,37,29,10,79,26,51,48,5,86,71,58,78,90,57,82,45,70,11,14,13,50,68,94,99,22,47,12,1,74,18,46,4,6,88,54,83,96,63,66,35,27,36,72,42,98,0,52,40,91,33,21,34,85,3,38,31,92,9,87,19,73,30,16,53,80]
if (example):
    calllist= [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

allboards = []
blankboard = {
    "rows": [],
    "cols": [set(), set(), set(), set(), set()],
}
oneboard = copy.deepcopy(blankboard)

filename = "day4_input.txt"
if (example):
    filename = "day4_example.txt"

for line in open(filename):
    line = line.strip()
    if len(line)==0:
        allboards.append(oneboard)
        oneboard = copy.deepcopy(blankboard)
        continue
    lvec = line.split()
    for n in range(len(lvec)):
        lvec[n] = int(lvec[n])
        oneboard["cols"][n].add(lvec[n])
    oneboard["rows"].append(set(lvec))

# print(allboards)


def playBingo():
    finished = set()
    for call in calllist:
        print("removing", call)
        for bnum in range(len(allboards)):
            success = -1
            if bnum in finished:
                continue
            board = allboards[bnum]
            for rc in board:
                for vals in board[rc]:
                    try:
                        vals.remove(call)
                        if len(vals)==0:
                            success = call
                    except:
                        pass
            if (success > -1):
                if part1:
                    return success, board, bnum+1
                else:
                    finished.add(bnum)
                    print("Board", bnum, "wins with the number", call)
                    if len(finished) == len(allboards):
                        return success, board, bnum+1
                        

(success, board, bnum) = playBingo()
unmarked = 0
for vals in board["rows"]:
    unmarked += sum(vals)

print(unmarked, success, unmarked*success)
