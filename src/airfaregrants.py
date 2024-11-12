n = int(input())
p = [int(input()) for _ in range(n)]
print(max(0, min(p) - max(p) // 2))
