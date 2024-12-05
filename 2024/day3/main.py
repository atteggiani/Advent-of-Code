import pandas as pd
import os 
import re

input_file=os.path.split(__file__)[0]+'/input'

with open(input_file) as f:
    data = f.readlines()

data = "".join(data)

# part1
valid = re.findall(r'mul\(\d*,\d*\)', data)

def mul(a,b):
    return a*b

print(sum([eval(x) for x in valid]))

# part2

splitted = [line.split("do()") for line in data.split("don't()")]
valid_data = "".join(splitted[0]+["".join(f[1:]) for f in splitted[1:] if len(f) > 1])
valid = re.findall(r'mul\(\d*,\d*\)', valid_data)
print(sum([eval(x) for x in valid]))