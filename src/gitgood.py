f = []
g = set()
for _ in range(int(input())):
    a, b = input().split()
    if a == "cd":
        if b == "..":
            f.pop()
        else:
            f.append(b)
    else:
        g.add("/".join(f + [b]))
if g:
    for i in sorted(g):
        print(f"git add {i}")
    print("git commit")
    print("git push")
