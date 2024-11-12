n = int(input())
ma, mb = -1, 200001
for _ in range(n):
    a, b = [int(d) for d in input().split()]
    if a > ma:
        ma = a
    if b < mb:
        mb = b
    if ma > mb:
        break
if ma <= mb:
    print(mb - ma + 1, ma)
else:
    print("bad news")
