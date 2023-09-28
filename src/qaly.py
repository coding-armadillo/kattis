qaly = 0
for _ in range(int(input())):
    q, y = input().split()
    q, y = float(q), float(y)
    qaly += q * y
print(qaly)
