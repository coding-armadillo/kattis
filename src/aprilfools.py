from string import ascii_uppercase

n = int(input())
for _ in range(n):
    s = int(input())
    d = dict(
        zip(
            ascii_uppercase,
            ascii_uppercase[-s:] + ascii_uppercase[:-s],
        )
    )
    print("".join(d.get(c, c) for c in input()))
