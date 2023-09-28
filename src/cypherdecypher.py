from string import ascii_uppercase


def f(n, m):
    return ascii_uppercase[(n * m) % 26]


m = input()
for _ in range(int(input())):
    s = input()
    print("".join([f(ascii_uppercase.index(c), int(d)) for c, d in zip(s, m)]))
