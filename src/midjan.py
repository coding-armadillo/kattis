input()
n = [int(d) for d in input().split()]
m = [int(d) for d in input().split()]
print(*[d for d in n if d not in m])
print(*[d for d in m if d not in n])
