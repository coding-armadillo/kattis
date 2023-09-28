l, d, x = input(), input(), input()
l, d, x = int(l), int(d), int(x)

for i in range(l, d + 1):
    if sum([int(d) for d in str(i)]) == x:
        print(i)
        break

for i in range(d, l - 1, -1):
    if sum([int(d) for d in str(i)]) == x:
        print(i)
        break
