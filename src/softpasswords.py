from string import ascii_lowercase, ascii_uppercase, digits

s = input()
p = input()
m = dict(zip(ascii_lowercase + ascii_uppercase, ascii_uppercase + ascii_lowercase))

if s == p:
    print("Yes")
elif s[-1] in digits and s[:-1] == p:
    print("Yes")
elif s[0] in digits and s[1:] == p:
    print("Yes")
elif s == "".join(m.get(c, c) for c in p):
    print("Yes")
else:
    print("No")
