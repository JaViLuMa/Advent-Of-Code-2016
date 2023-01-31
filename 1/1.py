def calculate(instructions, directions, part2=False):
    direction = 0
    x, y = 0, 0
    seen = set()

    for lOrR, steps in instructions:
        direction = (direction + (1 if lOrR == 'R' else -1)) % 4

        dx, dy = directions[direction]

        for _ in range(steps):
            x += dx
            y += dy

            if part2 and (x, y) in seen:
                return abs(x) + abs(y)

            seen.add((x, y))

    return abs(x) + abs(y)


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open('data.txt') as f:
    instructions = [[x[0], int(x[1:])] for x in f.read().split(', ')]

print(f'Part 1: {calculate(instructions, directions)} | Part 2: {calculate(instructions, directions, part2=True)}')
