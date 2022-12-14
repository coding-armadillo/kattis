n = int(input())
days = set()
for _ in range(n):
    start, end = [int(d) for d in input().split()]
    days.update(range(start, end + 1))
print(len(days))
