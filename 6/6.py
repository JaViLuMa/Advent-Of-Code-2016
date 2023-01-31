from collections import Counter


with open('data.txt') as f:
    lines = f.read().splitlines()

errorCorrectedMessage = ''
actualErrorCorrectedMessage = ''

for i in range(len(lines[0])):
    errorCorrectedMessage += Counter([line[i] for line in lines]).most_common()[0][0]

    actualErrorCorrectedMessage += Counter([line[i] for line in lines]).most_common()[-1][0]

print(f'Part 1: {errorCorrectedMessage} | Part 2: {actualErrorCorrectedMessage}')

