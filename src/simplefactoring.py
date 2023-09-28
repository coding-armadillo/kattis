for _ in range(int(input())):
    a, b, c = [int(d) for d in input().split()]
    import math

    if not b**2 - 4 * a * c < 0 and math.sqrt(b**2 - 4 * a * c).is_integer():
        print("YES")
    else:
        print("NO")
