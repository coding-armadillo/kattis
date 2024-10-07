n = int(input())
d = [int(input()) for _ in range(n)]
print(sum(v % 2 for v in d))
