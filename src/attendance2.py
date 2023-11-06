n = int(input())
s = []
for _ in range(n):
    c = input()
    if c == "Present!":
        s.pop()
    else:
        s.append(c)
if not s:
    print("No Absences")
else:
    print("\n".join(s))
