n = int(input())
v = sorted([int(d) for d in input().split()])

prev = v[0]
ans = {prev: 1}
for i in range(1, n):
    if v[i] == prev + ans[prev]:
        ans[prev] += 1
    else:
        prev = v[i]
        ans[prev] = 1

print(sum(ans.keys()))
