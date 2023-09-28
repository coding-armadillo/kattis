import math

mapping = {
    "000": "0",
    "001": "1",
    "010": "2",
    "011": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7",
}
b = input()
length = 3 * math.ceil(len(b) / 3)
b = b.zfill(length)

print("".join([mapping[b[i : i + 3]] for i in range(0, length, 3)]))
