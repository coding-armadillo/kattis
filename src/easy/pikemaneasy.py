def f(n, time, l):
    total_time, penalty = 0, 0
    for i, t in enumerate(sorted(l)):
        if total_time + t > time:
            return i, penalty
        total_time += t
        penalty = (penalty + total_time) % 1_000_000_007
    return n, penalty


n, t = [int(d) for d in input().split()]
a, b, c, t0 = [int(d) for d in input().split()]
l = [t0]
for _ in range(n - 1):
    l.append(((a * l[-1] + b) % c) + 1)


n, penalty = f(n, t, l)
print(n, penalty)
