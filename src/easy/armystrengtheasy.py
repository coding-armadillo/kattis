t = int(input())
for _ in range(t):
    input()
    ng, nm = [int(d) for d in input().split()]
    g = [int(d) for d in input().split()]
    m = [int(d) for d in input().split()]
    if max(m) > max(g):
        print("MechaGodzilla")
    else:
        print("Godzilla")
