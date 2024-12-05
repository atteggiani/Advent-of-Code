import pandas as pd
import os 

input_file=os.path.split(__file__)[0]+'/input'

data=pd.read_csv(input_file, names=['data'])
data = [[int(n) for n in l.split()] for l in list(data['data'])]

#part 1
safe = []
for line in data:
    for i,n in enumerate(line):
        if i == 0:
            nprev = n
            continue
        if n - nprev in [1,2,3]:
            if i == 1:
                pos=True
            elif not pos:
                break
            elif i == len(line)-1:
                safe.append(line)
        elif n - nprev in [-1,-2,-3]:
            if i == 1:
                pos=False
            elif pos:
                break
            elif i == len(line)-1:
                safe.append(line)
        else:
            break
        nprev = n

print(len(safe))

#part 2

safe = []
for line in data:
    lngth = len(safe)
    for k in range(len(line)):
        if len(safe) != lngth:
            break
        newline = line[0:k]+line[k+1:]
        for i,n in enumerate(newline):
            if i == 0:
                nprev = n
                continue
            if n - nprev in [1,2,3]:
                if i == 1:
                    pos=True
                elif not pos:
                    break
                elif i == len(newline)-1:
                    safe.append(newline)
            elif n - nprev in [-1,-2,-3]:
                if i == 1:
                    pos=False
                elif pos:
                    break
                elif i == len(newline)-1:
                    safe.append(newline)
            else:
                break
            nprev = n

print(len(safe))