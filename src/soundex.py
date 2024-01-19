m = {
    "B": 1,
    "F": 1,
    "P": 1,
    "V": 1,
    "C": 2,
    "G": 2,
    "J": 2,
    "K": 2,
    "Q": 2,
    "S": 2,
    "X": 2,
    "Z": 2,
    "D": 3,
    "T": 3,
    "L": 4,
    "M": 5,
    "N": 5,
    "R": 6,
}

while True:
    try:
        s = input()
        s = [str(m.get(c, "")) for c in s]
        prev = s[0]
        ans = [prev]
        for c in s[1:]:
            if c != prev:
                ans.append(c)
                prev = c
        print("".join(ans))
    except:
        break
