import pandas as pd
import os 
import re

input_file=os.path.split(__file__)[0]+'/input'

with open(input_file) as f:
    data = f.readlines()

# Part 1

word = 'XMAS'
lw = len(word)
count = 0
for y,line in enumerate(data):
    for x,letter in enumerate(line.split()[0]):
        if letter == 'X':
            c=0
            print(x,y)
            #ff
            if x + lw <= len(data[y]):
                c+=data[y][x:x+lw] == word
                if data[y][x:x+lw] == word:
                    print("ff")
            #bb
            if x - lw + 1 >= 0:
                c+=data[y][x-lw+1:x+1][::-1] == word
                if data[y][x-lw+1:x+1][::-1] == word:
                    print("bb")
            #dd
            if y + lw <= len(data):
                c+=''.join([data[y+i][x] for i in range(lw)]) == word
                if ''.join([data[y+i][x] for i in range(lw)]) == word:
                    print("dd")
            #uu
            if y - lw + 1 >= 0:
                c+=''.join([data[y-i][x] for i in range(lw)]) == word
                if ''.join([data[y-i][x] for i in range(lw)]) == word:
                    print("uu")
            #fd
            if (x + lw < len(data[y])) and (y + lw <= len(data)):
                c+=''.join([data[y+i][x+i] for i in range(lw)]) == word
                if ''.join([data[y+i][x+i] for i in range(lw)]) == word:
                    print("fd")
            #fu
            if (x + lw < len(data[y])) and (y - lw + 1 >= 0):
                c+=''.join([data[y-i][x+i] for i in range(lw)]) == word
                if ''.join([data[y-i][x+i] for i in range(lw)]) == word:
                    print("fu")
            #bu
            if (x - lw + 1 >= 0) and (y - lw + 1 >= 0):
                c+=''.join([data[y-i][x-i] for i in range(lw)]) == word
                if ''.join([data[y-i][x-i] for i in range(lw)]) == word:
                    print("bu")
            #bd
            if (x - lw + 1 >= 0) and (y + lw <= len(data)):
                c+=''.join([data[y+i][x-i] for i in range(lw)]) == word
                if ''.join([data[y+i][x-i] for i in range(lw)]) == word:
                    print("bd")
            count+=c
print(count)

# Part 2
count = 0
valid = ['MMSS','MSSM','SSMM','SMMS']
for y,line in enumerate(data):
    for x,letter in enumerate(line.split()[0]):
        if letter == 'A' and (
        y-1 >= 0 and y+1 < len(data) and x-1 >= 0 and x+1 < len(data[y])) and (
            ''.join([data[y-1][x-1],data[y-1][x+1],data[y+1][x+1],data[y+1][x-1]]) in valid):
            count+=1
print(count)