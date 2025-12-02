import os
import sys
sys.path.insert(0, "/Users/davide/projects/advent_of_code")
from read_input import read_input

data = read_input(os.path.split(os.path.split(__file__)[0])[1][3:])

data = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............",
]

freqs = []
antipods = []
for i,line in enumerate(data):
    for infr,fr in enumerate(line):
        if fr != '.' and fr not in freqs:
            freqs.append(fr)
            for il,checkline in enumerate(data[i+1:]):
                inds = [inf for inf,f in enumerate(checkline) if f == fr]
                antipods.extend([ant for ind in inds for ant in ((2*infr-ind,2*i-(il+i+1)),(2*ind-infr,2*(il+i+1)-i)) if ant[0] >= 0 and ant[0] < len(data[0]) and ant[1] >= 0 and ant[1] < len(data)])
unique = set(antipods)
print(len(unique))
newdata = [[n for n in line] for line in data]
for u in unique:
    newdata[u[1]][u[0]] = 'X'