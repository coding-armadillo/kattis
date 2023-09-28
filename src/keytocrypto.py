import string

uppers = string.ascii_uppercase


def decrypt(c, k):
    index = (uppers.index(c) - uppers.index(k)) % 26
    return uppers[index]


m, w = input(), input()

size_w = len(w)
size_m = len(m)
o = []
for i in range(0, size_m, size_w):
    if i + size_w < size_m:
        l = zip(m[i : i + size_w], w)
    else:
        l = zip(m[i:], w)
    t = "".join([decrypt(c, k) for c, k in l])
    o.append(t)
    w = t
print("".join(o))
