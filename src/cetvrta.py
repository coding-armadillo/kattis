from collections import Counter

x, y = Counter(), Counter()

for _ in range(3):
    _x, _y = [int(d) for d in input().split()]
    x[_x] += 1
    y[_y] += 1


for key in x:
    if x[key] == 1:
        print(key, " ")
        break

for key in y:
    if y[key] == 1:
        print(key)
        break
