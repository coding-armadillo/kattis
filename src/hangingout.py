l, x = [int(d) for d in input().split()]
o, r = 0, 0
for _ in range(x):
    action, n = input().split()
    n = int(n)
    if action == "leave":
        o -= n
    elif action == "enter":
        if o + n > l:
            r += 1
        else:
            o += n
print(r)
