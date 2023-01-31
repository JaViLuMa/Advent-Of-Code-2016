ranges = []

with open('data.txt') as f:
    lines = f.read().splitlines()

    for line in lines:
        beginning, end = line.split('-')

        ranges.append((int(beginning), int(end)))

ranges.sort()

lowest = 0

for beginning, end in ranges:
    if beginning > lowest + 1:
        break    

    lowest = max(lowest, end)

l = 0
allowed = 0

for beginning, end in ranges:
    if beginning > l + 1:
        allowed += beginning - l - 1

    l = max(l, end)

print(f'Part 1: {lowest + 1} | Part 2: {allowed}')

