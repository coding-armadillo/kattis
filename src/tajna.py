s = input()

l = len(s)
r = int(l**0.5)
while l % r:
    r -= 1
c = l // r

parts = [s[i : i + r] for i in range(0, l, r)]

print("".join(["".join([row[i] for row in parts]) for i in range(r)]))
