from random import randint

s = int(input())
while True:
    a = randint(-999, 999)
    b = s - a
    if a == 0 or b == 0 or abs(a) > 999 or abs(b) > 999:
        continue
    print(a, b)
    break
