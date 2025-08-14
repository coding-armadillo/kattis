from string import ascii_lowercase

s = input()
a = [c for c in ascii_lowercase if c not in s]
print("Good job!" if not a else "".join(a))
