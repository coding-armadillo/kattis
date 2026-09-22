n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v
m = int(input())
for _ in range(m):
    w = input()
    print(d.get(w, f"?{w}?") if w.isalpha() else w)
