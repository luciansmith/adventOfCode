import copy

polymap = {
    "BB": "N",
    "BC": "B",
    "BH": "H",
    "BN": "B",
    "CB": "H",
    "CC": "N",
    "CH": "B",
    "CN": "C",
    "HB": "C",
    "HC": "B",
    "HH": "N",
    "HN": "C",
    "NB": "B",
    "NC": "B",
    "NH": "C",
    "NN": "C",
    }

init = "PBFNVFFPCPCPFPHKBONB"
count = dict()

polymap.clear()
for n in open("day14input.txt"):
    (pp, x) = n.strip().split(" -> ")
    polymap[pp] = x
    count[x] = 0

for pp in polymap:
    x = polymap[pp]
    polymap[pp] = [pp[0] + x, x + pp[1], 0.0]

poly1 = copy.deepcopy(polymap)
poly2 = copy.deepcopy(polymap)

for n in range(len(init)-1):
    poly1[init[n] + init[n+1]][2] += 1
    count[init[n]] = 0
count[init[-1]] = 0



# poly1["NN"][2] = 1
# poly1["NC"][2] = 1
# poly1["CB"][2] = 1

first = init[0]
last = init[-1]

def iterate(poly1, poly2):
    for pp in poly1:
        (p1, p2, n) = poly1[pp]
        poly2[p1][2] += n
        poly2[p2][2] += n

for n in range(40):
    print("\nstep", str(n+1))
    iterate(poly1, poly2)
    poly1 = copy.deepcopy(poly2)
    poly2 = copy.deepcopy(polymap)
    
for pp in poly1:
    count[pp[0]] += poly1[pp][2]/2
    count[pp[1]] += poly1[pp][2]/2

count[first] += .5
count[last] += .5

print(count)

vec = []
for el in count:
    vec.append(count[el])
print(sum(vec))

print(max(vec) - min(vec))
