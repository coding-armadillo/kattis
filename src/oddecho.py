n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i in range(0, n, 2):
    print(words[i])
