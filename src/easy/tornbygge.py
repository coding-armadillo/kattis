_ = input()
n = 0
top = 0
for d in [int(d) for d in input().split()]:
    if not top or d > top:
        n += 1
    top = d

print(n)
