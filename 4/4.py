import re


with open('data.txt') as f:
    data = f.read().splitlines()


def decrypt(name, sector):
    result = ''

    for c in name:
        if c == '-':
            result += ' '
        else:
            result += chr(((ord(c) - ord('a') + sector) % 26) + ord('a'))

    return result


sum = 0
northPoleSector = 0

for line in data:
    matches = re.match(r'(.*)-(\d+)\[(.*)\]', line)

    if matches:
        name, sector, checksum = matches.groups()

        letters = {}

        if decrypt(name, int(sector)) == 'northpole object storage':
            northPoleSector = int(sector)

        for c in name:
            if c == '-':
                continue
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        letters = sorted(letters.items(), key=lambda x: (-x[1], x[0]))

        if ''.join([x[0] for x in letters[:5]]) == checksum:
            sum += int(sector)


print(f'Part 1: {sum} | Part 2: {northPoleSector}')

