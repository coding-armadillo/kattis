from string import ascii_letters, digits


def f(w):
    if set(digits) & set(w) and set(ascii_letters) & set(w):
        return "*" * len(w)
    else:
        return w


print(*[f(w) for w in input().split()])
