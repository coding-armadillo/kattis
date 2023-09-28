while True:
    n = int(input())
    if not n:
        break
    a, b = [], []
    for _ in range(n):
        a.append(int(input()))
    for _ in range(n):
        b.append(int(input()))
    mapping = dict(zip(sorted(a), sorted(b)))
    for key in a:
        print(mapping[key])
    print()
