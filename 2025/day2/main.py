import os 

with open (os.path.join(os.path.dirname(__file__), 'input')) as f:
    lines = f.read().splitlines()

ranges="".join(lines).split(',')
all_ids=[range(int(r.split('-')[0]),int(r.split('-')[1])+1) for r in ranges]
# part 1 and 2
def is_invalid(str_id):
    length=len(str_id)
    for i in range(1,length//2+1):
        if length % i != 0:
            continue
        if str_id == str_id[:i]*(length//i):
            return True
    return False

p1=0
p2=0
for ids in all_ids:
    for id in ids:
        str_id=str(id)
        if len(str_id) % 2 == 0:
            ind=len(str_id)//2
            if str_id[:ind]==str_id[ind:]:
                p1 += id
        if is_invalid(str_id):
            p2 += id
print(f'{p1=}')
print(f'{p2=}')