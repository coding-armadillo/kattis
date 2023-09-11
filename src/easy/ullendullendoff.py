n = int(input())
names = input().split()
if n < 13:
    i = 13 % n - 1
else:
    i = 12
print(names[i])
