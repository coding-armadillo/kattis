t = int(input())
for _ in range(t):
    a = int(input().replace(" ", ""))
    b = int(input().replace(" ", ""))
    print(" ".join(str(a + b)))
