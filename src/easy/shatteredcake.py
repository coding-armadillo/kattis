w, n = int(input()), int(input())
total = 0
for _ in range(n):
    _w, _l = [int(d) for d in input().split()]
    total += _w * _l
print(int(total / w))
