n = int(input())
res = ["Gnomes:"]
for _ in range(n):
    a, b, c = [int(d) for d in input().split()]
    res.append("Ordered" if (a <= b and b <= c) or (a >= b and b >= c) else "Unordered")
print(*res, sep="\n")
