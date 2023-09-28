from collections import Counter

s = input()
cards = {
    "P": Counter(),
    "K": Counter(),
    "H": Counter(),
    "T": Counter(),
}
duplicated = False
for i in range(0, len(s), 3):
    suit = s[i]
    card = s[i + 1 : i + 3]
    if cards[suit][card]:
        duplicated = True
        break
    cards[suit][card] += 1

if not duplicated:
    print(" ".join([str(13 - len(c)) for c in cards.values()]))
else:
    print("GRESKA")
