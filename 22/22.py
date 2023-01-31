import re


nodes = []


def nodeAsObject(node):
    return {
        'name': node[0],
        'size': int(node[1][:-1]),
        'used': int(node[2][:-1]),
        'avail': int(node[3][:-1]),
        'use%': int(node[4][:-1]),
    }


def createGridOfNodes(nodes):
    grid = [[{} for _ in range(28 + 1)] for _ in range(32 + 1)]

    for node in nodes:
        pattern = r'/dev/grid/node-x(\d+)-y(\d+)'

        coords = re.search(pattern, node[0])

        if coords:
            x, y = int(coords.group(1)), int(coords.group(2))

            grid[x][y] = nodeAsObject(node)

    return grid


def viablePairs(grid):
    pairs = 0

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            for x2 in range(len(grid)):
                for y2 in range(len(grid[x2])):
                    if grid[x][y]['used'] > 0 and grid[x][y]['used'] <= grid[x2][y2]['avail']:
                        pairs += 1

    return pairs


with open('data.txt') as f:
    for line in f:
        nodes.append(line.strip().split())

grid = createGridOfNodes(nodes)

numOfViablePairs = viablePairs(grid)

xCoord, yCoord = 0, 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y]['used'] == 0:
            xCoord, yCoord = x, y

totalMoves = xCoord + yCoord + 32 + (32 - 1) * 5

print(f'Part 1: {numOfViablePairs} | Part 2: {totalMoves}')

