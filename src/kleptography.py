from string import ascii_lowercase as l


n, m = [int(d) for d in input().split()]
p = input()
c = input()
p = p[::-1]
c = c[::-1]

ans = ""
for i in range(0, m, n):
    if i + n < m:
        part = c[i : i + n]
    else:
        part = c[i:]

    ans += p
    p = "".join([l[(l.index(a) - l.index(b)) % 26] for a, b in zip(part, p)])

ans += p
print(ans[::-1][n:])
