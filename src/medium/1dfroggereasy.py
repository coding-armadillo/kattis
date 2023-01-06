n, s, m = [int(d) for d in input().split()]
b = [int(d) for d in input().split()]
visited, hops = set(), 0
while True:
    if s in visited:
        print("cycle")
        break
    elif s < 1:
        print("left")
        break
    elif s > n:
        print("right")
        break
    elif b[s - 1] == m:
        print("magic")
        break
    else:
        visited.add(s)
        s += b[s - 1]
        hops += 1
print(hops)
