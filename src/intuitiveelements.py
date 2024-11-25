t = int(input())
for _ in range(t):
    a, b = input(), input()
    if not set(b) - set(a):
        print("YES")
    else:
        print("NO")
