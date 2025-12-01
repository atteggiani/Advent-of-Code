import os 

with open (os.path.join(os.path.dirname(__file__), 'input')) as f:
    lines = f.read().splitlines()

# with open (os.path.join(os.path.dirname(__file__), 'test_input')) as f:
#     lines = f.read().splitlines()

#part 1 and 2
numbers=[50]
p1=0
p2=0
rotations=[int(line[1:])*(1 if line.startswith('R') else -1) for line in lines]
for rotation in rotations:
    current=numbers[-1]
    raw_new = (current+rotation)
    new = raw_new%100
    numbers.append(new)
    if new == 0:
        p1 += 1
    p2 += abs(raw_new//100)
    if raw_new <= 0:
        if new == 0:
            p2 += 1
        if current == 0:
            p2 -= 1
    # print(f'Current: {current}, Rotation: {rotation}, Raw_new: {raw_new}, New: {new}, p2: {p2}')

print(f'{p1=}')
print(f'{p2=}')
# print(numbers)
