n, m = [int(d) for d in input().split()]
ans = ["?"] * n
valid = True
for _ in range(m):
    s, k = input().split()
    s = int(s)
    for a, b in zip(ans[s - 1 : s - 1 + len(k)], list(k)):
        if a != "?" and a != b:
            valid = False
    ans[s - 1 : s - 1 + len(k)] = list(k)
print("".join(ans) if valid else "Villa")
