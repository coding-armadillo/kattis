n = int(input())
f = True
for _ in range(n):
    h = int(input())
    if h < 48:
        f = False
print("True" if f else "False")
