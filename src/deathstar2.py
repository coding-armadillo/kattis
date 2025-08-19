import string


def f(c):
    if c in "aeiou":
        return c
    elif c == "-":
        return "\n"
    elif c in string.digits:
        return bin(int(c))[2:]
    else:
        return "beepbloop"


print("".join(f(c) for c in input()))
