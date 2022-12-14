n = int(input())
awake = [0] * n
s = list(input())
for i in range(n):
    if s[i] == "1":
        awake[i] = 1
        if i + 1 < n:
            awake[i + 1] = 1
        if i + 2 < n:
            awake[i + 2] = 1
print(sum(awake))
