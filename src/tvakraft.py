n = int(input())
while n:
    if n == 1:
        print("Yes")
        break
    elif n % 2:
        print("No")
        break
    else:
        n //= 2
