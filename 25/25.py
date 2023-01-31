TARGET = 643 * 4

n = 1

while n < TARGET:
    if n % 2 == 0:
        n = (n * 2) + 1
    else:
        n = n * 2

print(n - TARGET)
