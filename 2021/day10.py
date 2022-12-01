example = False

filename = "day10_input.txt"
if (example):
    filename = "day10_example.txt"
    

def checkParens(line):
    expect_stack = []
    for ch in line:
        #Open
        if ch=="(":
            expect_stack.append(")")
        elif ch=="{":
            expect_stack.append("}")
        elif ch=="<":
            expect_stack.append(">")
        elif ch=="[":
            expect_stack.append("]")
        #Close
        elif ch==")" or ch=="}" or ch==">" or ch=="]":
            endch = expect_stack.pop()
            if endch != ch:
                return (ch, endch)
        else:
            raise ValueError("Unexpected character " + ch);
    expect_stack.reverse()
    return expect_stack

pointvals = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

pointvals_autocomp = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

score = 0
sortscores = []
for line in open(filename):
    ret = checkParens(line.strip())
    if type(ret) is tuple:
        print(line.strip(), ": expected", ret[1], "but found", ret[0], ":", pointvals[ret[0]], "points")
        score = score + pointvals[ret[0]]
    else:
        print(line.strip(), "complete with", ret)
        sortscore = 0
        for ch in ret:
            sortscore = sortscore * 5 + pointvals_autocomp[ch]
        sortscores.append(sortscore)

print("Error score:", score)

sortscores.sort()
print("Autocomplete score:", sortscores[round((len(sortscores)-1)/2)])
