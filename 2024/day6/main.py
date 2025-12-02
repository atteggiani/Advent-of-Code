import os
import sys
sys.path.insert(0, "/Users/davide/projects/advent_of_code")
from read_input import read_input
import time

data = read_input(os.path.split(os.path.split(__file__)[0])[1][3:])

#part 1

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

# tot = []
# ind = init_ind(data)
# tot.append(ind)
# direction = 'u'
# while True:
#     newind = advance(ind,direction)
#     try:
#         if data[newind[1]][newind[0]] in ['.','^']:
#             ind = newind
#             if ind not in tot:
#                 tot.append(ind)
#             continue
#         elif data[newind[1]][newind[0]] == '#':
#             direction = change_dir(direction)
#             continue
#     except IndexError:
#         break
# print(len(tot))

#part 2

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

def change_newdata(ind,direction,event='forward'):
    if event == 'forward':
        if (d:=newdata[ind[1]][ind[0]]) != 'O':
            if d in ['|','—']:
                newdata[ind[1]][ind[0]] = '+'
            elif direction in ['u','d']:
                newdata[ind[1]][ind[0]] = '|'
            else:
                newdata[ind[1]][ind[0]] = '—'
    if event == 'turn' and newdata[ind[1]][ind[0]] != 'O':
        newdata[ind[1]][ind[0]] = '+'
    if event == 'obs':
        newdata[ind[1]][ind[0]] = 'O'

tot = []
ind = init_ind(data)
direction = 'u'
tot.append((ind,direction))
obs = []
newdata = [[d for d in lines] for lines in data]
while True:
    # printdata()
    newind = advance(ind,direction)
    try:
        if data[newind[1]][newind[0]] in ['.','^']:
            ind = newind
            if (ind,direction) not in tot:
                tot.append((ind,direction))
            change_newdata(ind,direction)
            # check close loop
            testobs = advance(ind,direction)
            if data[testobs[1]][testobs[0]] in ['.',"^"]:
                newdir = change_dir(direction)
                testinds = find_testinds(ind,newdir)
                if any([(ti,newdir) in tot for ti in testinds]) and testobs not in obs:
                    obs.append(testobs)
                    change_newdata(testobs,direction,'obs')
            continue
        elif data[newind[1]][newind[0]] == '#':
            direction = change_dir(direction)
            change_newdata(ind,direction,'turn')
            continue
    except IndexError:
        break
print(len(obs))
