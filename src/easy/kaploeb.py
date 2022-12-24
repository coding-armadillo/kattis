l, k, _ = [int(d) for d in input().split()]

record = {}
for _ in range(l):
    i, t = input().split()
    mm, ss = [int(d) for d in t.split(".")]
    s = mm * 60 + ss
    if i in record:
        record[i].append(s)
    else:
        record[i] = [s]

delete = [i for i in record if len(record[i]) != k]
for i in delete:
    record.pop(i)

sorted_i = sorted(record, key=lambda i: (sum(record[i]), int(i)))
print("\n".join(sorted_i))
