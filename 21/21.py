import re
from itertools import permutations


def swap(instruction: str, s: str) -> str:
    pattern = r'swap (position|letter) (\d+|.) with.*(\d+|.)'

    matches = re.match(pattern, instruction)

    if matches:
        if matches.group(1) == 'position':
            index1 = int(matches.group(2))
            index2 = int(matches.group(3))

            temp = list(s)

            temp[index1], temp[index2] = temp[index2], temp[index1]

            return ''.join(temp)

        elif matches.group(1) == 'letter':
            char1: str = matches.group(2)
            char2: str = matches.group(3)

            return s.replace(char1, '*').replace(char2, char1).replace('*', char2)

    return s


def rotateLeft(s: str, n: int) -> str:
    return s[n:] + s[0:n]


def rotateRight(s: str, n: int) -> str:
    return rotateLeft(s, len(s) - n)


def rotate(instruction: str, s: str) -> str:
    if 'based' in instruction:
        pattern = r'rotate based on position of letter (.)'

        match = re.match(pattern, instruction)

        if match:
            char: str = match.group(1)

            index = s.index(char)

            if index >= 4:
                index += 1

            return rotateRight(s, index + 1)

    elif 'left' in instruction or 'right' in instruction:
        pattern = r'rotate (right|left) (\d+).*'

        match = re.match(pattern, instruction)

        if match:
            direction: str = match.group(1)
            n: int = int(match.group(2))

            if direction == 'left':
                return rotateLeft(s, n)
            elif direction == 'right':
                return rotateRight(s, n)
    return s

            
def reverse(instruction: str, s: str) -> str:
    pattern = r'reverse positions (\d+) through (\d+)'

    matches = re.match(pattern, instruction)

    if matches:
        index1: int = int(matches.group(1))
        index2: int = int(matches.group(2))

        return s[0:index1] + s[index1:index2 + 1][::-1] + s[index2 + 1:]

    return s


def move(instruction: str, s: str) -> str:
    pattern = r'move position (\d+) to position (\d+)'

    matches = re.match(pattern, instruction)

    if matches:
        index1: int = int(matches.group(1))
        index2: int = int(matches.group(2))

        if index1 is not None and index2 is not None:
            temp = list(s)

            temp.insert(index2, temp.pop(index1))

            return ''.join(temp)

    return s


def scramble(instructions: list[str], s: str) -> str:
    for instruction in instructions:
        if 'swap' in instruction:
            s = swap(instruction, s)
        elif 'rotate' in instruction:
            s = rotate(instruction, s)
        elif 'reverse' in instruction:
            s = reverse(instruction, s)
        elif 'move' in instruction:
            s = move(instruction, s)

    return s


def unscramble(instructions: list[str], s: str, us: str) -> str:
    for p in permutations(s):
        if us == scramble(instructions, ''.join(p)):
            return ''.join(p)

    return ''


with open('data.txt') as f:
    instructions = f.read().splitlines()

scrambleMe = 'abcdefgh'
unscrambleMe = 'fbgdceah'

print(f'Part 1: {scramble(instructions, scrambleMe)} | Part 2: {unscramble(instructions, scrambleMe, unscrambleMe)}')
