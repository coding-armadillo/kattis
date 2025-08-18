n = int(input())
s = []
for _ in range(n):
    s.append(input())

v = 0
for i in range(1, n):
    v += abs(ord(s[i][0]) - ord(s[i - 1][0])) + abs(ord(s[i][1]) - ord(s[i - 1][1]))
print(v)
