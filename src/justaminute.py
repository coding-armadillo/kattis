a, b = [], []
for _ in range(int(input())):
    x, y = [int(d) for d in input().split()]
    a.append(x * 60)
    b.append(y)
ans = sum(b) / sum(a)
if ans <= 1:
    ans = "measurement error"
print(ans)
