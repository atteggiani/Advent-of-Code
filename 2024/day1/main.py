import pandas as pd
import os 

input_file=os.path.split(__file__)[0]+'/input'
data=pd.read_csv(input_file, names=['A','B'])

#part 1
list1 = sorted(list(data['A']))
list2 = sorted(list(data['B']))

p1 = sum([abs(l1-l2) for l1,l2 in zip(list1,list2)])
print(p1)

#part 2
p2=sum([l*list2.count(l) for l in list1])
print(p2)
