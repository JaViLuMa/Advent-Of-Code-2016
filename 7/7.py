import re


def isABBA(string):
    for i in range(len(string) - 3):
        a, b, c, d = string[i], string[i + 1], string[i + 2], string[i + 3]
        
        if a == d and b == c and a != b:
            return True
    
    return False

    
with open('data.txt') as file:
    lines = [re.split(r'\[([^\]]+)\]', line) for line in file]
    
    parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]

TLS = sum(isABBA(ip) and not(isABBA(hyperNet)) for ip, hyperNet in parts)

SSL = 0

for ip, hyperNet in parts:
    for a, b, c in zip(ip, ip[1:], ip[2:]):
        if a == c and a != b:
            if b + a + b in hyperNet:
                SSL += 1

                break

print(f'Part 1: {TLS} | Part 2: {SSL}')

