i = []
m = {
    "xxxxx" "x...x" "x...x" "x...x" "x...x" "x...x" "xxxxx": "0",
    "....x" "....x" "....x" "....x" "....x" "....x" "....x": "1",
    "xxxxx" "....x" "....x" "xxxxx" "x...." "x...." "xxxxx": "2",
    "xxxxx" "....x" "....x" "xxxxx" "....x" "....x" "xxxxx": "3",
    "x...x" "x...x" "x...x" "xxxxx" "....x" "....x" "....x": "4",
    "xxxxx" "x...." "x...." "xxxxx" "....x" "....x" "xxxxx": "5",
    "xxxxx" "x...." "x...." "xxxxx" "x...x" "x...x" "xxxxx": "6",
    "xxxxx" "....x" "....x" "....x" "....x" "....x" "....x": "7",
    "xxxxx" "x...x" "x...x" "xxxxx" "x...x" "x...x" "xxxxx": "8",
    "xxxxx" "x...x" "x...x" "xxxxx" "....x" "....x" "xxxxx": "9",
    "....." "..x.." "..x.." "xxxxx" "..x.." "..x.." ".....": "+",
}
for _ in range(7):
    i.append(input())

d = (len(i[0]) + 1) // 6

f = ""
for j in range(d):
    s = ""
    for _ in range(7):
        s += i[_][6 * j : 6 * j + 5]
    f += m[s]
ans = str(eval(f))

mm = {v: k for k, v in m.items()}
o = [""] * 7
for c in ans:
    for _ in range(7):
        o[_] += mm[c][5 * _ : 5 * _ + 5] + "."

for r in o:
    print(r[:-1])
