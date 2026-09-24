input()
p = input()
m = int(input())
for _ in range(m):
    a, b = input().split()
    if a == p:
        p = b
    elif b == p:
        p = a
    else:
        pass
print(p)
