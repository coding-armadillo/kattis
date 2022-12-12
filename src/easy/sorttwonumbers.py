line = input()
a, b = [int(d) for d in line.split()]
if a < b:
    print(a, b)
else:
    print(b, a)
