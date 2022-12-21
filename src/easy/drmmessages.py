l = ord("A")
r = ord("Z")


def divide(message):
    half = len(message) // 2
    return message[:half], message[half:]


def to_ord(c, rotation):
    new_chr = ord(c) + rotation
    return new_chr if new_chr <= r else l + (new_chr - r - 1)


def rotate(half):
    rotation = sum([ord(c) - l for c in half])
    rotation %= 26
    result = [to_ord(c, rotation) for c in half]
    return "".join([chr(c) for c in result])


def merge(first, second):
    rotations = [ord(c) - l for c in second]
    result = [to_ord(c, rotation) for c, rotation in zip(first, rotations)]
    return "".join([chr(c) for c in result])


message = input()
first, second = divide(message)
print(merge(rotate(first), rotate(second)))
