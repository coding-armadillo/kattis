n = int(input())
p = int(input())
s = [int(d) for d in input().split()]
for i in range(p, p + n):
    if i not in s:
        print(i)
