import os
import sys
sys.path.insert(0, "/Users/davide/projects/advent_of_code")
from read_input import read_input
from multiprocessing import Pool

data = read_input(os.path.split(os.path.split(__file__)[0])[1][3:])

def advance(i, direction):
    if direction == 'u':
        return (i[0],i[1]-1)
    elif direction == 'd':
        return (i[0],i[1]+1)
    elif direction == 'l':
        return (i[0]-1,i[1])
    elif direction == 'r':
        return (i[0]+1,i[1])

def change_dir(direction):
    if direction == 'u':
        return 'r'
    elif direction == 'r':
        return 'd'
    elif direction == 'd':
        return 'l'
    elif direction == 'l':
        return 'u'

# Find starting pos.
def init_ind(data):
    for il,line in enumerate(data):
        try:
            return (line.index('^'),il)
        except ValueError:
            continue

# data = [
#     "....#.....",
#     ".........#",
#     "..........",
#     "..#.......",
#     ".......#..",
#     "..........",
#     ".#..^.....",
#     "........#.",
#     "#.........",
#     "......#...",
# ]

def find_testinds(ind,direction):
    if direction == 'u':
        return [advance((ind[0],idy),direction) for idy in range(ind[1]+1)]
    if direction == 'r':
        return [advance((idx,ind[1]),direction) for idx in range(ind[0],len(data[0])+1)]
    if direction == 'd':
        return [advance((ind[0],idy),direction) for idy in range(ind[1],len(data))]
    if direction == 'l':
        return [advance((idx,ind[1]),direction) for idx in range(ind[0]+1)]

def run(index):
    ind = init_ind(data)
    newdata = [[d for d in lines] for lines in data]
    newdata[index[1]][index[0]] = '#'
    direction = 'u'
    tot = [(ind,direction)]
    while True:
        newind = advance(ind,direction)
        try:
            if newdata[newind[1]][newind[0]] in ['.','^']:
                ind = newind
                if (ind,direction) not in tot:
                    tot.append((ind,direction))
                else:
                    print(index)
                    return 1
            elif newdata[newind[1]][newind[0]] == '#':
                direction = change_dir(direction)
            continue
        except IndexError:
            return 0

inds = [(ic,il) for il,line in enumerate(data) for ic,char in enumerate(line) if data[il][ic] != '#']

if __name__ == '__main__':
    with Pool() as p:
        results = p.imap_unordered(run,inds)
        output = list(results)
    print(sum(output))

# if __name__ == '__main__':
#     with Pool() as p:
#         results = p.imap_unordered(run,[1,2,3])
#         output = list(results)
#     print(output)


# count = 0
# for il,line in enumerate(data):
#     for ic,char in enumerate(line):
#         count += run((ic,il))
# print(count)

