n = int(input())
d150 = n // 150
n %= 150
d30 = n // 30
n %= 30
d15 = n // 15
n %= 15
d5 = n // 5
n %= 5
d1 = n
print(d1, d5, d15, d30, d150)
