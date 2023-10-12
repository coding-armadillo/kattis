import math

for _ in range(int(input())):
    s = input()
    for n in range(1, len(s) + 1):
        if (s[:n] * math.ceil(len(s) / n)).startswith(s):
            print(n)
            break
