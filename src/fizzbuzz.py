x, y, n = [int(d) for d in input().split()]
for i in range(1, n + 1):
    ans = ""
    if not i % x:
        ans += "Fizz"
    if not i % y:
        ans += "Buzz"
    if not ans:
        ans = i
    print(ans)
