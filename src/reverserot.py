import string

rotations = string.ascii_uppercase + "_."


def rotate(c, n):
    index = (rotations.index(c) + n) % 28
    return rotations[index]


while True:
    line = input()
    if line == "0":
        break
    n, m = line.split()
    n = int(n)
    print("".join([rotate(c, n) for c in m[::-1]]))
