mapping = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
}


def f(d):
    if d < 13:
        return mapping[d]

    ones = d % 10
    if d < 20:
        return {3: "thir", 5: "fif", 8: "eigh"}.get(ones, mapping[ones]) + "teen"

    tens = d // 10
    return (
        {2: "twen", 3: "thir", 4: "for", 5: "fif", 8: "eigh"}.get(tens, mapping[tens])
        + "ty"
        + ("-" + mapping[ones] if ones else "")
    )


def t(w):
    if w.isdigit():
        return f(int(w))
    else:
        return w


while True:
    try:
        words = input()
    except:
        break
    print(" ".join([t(w) for w in words.split()]))
