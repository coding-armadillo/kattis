n = int(input())
for _ in range(n):
    d = [int(v or 0) for v in input().split(",")]
    print(sum(v * (60**i) for i, v in enumerate(d[::-1])))
