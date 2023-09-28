import string

uppers = string.ascii_uppercase


def unshift(c, k, f):
    index = uppers.index(k)
    if f:
        new_index = uppers.index(c) + index
    else:
        new_index = uppers.index(c) - index
    return uppers[new_index % 26]


message, key = input(), input()
print("".join([unshift(c, k, i % 2) for i, (c, k) in enumerate(zip(message, key))]))
