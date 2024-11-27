def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


c, i = 0, 2
while c < 100:
    if is_prime(i):
        print(i)
        c += 1
    i += 1
