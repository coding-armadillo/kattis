s = input()
i, m, p = 0, {}, None

for c in s:
    if c.isupper():
        m[i] = 1
        p = i
        i += 1
    else:
        m[p] += 1

print(
    sum(
        4 - m[k] % 4 if m[k] % 4 else (4 if not m[k] else 0)
        for k in list(m.keys())[:-1]
    )
)
