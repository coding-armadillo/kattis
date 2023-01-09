for _ in range(int(input())):
    n = int(input())
    warehouse = {}
    for _ in range(n):
        s = input().split()
        name, quantity = s[0], int(s[1])
        if name not in warehouse:
            warehouse[name] = quantity
        else:
            warehouse[name] += quantity
    print(len(warehouse))
    names = sorted(warehouse)
    for name in sorted(
        warehouse, key=lambda k: (warehouse[k], -names.index(k)), reverse=True
    ):
        print(name, warehouse[name])
