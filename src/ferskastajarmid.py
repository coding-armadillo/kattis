n = int(input())
memes = {}
for _ in range(n):
    item = input().split()
    meme, score = item[0], int(item[1]) * int(item[2])
    memes[meme] = score
print(max(memes, key=lambda v: (memes[v], -sorted(memes).index(v))))
