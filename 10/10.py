import re, collections


bot = collections.defaultdict(list)
output = collections.defaultdict(list)

with open('data.txt') as fp:
    instructions = fp.read().splitlines()

pipeline = {}

for line in instructions:
    if line.startswith('value'):
        pattern = r'value (\d+) goes to bot (\d+)'

        matches = re.search(pattern, line)
        
        if matches:
            n, b = map(int, matches.groups())
            bot[b].append(n)

    if line.startswith('bot'):
        pattern = r'bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)'

        matches = re.search(pattern, line)

        if matches:
            who, t1, n1, t2, n2 = matches.groups()

            pipeline[int(who)] = (t1, int(n1)),(t2, int(n2))

botComparing61And17 = None

while bot:
    for k,v in dict(bot).items():
        if len(v) == 2:
            v1, v2 = sorted(bot.pop(k))

            if v1 == 17 and v2 == 61:
                botComparing61And17 = k

            (t1,n1),(t2,n2) = pipeline[k]

            eval(t1)[n1].append(v1)
            eval(t2)[n2].append(v2)


a, b, c = (output[k][0] for k in [0, 1, 2])

print(f'Part 1: {botComparing61And17} | Part 2: {a * b * c}')
