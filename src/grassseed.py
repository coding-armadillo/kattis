c = float(input())
total = 0
for _ in range(int(input())):
    w, l = [float(d) for d in input().split()]
    total += c * w * l
print(f"{total:.7f}")
