n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))


def group_score(s):
    gs = 0
    for i in range(len(s)):
        gs += s[i] * (0.8**i)
    return 0.2 * gs


print(group_score(s))
new_gs = []
for i in range(n):
    new_gs.append(group_score([s[j] for j in range(n) if j != i]))
print(sum(new_gs) / len(new_gs))
