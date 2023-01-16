encoding = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "_": "..--",
    ",": ".-.-",
    ".": "---.",
    "?": "----",
}

decoding = dict([(v, k) for k, v in encoding.items()])

while True:
    try:
        encoded = input()
    except:
        break
    length = [len(encoding[c]) for c in encoded]
    morse = "".join([encoding[c] for c in encoded])

    ans, s = "", 0
    for i in reversed(length):
        ans += decoding[morse[s : s + i]]
        s += i
    print(ans)
