from copy import deepcopy


def cpy(x, y, registers):
    if x in registers:
        registers[y] = registers[x]
    else:
        registers[y] = int(x)


def inc(x, registers):
    registers[x] += 1


def dec(x, registers):
    registers[x] -= 1


def jnz(x, y, registers):
    if x in registers:
        x = registers[x]
    else:
        x = int(x)

    if y in registers:
        y = registers[y]
    else:
        y = int(y)

    if x != 0:
        return y
    else:
        return 1


def tgl(x, registers, instructions, i):
    if x in registers:
        x = registers[x]
    else:
        x = int(x)

    if i + x >= len(instructions):
        return 1

    instruction = instructions[i + x].split()

    if len(instruction) == 2:
        if instruction[0] == 'inc':
            instruction[0] = 'dec'
        else:
            instruction[0] = 'inc'
    else:
        if instruction[0] == 'jnz':
            instruction[0] = 'cpy'
        else:
            instruction[0] = 'jnz'
    instructions[i + x] = ' '.join(instruction)

    return 1


def setRegisters(instructions, registers):
    i = 0

    while i < len(instructions):
        if i > len(instructions):
            break

        instruction = instructions[i].split()

        if instruction[0] == 'cpy':
            cpy(instruction[1], instruction[2], registers)
            i += 1

        elif instruction[0] == 'inc':
            inc(instruction[1], registers)
            i += 1

        elif instruction[0] == 'dec':
            dec(instruction[1], registers)
            i += 1

        elif instruction[0] == 'jnz':
            i += jnz(instruction[1], instruction[2], registers)

        elif instruction[0] == 'tgl':
            i += tgl(instruction[1], registers, instructions, i)
    
    return registers['a']


with open('data.txt') as f:
    instructions = f.read().splitlines()

instructionsCopy = deepcopy(instructions)

registerA7 = { 'a': 7, 'b': 0, 'c': 0, 'd': 0 }
registerA12 = { 'a': 12, 'b': 0, 'c': 0, 'd': 0 }

sevenEggs = setRegisters(instructions, registerA7)
twelveEggs = setRegisters(instructionsCopy, registerA12)

print(f'Part 1: {sevenEggs} | Part 2: {twelveEggs}')
