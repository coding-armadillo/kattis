h, n = [int(d) for d in input().split()]
damage = dict(
    zip(["standard", "fire", "ice", "light"], [int(d) for d in input().split()])
)
v = 0
for _ in range(n):
    v += damage[input()]
h -= v
if h <= 0:
    print("dead")
else:
    print(h)
