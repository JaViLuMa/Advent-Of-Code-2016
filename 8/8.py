import numpy as np
import os
from time import sleep


def pprint(grid):
    for row in grid:
        print(*row, sep='')

    sleep(0.1)


grid = np.full((6, 50), '░')

operations = {}

with open('data.txt') as f:
    for index, line in enumerate(f.read().splitlines()):
        if 'rect' in line:
            operations[index] = ('rect', int(line[5:line.index('x')]), int(line[line.index('x') + 1:]))
        
        elif 'rotate row' in line:
            operations[index] = ('row', int(line[13:line.index(' by')]), int(line[line.index('by ') + 3:]))
            
        elif 'rotate column' in line:
            operations[index] = ('col', int(line[16:line.index(' by')]), int(line[line.index('by ') + 3:]))


for operation in operations.values():
    os.system('cls')

    if operation[0] == 'rect':
        grid[:operation[2], :operation[1]] = '█'

        pprint(grid)

    elif operation[0] == 'row':
        grid[operation[1]] = np.roll(grid[operation[1]], operation[2])

        pprint(grid)

    elif operation[0] == 'col':
        grid[:, operation[1]] = np.roll(grid[:, operation[1]], operation[2])

        pprint(grid)

print(f'Part 1: {np.sum(grid == "█")}')
