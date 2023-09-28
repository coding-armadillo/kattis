cols = input().split()
m = int(input())
songs = [input().split() for _ in range(m)]
n = int(input())

for i in range(n):
    col = input()
    index = cols.index(col)
    songs = sorted(songs, key=lambda k: k[index])
    print(" ".join(cols))
    for song in songs:
        print(" ".join(song))
    if i < n - 1:
        print()
