c = int(input())
shares = {}
days = set()
for i in range(c):
    k = int(input())
    record = {}
    for _ in range(k):
        n, d = [int(d) for d in input().split()]
        days.add(d)
        record[d] = n
    shares[i] = record

days = sorted(list(days))
ans = [0] * c
for i in range(len(days)):
    d = days[i]
    a = list(shares[j].get(d, ans[j]) for j in shares)
    ans = a
    print(sum(a), end=" ")
