import string
from random import choice, randint

vowels = set("aeiou")
consonants = set(string.ascii_lowercase) - vowels
names = set()


def f(w):
    return "".join([choice(list(consonants)) if c else choice(list(vowels)) for c in w])


for _ in range(int(input())):
    s = randint(3, 20)
    w = []
    for i in range(s):
        if i < 2:
            w.append(randint(0, 1))
        else:
            if w[-1] == w[-2]:
                w.append((w[-2] + 1) % 2)
            else:
                w.append(randint(0, 1))

    name = f(w)
    while name in names:
        name = f(w)
    names.add(name)

    print(name)
