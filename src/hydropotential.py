v = []
for _ in range(6):
    v.append(int(input()))
for i in range(0, 6, 2):
    print(v[i] * v[i + 1] * 10)
