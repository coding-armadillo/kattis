import math

for _ in range(int(input())):
    m = input()
    k = math.ceil(len(m) ** 0.5)

    m += "*" * (k * k - len(m))
    rows = [m[i : i + k] for i in range(0, len(m), k)]

    s = []
    for i in range(k):
        s.append("".join([row[i] for row in rows if row[i] != "*"][::-1]))
    print("".join(s))
