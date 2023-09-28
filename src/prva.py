r, c = [int(d) for d in input().split()]
puzzle = []
for _ in range(r):
    puzzle.append(input())

words = set()
for row in puzzle:
    words.update([w for w in row.split("#") if len(w) > 1])
for i in range(c):
    col = "".join([row[i] for row in puzzle])
    words.update([w for w in col.split("#") if len(w) > 1])

print(sorted(words)[0])
