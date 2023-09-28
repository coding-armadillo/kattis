from itertools import product

p = input()
ans = []
for i in range(len(p)):
    for t in product("24", repeat=i + 1):
        if int(p) % int("".join(t)) == 0:
            ans.append(int("".join(t)))
print("\n".join([str(d) for d in sorted(ans)]))
