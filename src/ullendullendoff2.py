n = int(input())
names = [input() for _ in range(n)]
s = 12 if n >= 13 else 13 % n - 1
names[0], names[s] = names[s], names[0]
print("\n".join(names))
