while True:
    n = int(input())
    if not n:
        break
    record = {}
    for _ in range(n):
        order = input().split()
        name = order[0]
        items = order[1:]
        for item in items:
            if item not in record:
                record[item] = [name]
            else:
                record[item].append(name)
    for name in sorted(record):
        print(name, " ".join(sorted(record[name])))
    print()
