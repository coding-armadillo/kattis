n, m = [int(_) for _ in input().split()]
d = [int(_) for _ in input().split()]
d = [v > m for v in d]


for k in range(n):
    if not d[k]:
        break

if all(d):
    print("It had never snowed this early!")
else:
    print(f"It hadn't snowed this early in {k} years!")
