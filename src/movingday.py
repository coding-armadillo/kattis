n, v = [int(d) for d in input().split()]
b = []
for _ in range(n):
    l, w, h = [int(d) for d in input().split()]
    b.append(l * w * h)
print(max(b) - v)
