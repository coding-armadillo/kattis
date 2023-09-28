n = int(input())
names = []
for _ in range(n):
    names.append(input())
order = []
for i in range(1, n):
    order.append(names[i] > names[i - 1])
if all(order):
    print("INCREASING")
elif not any(order):
    print("DECREASING")
else:
    print("NEITHER")
