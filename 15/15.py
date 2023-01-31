import re
from typing import List, Tuple


def parseInput() -> list[tuple[int, int, int]]:
    with open('data.txt') as f:
        lines = f.read().splitlines()

    discs = []

    for line in lines:
        matches = re.match(r'Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).', line)

        if matches:
            discs.append((int(matches.group(1)), int(matches.group(2)), int(matches.group(4))))

    return discs


def discInPosition(disc: tuple[int, int, int], time) -> bool:
    discId, positions, position = disc

    return (discId + position + time) % positions == 0


def fallsThrough(discs: list[tuple[int, int, int]], time: int) -> bool:
    for disc in discs:
        if not discInPosition(disc, time):
            return False

    return True


def solve(discs: list[tuple[int, int, int]]) -> int:
    time = 0

    while True:
        time += 1

        if fallsThrough(discs, time):
            return time



discs = parseInput()

discsWithAdditionalDisc = discs + [(7, 11, 0)]

print(f'Part 1: {solve(discs)} | Part 2: {solve(discsWithAdditionalDisc)}')
