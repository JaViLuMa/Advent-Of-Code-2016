SALT = 'qzyelonm'

import hashlib
import itertools
import re
import sys
from collections import defaultdict

def getHash(s, part2=False):
    if part2:
        for _ in range(2017):
            s = hashlib.md5(s.encode()).hexdigest()

        return s

    return hashlib.md5(s.encode()).hexdigest()
    

def getTriples(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return s[i]

    return None

def getQuintuple(s):
    for i in range(len(s) - 4):
        if s[i] == s[i + 1] == s[i + 2] == s[i + 3] == s[i + 4]:
            return s[i]

    return None


def get_keys(salt, part2=False):
    keys = []
    index = 0
    hashes = defaultdict(lambda: None)

    while len(keys) < 64:
        if hashes[index] is None:
            hashes[index] = getHash(salt + str(index))

        triple = getTriples(hashes[index])

        if triple is not None:
            for i in range(1, 1001):
                if hashes[index + i] is None:
                    hashes[index + i] = getHash(salt + str(index + i), part2)

                if getQuintuple(hashes[index + i]) == triple:
                    keys.append(index)
                    break
        index += 1

    return keys


print(f'Part 1: {get_keys(SALT)[63]} | Part 2: {get_keys(SALT, True)[63]}')
