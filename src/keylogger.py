n = int(input())
mapping = {
    "clank": "a",
    "bong": "b",
    "click": "c",
    "tap": "d",
    "poing": "e",
    "clonk": "f",
    "clack": "g",
    "ping": "h",
    "tip": "i",
    "cloing": "j",
    "tic": "k",
    "cling": "l",
    "bing": "m",
    "pong": "n",
    "clang": "o",
    "pang": "p",
    "clong": "q",
    "tac": "r",
    "boing": "s",
    "boink": "t",
    "cloink": "u",
    "rattle": "v",
    "clock": "w",
    "toc": "x",
    "clink": "y",
    "tuc": "z",
    "whack": " ",
}
cap = False
shift = False
res = ""
for _ in range(n):
    s = input()
    if s == "bump":
        cap = not cap
    elif s == "dink":
        shift = True
    elif s == "thumb":
        shift = False
    elif s == "pop":
        res = res[:-1]
    else:
        c = mapping.get(s)
        res = res + (c.upper() if (cap and not shift) or (shift and not cap) else c)
print(res)
