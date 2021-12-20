example = False

filename = "day12_input.txt"
if example:
    filename = "day12_example2.txt"

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

def explore(location, cavemap, visited, smalltwice):
    if location=="end":
        return [[location]]
    routes = []
    downvisits = visited.copy()
    downvisits.append(location)
    for nextcave in cavemap[location]:
        st = smalltwice
        if nextcave == "start":
            continue
        if capmap[nextcave] and nextcave in visited:
            if st:
                continue
            st = True
        for subroute in explore(nextcave, cavemap, downvisits, st):
            if len(subroute)==0:
                continue
            subroute.insert(0, location)
            routes.append(subroute)
    return routes
    
        
        

visited = []
routes = explore("start", cavemap, visited, True)
print("Without revisiting any small cave:", len(routes))

routes = explore("start", cavemap, visited, False)
print("With one allowed small cave revisit:", len(routes))
