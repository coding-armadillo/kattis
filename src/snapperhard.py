t = int(input())
for i in range(t):
    n, k = [int(d) for d in input().split()]
    on = True
    for _ in range(n):
        if not k % 2:
            on = False
        k //= 2
    print(f'Case #{i+1}: {"ON" if on else "OFF"}')
