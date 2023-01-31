def decompress(string):
    decompressed = ''
    index = 0

    while index < len(string):
        if string[index] == '(':
            end = string.index(')', index)

            length, times = map(int, string[index + 1:end].split('x'))

            decompressed += string[end + 1:end + 1 + length] * times

            index = end + 1 + length
        else:
            decompressed += string[index]

            index += 1

    return decompressed


def ofCourseThereIsMoreDecompressing(string):
    decompressed = 0
    index = 0

    while index < len(string):
        if string[index] == '(':
            end = string.index(')', index)

            length, times = map(int, string[index + 1:end].split('x'))

            decompressed += ofCourseThereIsMoreDecompressing(string[end + 1:end + 1 + length]) * times

            index = end + 1 + length
        else:
            decompressed += 1

            index += 1

    return decompressed


with open('data.txt') as f:
    compressedInput = f.read().strip()


print(f'Part 1: {len(decompress(compressedInput))} | Part 2: {ofCourseThereIsMoreDecompressing(compressedInput)}')
