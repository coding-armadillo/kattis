w = input()
_ = input()
s = input().split()


def f(w, t):
    a, b, c = len(w), len(t), 0
    if a > b:
        return c
    for i in range(b - a + 1):
        if t[i : i + a] == w:
            c += 1
    return c


print(sum(f(w, t) for t in s if w in t))
