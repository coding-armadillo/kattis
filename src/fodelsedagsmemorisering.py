n = int(input())
records = {}
for _ in range(n):
    s, c, date = input().split()
    c = int(c)
    date = "".join(date.split("/")[::-1])
    if date not in records:
        records[date] = (s, c)
    else:
        _, _c = records[date]
        if c > _c:
            records[date] = (s, c)
print(len(records.keys()))
ordered_keys = sorted(records, key=lambda k: records[k][0])
for key in ordered_keys:
    print(records[key][0])
