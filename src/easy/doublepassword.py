a, b = input(), input()
number = 1
for c1, c2 in zip(a, b):
    if c1 == c2:
        number *= 1
    else:
        number *= 2
print(number)
