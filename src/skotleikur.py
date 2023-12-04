k = int(input())
a = int(input())
b = int(input())
ans = []
for i in range(0, k // a + 1):
    if (k - a * i) % b == 0:
        ans.append((i, (k - a * i) // b))
print(len(ans))
for i, j in ans:
    print(i, j)
