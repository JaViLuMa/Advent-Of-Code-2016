from typing import List, Union


def keypadCode(grid: Union[List[List[Union[int, str]]], List[List[int]]], moves: List[str], part2: bool = False) -> str:
    startingPosX: int = 1 if not part2 else 0
    startingPosY: int = 1 if not part2 else 2

    code = ''

    for move in moves:
        for c in move:
            if not part2:
                if c == 'U':
                    startingPosY = max(startingPosY - 1, 0)
                elif c == 'D':
                    startingPosY = min(startingPosY + 1, 2)
                elif c == 'L':
                    startingPosX = max(startingPosX - 1, 0)
                elif c == 'R':
                    startingPosX = min(startingPosX + 1, 2)

            else:
                if c == 'U':
                    if startingPosY - 1 >= 0 and grid[startingPosY - 1][startingPosX] != 0:
                        startingPosY -= 1
                elif c == 'D':
                    if startingPosY + 1 < len(grid) and grid[startingPosY + 1][startingPosX] != 0:
                        startingPosY += 1
                elif c == 'L':
                    if startingPosX - 1 >= 0 and grid[startingPosY][startingPosX - 1] != 0:
                        startingPosX -= 1
                elif c == 'R':
                    if startingPosX + 1 < len(grid[0]) and grid[startingPosY][startingPosX + 1] != 0:
                        startingPosX += 1

        code += str(grid[startingPosY][startingPosX])

    return code


keypadWhatIThink: List[List[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

keypadWhatItIs: List[List[Union[int, str]]] = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, 'A', 'B', 'C', 0],
    [0, 0, 'D', 0, 0]
]

moves: List[str] = []

with open('data.txt') as f:
    for line in f.read().split():
        moves.append(line)

print(f'Part 1: {keypadCode(keypadWhatIThink, moves)} | Part 2: {keypadCode(keypadWhatItIs, moves, True)}')

