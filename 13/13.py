FAV_NUMBER = 1358

def isWall(x, y):
    value = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + FAV_NUMBER

    ones = bin(value).count('1')
    
    return ones % 2 == 1


traversed = {(1, 1)}

steps = 0

newPlaces = traversed

fewestNumberOfSteps = None
distinctPathsBeforeReaching50Steps = None

while fewestNumberOfSteps is None or distinctPathsBeforeReaching50Steps is None:
    toCheck = newPlaces.copy()
    newPlaces = set()

    for oldX, oldY in toCheck:
        for x, y in [(oldX + 1, oldY), (oldX - 1, oldY), (oldX, oldY + 1), (oldX, oldY - 1)]:
            if x < 0 or y < 0 or (x, y) in traversed or isWall(x, y):
                continue

            traversed.add((x, y))
            newPlaces.add((x, y))
    steps += 1

    if (31, 39) in newPlaces:
        fewestNumberOfSteps = steps

    if steps == 50:
        distinctPathsBeforeReaching50Steps = len(traversed)

print(f'Part 1: {fewestNumberOfSteps} | Part 2: {distinctPathsBeforeReaching50Steps}')
