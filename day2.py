forward = 0
down = 0
aim = 0

part = 2

for line in open("day2_input.txt"):
# for line in open("day1_example.txt"):
    (direction, val) = line.strip().split()
    val = int(val)
    if (part == 1):
        if direction=="forward":
            forward += val
        elif direction=="down":
            down += val
        elif direction=="up":
            down -= val
        else:
            raise ValueError("Unknown direction")
    else:
        if direction=="forward":
            forward += val
            down += aim*val
        elif direction=="down":
            aim += val
        elif direction=="up":
            aim -= val
        else:
            raise ValueError("Unknown direction")
        

print(forward, down, forward*down)
