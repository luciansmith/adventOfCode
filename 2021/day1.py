import numpy

prev = numpy.inf
prev2 = numpy.inf
prev3 = numpy.inf
increases = 0
for line in open("day1_input.txt"):
# for line in open("day1_example.txt"):
    next = int(line.strip())
    if prev3 < next:
        increases += 1
    prev3 = prev2
    prev2 = prev
    prev  = next

print(increases)
