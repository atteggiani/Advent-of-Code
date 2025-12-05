#!/usr/bin/env python3
import os 

with open (os.path.join(os.path.dirname(__file__), 'input')) as f:
    lines = f.read().splitlines()

ind=lines.index('')
fresh_ranges = lines[:ind]
ingredients = lines[ind+1:]

# part 1
p1=0
for ing in ingredients:
    ing = int(ing)
    for fr in fresh_ranges:
        frmin,frmax = fr.split('-')
        if ing >= int(frmin) and ing <= int(frmax):
            # fresh.append(ing)
            p1+=1
            break
print(p1)

# part 2
int_fresh_ranges = [[int(fr.split('-')[0]),int(fr.split('-')[1])] for fr in fresh_ranges]

# int_fresh_ranges = [[1,2]]*4

joined_fr=int_fresh_ranges[:1]

for fr in int_fresh_ranges[1:]:
    new=fr
    new_joined_fr=joined_fr.copy()
    # print(f"new: {new}")
    for i,jfr in enumerate(joined_fr):
        jfrmin,jfrmax=jfr
        if new[1] < jfrmin or new[0] > jfrmax:
            continue
        elif new[0] >= jfrmin and new[1] > jfrmax:
            new[0]=jfrmax+1
            # print("new0+1")
        elif new[0] < jfrmin and new[1] <= jfrmax:
            new[1]=jfrmin-1
            # print("new1-1")
        elif new[0] < jfrmin and new[1] > jfrmax:
            del new_joined_fr[i]
            # print(f"del {i}")
        elif new[0] >= jfrmin and new[1] <= jfrmax:
            # print(f"no new")
            new=None
            break
    if new is None:
        continue
    new_joined_fr.append(new)
    joined_fr=new_joined_fr
    # print(f"appended {new}")


# print(joined_fr)
print(sum((jfr[1]-jfr[0]+1) for jfr in joined_fr))