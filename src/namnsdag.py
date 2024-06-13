s = input()
n = int(input())
names = [input() for _ in range(n)]
for i in range(n):
    if len(s) != len(names[i]):
        continue

    if sum(a != b for a, b in zip(s, names[i])) <= 1:
        print(i + 1)
        break
