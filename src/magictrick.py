s = input()
counter = {}
guess = 1
for c in s:
    if c in counter:
        guess = 0
        break
    else:
        counter[c] = None
print(guess)
