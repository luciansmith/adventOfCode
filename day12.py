example = True

filename = "day12_input.txt"
if example:
    filename = "day12_example.txt"

cavemap = {}
capmap = {}
for line in open(filename):
    (left, right) = line.strip().split("-")
    if left not in cavemap:
        cavemap[left] = []
        capmap[left] = 'a' <= left[0] and left[0] <= 'z'
    if right not in cavemap:
        cavemap[right] = []
        capmap[right] = 'a' <= right[0] and right[0] <= 'z'
    cavemap[left].append(right)
    cavemap[right].append(left)

def explore(location, cavemap, visited):
    if location=="end":
        return [[location]]
    routes = []
    downvisits = visited.copy()
    downvisits.append(location)
    for nextcave in cavemap[location]:
        if capmap[nextcave] and nextcave in visited:
            continue
        for subroute in explore(nextcave, cavemap, downvisits):
            if len(subroute)==0:
                continue
            subroute.insert(0, location)
            routes.append(subroute)
    return routes
    
        
        

visited = []
routes = explore("start", cavemap, visited)
print(routes)
print(len(routes))
