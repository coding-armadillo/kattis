n = int(input())
while True:
    sd = sum([int(d) for d in str(n)])
    if not n % sd:
        break
    n += 1
print(n)
