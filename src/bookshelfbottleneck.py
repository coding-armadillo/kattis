n, H = [int(d) for d in input().split()]
w, f = 0, True
for _ in range(n):
    s = [int(d) for d in input().split()]
    a = [H - d for d in s]
    b = [d for d in a if d >= 0]
    if not b:
        f = False
        break
    else:
        i = a.index(min(b))
        w += min([s[j] for j in range(3) if j != i])
print(w if f else "impossible")
