NUM_OF_ELVES = 3004953

n = 0

while pow(2, n) < NUM_OF_ELVES:
    n += 1

remainder = NUM_OF_ELVES - pow(2, n - 1)

w = 1

for i in range(1, NUM_OF_ELVES):
    w = w % i + 1

    if w > (i + 1) / 2:
        w += 1

print(f'Part 1: {2 * remainder + 1} | Part 2: {w}')

