n = int(input())
e = 1
m = 1
for i in range(1, n + 1):
    m *= i
    e += 1 / m
print(e)
