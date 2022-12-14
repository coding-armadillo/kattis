while True:
    n = int(input())
    if n == -1:
        break
    miles = 0
    elapsed = 0
    for _ in range(n):
        s, t = [int(d) for d in input().split()]
        miles += s * (t - elapsed)
        elapsed = t
    print(f"{miles} miles")
