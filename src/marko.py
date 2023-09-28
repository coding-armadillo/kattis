mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
n = []
for _ in range(int(input())):
    w = input()
    t = ""
    for c in w:
        for d, r in mapping.items():
            if c in r:
                t += d
                break
    n.append(t)

d = input()
print(sum([d == t for t in n]))
