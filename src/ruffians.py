t = int(input())
for _ in range(t):
    a, b, f = input().split(), input().split(), False
    for i in range(5):
        if a[i] in [b[j] for j in range(5) if i != j]:
            f = True
            break
    print("YES" if f else "NO")
