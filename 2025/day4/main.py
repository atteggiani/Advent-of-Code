#!/usr/bin/env python3
import os 

with open (os.path.join(os.path.dirname(__file__), 'input')) as f:
    lines = f.read().splitlines()

# part 1 and 2
p=0
c=0
rolls=set([(x,y) for y,_ in enumerate(lines) for x,_ in enumerate(lines[0]) if lines[y][x]=='@'])
while True:
    c+=1
    newrolls = set()
    for xr,yr in rolls:
        count = 0
        count += bool((xr-1,yr-1) in rolls)
        count += bool((xr,yr-1) in rolls)
        count += bool((xr+1,yr-1) in rolls)
        count += bool((xr-1,yr+1) in rolls)
        count += bool((xr,yr+1) in rolls)
        count += bool((xr+1,yr+1) in rolls)
        count += bool((xr-1,yr) in rolls)
        count += bool((xr+1,yr) in rolls)
        if count <4:
            p+=1
        else:
            newrolls.add((xr,yr))
    if c==1:
        print('p1=',p)
    if rolls == newrolls:
        break
    rolls = newrolls
print('p2=',p)
    
