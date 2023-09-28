n, x = [int(d) for d in input().split()]
for _ in range(n):
    x -= int(input())
    if x < 0:
        print("Neibb")
        break
if x >= 0:
    print("Jebb")
