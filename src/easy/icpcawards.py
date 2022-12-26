n = int(input())
shown = {}
for _ in range(n):
    u, t = input().split()
    if u not in shown and len(shown.keys()) < 12:
        print(u, t)
        shown[u] = True
