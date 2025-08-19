n = int(input())

while True:
    n += 1
    v = n**2
    if "6" not in str(v):
        print(n)
        break
