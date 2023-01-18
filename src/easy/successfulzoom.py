n = int(input())
x = [int(d) for d in input().split()]
found = False
for k in range(1, n // 2 + 1):
    v = [x[i] for i in range(k - 1, n, k)]
    if all([v[i] < v[i + 1] for i in range(len(v) - 1)]):
        print(k)
        found = True
        break
if not found:
    print("ABORT!")
