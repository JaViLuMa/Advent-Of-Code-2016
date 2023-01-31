BEGINNING_ROW = '^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^'


def getNextRow(row):
    newRow = ''
    for i in range(len(row)):
        if i == 0:
            left = '.'
        else:
            left = row[i-1]
        if i == len(row) - 1:
            right = '.'
        else:
            right = row[i+1]
        if (left == '^' and row[i] == '^' and right == '.') or (left == '.' and row[i] == '^' and right == '^') or (left == '^' and row[i] == '.' and right == '.') or (left == '.' and row[i] == '.' and right == '^'):
            newRow += '^'
        else:
            newRow += '.'
    return newRow


def countSafeTiles(row):
    return row.count('.')


def solve(rows):
    row = BEGINNING_ROW
    safeTiles = countSafeTiles(row)
    for _ in range(rows - 1):
        row = getNextRow(row)
        safeTiles += countSafeTiles(row)
    print(safeTiles)


print(f'Part 1: {solve(40)} | Part 2: {solve(400000)}')

