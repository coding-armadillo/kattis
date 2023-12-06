a, b = input().split()
a = list(a)[::-1]
for i in range(len(a)):
    if a[i] == "5":
        a[i] = "2"
    elif a[i] == "2":
        a[i] = "5"
b = list(b)[::-1]
for i in range(len(b)):
    if b[i] == "5":
        b[i] = "2"
    elif b[i] == "2":
        b[i] = "5"
a, b = int("".join(a)), int("".join(b))
if a > b:
    print(1)
else:
    print(2)
