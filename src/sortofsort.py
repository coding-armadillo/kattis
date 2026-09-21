n = int(input())
a = [int(d) for d in input().split()]
s = [a[0]]
for i in range(1, n):
    if a[i] >= s[-1]:
        s.append(a[i])
print(*s)
