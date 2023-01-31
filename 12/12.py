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
        if registers[x] != 0:
            return int(y)
    else:
        if int(x) != 0:
            return int(y)
    return 1


def setRegisters(instructions, registers):
    i = 0

    while i < len(instructions):
        instruction = instructions[i]

        if instruction.startswith('cpy'):
            cpy(*instruction[4:].split(), registers)
        elif instruction.startswith('inc'):
            inc(*instruction[4:].split(), registers)
        elif instruction.startswith('dec'):
            dec(*instruction[4:].split(), registers)
        elif instruction.startswith('jnz'):
            i += jnz(*instruction[4:].split(), registers) - 1

        i += 1

    return registers['a']


with open('data.txt') as f:
    instructions = f.read().splitlines()

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
registersWithInitializedC = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

print(f'Part 1: {setRegisters(instructions, registers)} | Part 2: {setRegisters(instructions, registersWithInitializedC)}')
