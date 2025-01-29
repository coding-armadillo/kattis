import string


def f(v):
    for i in range(len(v)):
        if v[i] in string.ascii_uppercase:
            return v[i:]


n = int(input())
names = [input() for _ in range(n)]
print(*sorted(names, key=lambda v: f(v)))
