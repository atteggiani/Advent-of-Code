#!/usr/bin/env python3
import os 

with open (os.path.join(os.path.dirname(__file__), 'test_input')) as f:
    lines = f.read().splitlines()

# part 1 and 2
n_b=[2,12]
for N in n_b:
    jolt=[]
    for line in lines:
        jlt=''
        R=N
        while R < len(line):
            val = max(line[:-R+1])
            jlt+=val
            ind = line.index(val)
            R-=1
            line=line[ind+1:]
            if R==1:
                val = max(line)
                jlt+=val
                break
        if R>1:
            jlt+=line
        jolt.append(int(jlt))
    # print(jolt)
    print(sum(jolt))