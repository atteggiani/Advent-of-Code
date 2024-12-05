import pandas as pd
import os

input_file=os.path.split(__file__)[0]+'/input'
input_file2=os.path.split(__file__)[0]+'/input2'

data=pd.read_csv(input_file, names=['X','Y'], sep='|')
R = list(zip(data['X'],data['Y']))

with open(input_file2) as f:
    pn = f.readlines()
pn = [list(eval(p.strip())) for p in pn]

# Part 1 and Part 2
p1 = 0
p2 = 0
for page in pn:
    r=[y for x,y in R if x in page and y in page]
    sortedpage = sorted(page,key=r.count)
    if page == sortedpage:
        p1 += page[len(page)//2]
    else:
        p2 += sortedpage[len(sortedpage)//2]
print(p1,p2)