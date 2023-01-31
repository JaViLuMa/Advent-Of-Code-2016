from itertools import permutations


def generateGrid(gridRows):
    grid = []
    numbersToVisit = []
    zeroCoords = (0, 0)

    for row in gridRows:
        gridCols = []

        for col in list(row):
            gridCols.append(col)

            if col == '0':
                zeroCoords = (gridRows.index(row), row.index(col))

            if col != '0' and col.isdigit():
                numbersToVisit.append((int(col), (gridRows.index(row), row.index(col))))

        grid.append(gridCols)

    return grid, numbersToVisit, zeroCoords


def bfs(s, e, grid):
    moves = set([(-1, 0), (1, 0), (0, 1), (0, -1)])

    queue = [(s, [s])]
    visited = set()
    visited.add(s)

    while queue:
        node, path = queue.pop(0)

        if node == e:
            return path

        for move in moves:
            newX = node[0] + move[0]
            newY = node[1] + move[1]

            if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] != '#' and (newX, newY) not in visited:
                queue.append(((newX, newY), path + [(newX, newY)]))
                visited.add((newX, newY))

    return -1


def findShortestPath(grid, numsToVisitPermutations, zeroCoords, part2=False):
    shortestPath = float('inf')

    for permutation in numsToVisitPermutations:
        path = 0

        if part2:
            permutation = [(0, zeroCoords)] + list(permutation) + [(0, zeroCoords)]
        else:
            permutation = [(0, zeroCoords)] + list(permutation)

        for i in range(len(permutation) - 1):
            paths = bfs(permutation[i][1], permutation[i + 1][1], grid)
            
            path += len(paths) - 1

        shortestPath = min(shortestPath, path)

    return shortestPath


with open('data.txt') as f:
    lines = f.read().splitlines()

grid, numbersToVisit, zeroCoords = generateGrid(lines)

numsToVisitPermutations = list(permutations(numbersToVisit))

print(f'Part 1: {findShortestPath(grid, numsToVisitPermutations, zeroCoords)} | Part 2: {findShortestPath(grid, numsToVisitPermutations, zeroCoords, part2=True)}')
