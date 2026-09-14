from string import ascii_uppercase

s = set(input())
a = [c for c in ascii_uppercase if c not in s]
print("Alphabet Soup!" if not a else "".join(a))
