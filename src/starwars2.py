n = int(input())
x = sorted(int(d) for d in input().split())
print(*(x[n // 3 : -n // 3] + x[: n // 3] + x[-n // 3 :]))
