def count(word):
    return sum(word.count(c * 2) for c in "aeiouy")


while True:
    n = int(input())
    if not n:
        break
    words = []
    for _ in range(n):
        words.append(input())
    print(max(words, key=count))
