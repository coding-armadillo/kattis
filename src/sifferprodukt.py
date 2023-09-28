def digit_product(x):
    ans = 1
    while x:
        ans *= x % 10 or 1
        x //= 10
    return ans


x = int(input())
while True:
    x = digit_product(x)
    if x < 10:
        break
print(x)
