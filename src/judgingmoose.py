l, r = [int(d) for d in input().split()]
if not l and not r:
    print("Not a moose")
else:
    p = 2 * max(l, r)
    print("Odd" if l != r else "Even", p)
