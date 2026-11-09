t = int(input())
for _ in range(t):
    input()
    p = [int(d) for d in input().split()]
    print(len(set((d - 1) // 10 for d in p)))
