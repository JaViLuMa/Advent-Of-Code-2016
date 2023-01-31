DISK_SIZE_ONE = 272
DISK_SIZE_TWO = 35651584

INPUT = '11101000110010100'


def dragonCurve(a: str):
    b: str = a[::-1]
    b: str = b.translate(str.maketrans('01', '10'))

    return a + '0' + b


def checksum(data: str):
    checksumString = ''

    for i in range(0, len(data), 2):
        if data[i] == data[i + 1]:
            checksumString += '1'
        else:
            checksumString += '0'

    if len(checksumString) % 2 == 0:
        return checksum(checksumString)
    else:
        return checksumString


def solve(diskSize: int):
    data: str = INPUT

    while len(data) < diskSize:
        data = dragonCurve(data)

    data = data[:diskSize]

    return checksum(data)


print(f'Part 1: {solve(DISK_SIZE_ONE)} | Part 2: {solve(DISK_SIZE_TWO)}')
