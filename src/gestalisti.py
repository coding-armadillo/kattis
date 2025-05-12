n = int(input())
l = set()
for _ in range(n):
    s, name = input().split()
    if s == "+":
        l.add(name)
    elif s == "-":
        l.remove(name)
    elif s == "?":
        print("Jebb" if name in l else "Neibb")
