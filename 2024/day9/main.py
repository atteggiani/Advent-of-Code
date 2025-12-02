import os
import sys
sys.path.insert(0, "/Users/davide/projects/advent_of_code")
from read_input import read_input

data = read_input(os.path.split(os.path.split(__file__)[0])[1][3:])

# part 1
data = '2333133121414131402'

blocks = data[::2]
free_spaces = data[1::2]

final = ''
for i,b in enumerate(blocks):


