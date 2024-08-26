_ = input()
w = input().split()
m = int(input())
d = {}
for _ in range(m):
    k, v = input().split()
    d[k] = v
print(*[d[k] for k in w])
