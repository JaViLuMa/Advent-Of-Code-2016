def isTriangle(triangles):
    validTriangles = []

    for triangle in triangles:
        triangle = sorted(triangle)

        if triangle[0] + triangle[1] > triangle[2]:
            validTriangles.append(triangle)

    return validTriangles


triangleSides = []

with open('data.txt') as f:
    for line in f:
        triangleSides.append([int(x) for x in line.split()])

validTrianglesWithoutGroups = isTriangle(triangleSides)

groupsOfTriangles = []

for i in range(0, len(triangleSides), 3):
    for j in range(3):
        groupsOfTriangles.append([triangleSides[i][j], triangleSides[i+1][j], triangleSides[i+2][j]])

validTriangles = isTriangle(groupsOfTriangles)

print(f'Part 1: {len(validTrianglesWithoutGroups)} | Part 2: {len(validTriangles)}')

