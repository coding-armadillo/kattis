def adrian(n):
    if n == 0:
        return ""
    elif n == 1:
        return "A"
    elif n == 2:
        return "AB"
    elif n == 3:
        return "ABC"
    else:
        duplicate = n // 3
        return adrian(3) * duplicate + adrian(n % 3)


def bruno(n):
    if n == 0:
        return ""
    elif n == 1:
        return "B"
    elif n == 2:
        return "BA"
    elif n == 3:
        return "BAB"
    elif n == 4:
        return "BABC"
    else:
        duplicate = n // 4
        return bruno(4) * duplicate + bruno(n % 4)


def goran(n):
    if n == 0:
        return ""
    elif n in [1, 2]:
        return "C" * n
    elif n in [3, 4]:
        return "CC" + "A" * (n - 2)
    elif n in [5, 6]:
        return "CCAA" + "B" * (n - 4)
    else:
        duplicate = n // 6
        return goran(6) * duplicate + goran(n % 6)


def get_score(ans, guess):
    return sum([a == g for a, g in zip(ans, guess)])


n = int(input())
ans = input()

result = {}
result["Adrian"] = get_score(ans, adrian(n))
result["Bruno"] = get_score(ans, bruno(n))
result["Goran"] = get_score(ans, goran(n))

best = max(result.values())
print(best)

for name, score in result.items():
    if score == best:
        print(name)
