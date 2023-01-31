from hashlib import md5


doorId = 'abbhdwsy'

password = ''
secondPassword = '________'

i = 0

while len(password) < 8 or '_' in secondPassword:
    hash = md5((doorId + str(i)).encode()).hexdigest()

    if hash.startswith('00000'):
        if len(password) < 8:
            password += hash[5]

        if hash[5].isdigit() and int(hash[5]) < 8 and secondPassword[int(hash[5])] == '_':
            secondPassword = secondPassword[:int(hash[5])] + hash[6] + secondPassword[int(hash[5]) + 1:]

    i += 1

print(f'Part 1: {password} | Part 2: {secondPassword}')
