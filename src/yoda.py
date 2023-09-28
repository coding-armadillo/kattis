a, b = input(), input()
size = max(len(a), len(b))

a = [int(d) for d in a.zfill(size)]
b = [int(d) for d in b.zfill(size)]

ans_a = [d1 for d1, d2 in zip(a, b) if d1 >= d2]
ans_b = [d2 for d1, d2 in zip(a, b) if d2 >= d1]


def f(ans):
    if not ans:
        return "YODA"
    else:
        return int("".join([str(d) for d in ans]))


print(f(ans_a))
print(f(ans_b))
