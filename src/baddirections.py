t = int(input())
for _ in range(t):
    k, n = input().split()
    k = int(k)
    print("".join([str((int(c) + k) % 10) for c in n]))
