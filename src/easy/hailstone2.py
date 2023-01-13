n = int(input())
s = [n]
while True:
    v = s[-1]
    if v == 1:
        break
    elif v % 2 == 0:
        s.append(v // 2)
    else:
        s.append(3 * v + 1)
print(len(s))
