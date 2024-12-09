n = int(input())
b = 0
for _ in range(n):
    input()
    b += int(input())
if b == 0:
    print("Lagom")
elif b > 0:
    print("Usch, vinst")
else:
    print("Nekad")
