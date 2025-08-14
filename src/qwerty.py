from string import ascii_lowercase

QWERTY = "qwertyuiopasdfghjklzxcvbnm"
m = dict(zip(ascii_lowercase, QWERTY))
input()
s = input()
print("".join(m.get(c, c) for c in s))
