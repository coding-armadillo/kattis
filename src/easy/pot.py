n = int(input())
total = 0
for _ in range(n):
    line = input()
    n, p = int(line[:-1]), int(line[-1])
    total += n**p
print(total)
