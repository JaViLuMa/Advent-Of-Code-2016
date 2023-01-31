from hashlib import md5
from itertools import compress

KEY = "qtetzkpl"

def doors(path):
    string = (KEY + ''.join(path)).encode('utf-8')

    return (int(x, 16) > 10 for x in md5(string).hexdigest()[:4])

def bfs(start, goal):
    queue = [(start, [start], [])]
    
    while queue:
        (x, y), path, directions = queue.pop(0)

        moves = {
            'U': lambda x, y: (x, y - 1),
            'D': lambda x, y: (x, y + 1),
            'L': lambda x, y: (x - 1, y),
            'R': lambda x, y: (x + 1, y)
        }

        for direction in compress('UDLR', doors(directions)):
            nextMove = moves[direction](x, y)

            nextX, nextY = nextMove

            if not (0 <= nextX < 4 and 0 <= nextY < 4):
                continue
            elif nextMove == goal:
                yield directions + [direction]
            else:
                queue.append((nextMove, path + [nextMove], directions + [direction]))


paths = list(bfs((0, 0), (3, 3)))

print(f'Part 1: {"".join(paths[0])} | Part 2: {len(paths[-1])}')
