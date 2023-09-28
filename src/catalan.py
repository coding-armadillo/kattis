# https://en.wikipedia.org/wiki/Catalan_number
p = [1]
for i in range(10000):
    p.append(p[-1] * (i + 1))

for _ in range(int(input())):
    n = int(input())
    print(p[2 * n] // (p[n + 1] * p[n]))
