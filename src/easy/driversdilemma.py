c, x, m = [float(d) for d in input().split()]
top = 0
for _ in range(6):
    mph, mpg = [float(d) for d in input().split()]

    if m / mph * x + m / mpg <= c / 2:
        top = mph
if top:
    print(f"YES {top:.0f}")
else:
    print("NO")
