n = int(input())
a = input()
b = input()
m = 0
for i in range(n):
    d = abs(ord(a[i]) - ord(b[i]))
    m += min(d, 26 - d)
print(m)
