n, p = [int(d) for d in input().split()]
nouns = dict(tuple(input().split()) for _ in range(n))
phrases = []
for _ in range(p):
    row = input().split()
    row[-1] = nouns[row[-1]]
    phrases.append(" ".join(row))
rules = (
    "number of c",
    "amount of m",
    "most c",
    "most m",
    "fewest c",
    "least m",
    "more c",
    "more m",
    "fewer c",
    "less m",
    "many c",
    "much m",
    "few c",
    "little m",
)
for row in phrases:
    if row in rules:
        print("Correct!")
    else:
        print("Not on my watch!")
