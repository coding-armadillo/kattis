prev = 1
for _ in range(int(input())):
    a, op, b = input().split()
    a, b = int(a), int(b)
    if op == "+":
        ans = a + b - prev
    elif op == "-":
        ans = (a - b) * prev
    elif op == "*":
        ans = (a * b) ** 2
    elif op == "/":
        ans = (a + 1) // 2 if a % 2 else a // 2

    print(ans)
    prev = ans
