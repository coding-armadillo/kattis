n, a, b = [int(d) for d in input().split()]
fizzbuzz, fizz, buzz = 0, 0, 0
for i in range(1, n + 1):
    if not i % a and not i % b:
        fizzbuzz += 1
    elif not i % a:
        fizz += 1
    elif not i % b:
        buzz += 1
print(fizz, buzz, fizzbuzz)
