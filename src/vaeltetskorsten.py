n = int(input())
l = []
for _ in range(n):
    a, b = input().split()
    if b == "nej":
        l.append(int(a))
print(max(l))
