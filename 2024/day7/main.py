import os
import sys
sys.path.insert(0, "/Users/davide/projects/advent_of_code")
from read_input import read_input
from itertools import product

data = read_input(os.path.split(os.path.split(__file__)[0])[1][3:])

#part 1

all_results=[]
numbers = []
for d in data:
    if d[-1] == ':':
        all_results.append(int(d[:-1]))
        numbers.append([])
    else:
        numbers[-1].append(d)

# def calc_results(nums, operators = ['+', '*']):
#     results = []
#     for op in product(operators,repeat=len(nums)-1):
#         res = nums[0]
#         for i,o in enumerate(op):
#             res = str(eval(''.join([res,o,nums[i+1]])))
#         results.append(int(res))
#     return results

# count = 0
# for ir,r in enumerate(all_results):
#     if r in calc_results(numbers[ir]):
#         count += r
# print(count)

#part 2
# all_results = [190,3267,83,156,7290,161011,192,21037,292]
# numbers = [
#     ['10', '19'],
#     ['81', '40', '27'],
#     ['17', '5'],
#     ['15', '6'],
#     ['6', '8', '6', '15'],
#     ['16', '10', '13'],
#     ['17', '8', '14'],
#     ['9', '7', '18', '13'],
#     ['11', '6', '16', '20'],
# ]

def calc_results(nums, operators = ['+', '*', '']):
    results = []
    for op in product(operators,repeat=len(nums)-1):
        res = nums[0]
        for i,o in enumerate(op):
            res = str(eval(''.join([res,o,nums[i+1]])))
        results.append(int(res))
    return results

count = 0
for ir,r in enumerate(all_results):
    if r in calc_results(numbers[ir]):
        count += r
print(count)
