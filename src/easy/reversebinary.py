n = int(input())

b = []
while n:
    b.append(n % 2)
    n //= 2

print(sum([d * (2**p) for d, p in zip(b, reversed(range(len(b))))]))
