s = input()

for c in "aeiou":
    s = s.replace(f"{c}p{c}", c)

print(s)
