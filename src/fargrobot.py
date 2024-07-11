n = int(input())
s = input()
c = []
for _ in range(n):
    d = {k: s.index(k) for k in "RGB"}
    c.append(max(d, key=lambda k: d[k]))
    s = s[max(d.values()) + 1 :]
print("".join(c))
