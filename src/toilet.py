t = input()


def u(pos, preference):
    if pos == preference == "U":
        return 0
    elif pos == preference == "D":
        return 1
    elif pos == "U" and preference == "D":
        return 2
    else:
        return 1


def l(pos, preference):
    if pos == preference == "U":
        return 1
    elif pos == preference == "D":
        return 0
    elif pos == "U" and preference == "D":
        return 1
    else:
        return 2


def b(pos, preference):
    if pos == preference:
        return 0
    else:
        return 1


pu = [u(pos, preference) for pos, preference in zip(t[0] + "U" * (len(t) - 2), t[1:])]
pl = [l(pos, preference) for pos, preference in zip(t[0] + "D" * (len(t) - 2), t[1:])]
pb = [b(pos, preference) for pos, preference in zip(t[0] + t[1:-1], t[1:])]

print(sum(pu))
print(sum(pl))
print(sum(pb))
