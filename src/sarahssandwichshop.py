dc_m = {
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
}
m = {}
for k, cs in dc_m.items():
    for c in cs:
        m[c] = k
n = int(input())
for _ in range(n):
    w = input()
    print(*[m[c.upper()] for c in w], sep="")
