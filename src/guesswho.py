n, m, q = [int(d) for d in input().split()]
M = []
for _ in range(n):
    M.append(input())
Q = []
for _ in range(q):
    Q.append(input().split())
ans = [all([c[int(i) - 1] == v for i, v in Q]) for c in M]
if sum(ans) > 1:
    print("ambiguous")
    print(sum(ans))
else:
    print("unique")
    print(ans.index(True) + 1)
