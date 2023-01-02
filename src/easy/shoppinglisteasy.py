n, m = [int(d) for d in input().split()]
items = []
for _ in range(n):
    items.append(set(input().split()))

ans = items[0]
ans = ans.intersection(*items[1:])

print(len(ans))
print("\n".join(sorted(list(ans))))
